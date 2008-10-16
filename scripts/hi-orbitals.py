#!/usr/bin/python
# HiPart is a tool to analyse molecular densities with the hirshfeld partitioning scheme
# Copyright (C) 2007 - 2008 Toon Verstraelen <Toon.Verstraelen@UGent.be>
#
# This file is part of HiPart.
#
# HiPart is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# HiPart is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --


from molmod.io.gaussian03.fchk import FCHKFile
from molmod.data.periodic import periodic
from molmod.units import angstrom

from hipart.core import *
from hipart.lebedev_laikov import get_grid, grid_fns
from hipart.tools import load_cube, write_atom_grid

from optparse import OptionParser
import os, shutil, copy, sys, numpy


parser = OptionParser("%prog [options] densities.txt gaussian.fchk")
parser.add_option(
    "-l", "--lebedev", default=110, type='int',
    help="The number of grid points for the spherical averaging. "
    "[default=%default]. Select from: " + (", ".join(str(i) for i in sorted(grid_fns)))
)
(options, args) = parser.parse_args()
densities_filename, fchk_filename = args

rootdir = os.path.dirname(fchk_filename)
prefix = os.path.basename(fchk_filename).replace(".fchk", "")
workdir = os.path.join(rootdir, "%s-hipart-work" % prefix)
out_fn = os.path.join(rootdir, "%s-hipart-orbitals.out" % prefix)

if os.path.isfile(out_fn):
    print "Nothing todo. Bye bye."
    sys.exit()


# A) Load FCHK file and atomic densities
fchk = FCHKFile(fchk_filename, field_labels=["Number of basis functions"])
at = AtomTable(densities_filename)

# B) Compute densities on atomic grids
if not os.path.isdir(workdir):
    os.mkdir(workdir)

# B.0) make the lebedev grid
num_lebedev = options.lebedev
lebedev_xyz, lebedev_weights = get_grid(num_lebedev)

# B.1) call cubegen a few times, we assume restricted scf
num_orbitals = fchk.fields.get("Number of basis functions")
pb = ProgressBar("Orbitals on atomic grids", fchk.molecule.size*num_orbitals)
for i, number in enumerate(fchk.molecule.numbers):
    grid_written = False
    for j in xrange(num_orbitals):
        pb()
        cube_fn = os.path.join(workdir, "atom%05iorb%05i.cube" % (i,j))
        cube_fn_bin = "%s.bin" % cube_fn
        if not os.path.isfile(cube_fn_bin):
            if not os.path.isfile(cube_fn):
                if not grid_written:
                    center = fchk.molecule.coordinates[i]
                    grid_prefix = os.path.join(workdir, "atom%05igrid" % i)
                    write_atom_grid(grid_prefix, lebedev_xyz, center, at.records[number].rs)
                    grid_written = True
                os.system(". ~/g03.profile; cubegen 0 MO=%i %s %s -5 < %s" % (
                    j+1, fchk_filename, cube_fn, os.path.join(workdir, "atom%05igrid.txt" % i),
                ))
            values = load_cube(cube_fn, values_only=True)
            os.remove(cube_fn)
            values.tofile("%s.bin" % cube_fn)
    if grid_written:
        os.remove("%s.txt" % grid_prefix)
pb()


# C) Precompute distances and load density data
distances = {}
pb = ProgressBar("Precomputing distances", fchk.molecule.size**2)
for i, number_i in enumerate(fchk.molecule.numbers):
    grid_fn_bin = os.path.join(workdir, "atom%05igrid.bin" % i)
    grid_points = numpy.fromfile(grid_fn_bin, float).reshape((-1,3))
    for j, number_j in enumerate(fchk.molecule.numbers):
        pb()
        if i!=j:
            distances[(i,j)] = numpy.sqrt(((grid_points - fchk.molecule.coordinates[j])**2).sum(axis=1))
pb()



# D) Compute the matrix elements
f = file(out_fn, "w")
print >> f, "numorb =", num_orbitals
print >> f, "numat =", fchk.molecule.size

# construct the pro-atom density functions, using the densities from the
# previous iteration
atom_fns = []
for i, number_i in enumerate(fchk.molecule.numbers):
    atom_fns.append(at.records[number_i].get_atom_fn(0))

pb = ProgressBar("Atom centered matrices", fchk.molecule.size)
# Run over each atom and ...
for i, number_i in enumerate(fchk.molecule.numbers):
    pb()
    # construct the pro-atom and pro-molecule on this atomic grid
    atom_weights = numpy.array([atom_fns[i].density.y]*num_lebedev).transpose().ravel()
    promol_weights = numpy.zeros(len(atom_weights), float)
    for j, number_j in enumerate(fchk.molecule.numbers):
        if i==j:
            promol_weights += atom_weights
        else:
            promol_weights += atom_fns[j].density(distances[(i,j)])

    # avoid division by zero
    atom_weights[promol_weights < 1e-40] = 1e-40
    promol_weights[promol_weights < 1e-40] = 1e-40
    # multiply the density on the grid by the weight function
    hirshfeld_weights = atom_weights/promol_weights

    orbitals = []
    for j in xrange(num_orbitals):
        cube_fn_bin = os.path.join(workdir, "atom%05iorb%05i.cube.bin" % (i,j))
        orbitals.append(numpy.fromfile(cube_fn_bin, float))
    matrix = numpy.zeros((num_orbitals,num_orbitals), float)
    for j1 in xrange(num_orbitals):
        for j2 in xrange(j1+1):
            r = at.records[number_i].rs
            integrand = orbitals[j1]*orbitals[j2]*hirshfeld_weights
            radfun = (integrand.reshape((-1,num_lebedev))*lebedev_weights).sum(axis=1)*4*numpy.pi
            value = integrate(r, radfun*r*r)
            matrix[j1,j2] = value
            matrix[j2,j1] = value
    print >> f, "Atom %i: %s" % (i, periodic[number].symbol)
    for row in matrix:
        print >> f, " ".join("% 15.10e" % value for value in row)
pb()
f.close()


