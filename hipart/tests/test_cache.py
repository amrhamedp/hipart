# HiPart is a software toolkit to analyse molecular densities with the hirshfeld partitioning scheme.
# Copyright (C) 2007 - 2010 Toon Verstraelen <Toon.Verstraelen@UGent.be>
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


from hipart.tests.utils import iter_hf_sto3g_gaussian_caches, \
    iter_oh1_sto3g_gaussian_caches, iter_oh2_sto3g_gaussian_caches

import numpy, os
from nose.plugins.skip import SkipTest


def test_compute_atgrid_atweights():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_compute_atgrid_atweights, cache

def check_compute_atgrid_atweights(cache):
    cache.do_atgrids()
    cache.do_proatomfns()
    h0 = cache._compute_atweights(cache.atgrids[0], 0)
    h1 = cache._compute_atweights(cache.atgrids[0], 1)
    error = abs(h1+h0-1).max()
    assert(error < 1e-10)


def test_hf_charges():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_charges, cache

def check_hf_charges(cache):
    expected = {
        "hirsh": numpy.array([-0.13775422, 0.13775422]),
        "hirshi": numpy.array([-0.19453209, 0.19453209]),
        "isa": numpy.array([-0.20842675, 0.20842675]),
    }
    cache.do_charges()
    assert(abs(cache.charges - expected[cache.key]).max() < 1e-4)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_charges.txt" % cache.prefix)))


def test_oh1_charges():
    for cache in iter_oh1_sto3g_gaussian_caches():
        yield check_oh1_charges, cache

def check_oh1_charges(cache):
    expected = {
        "hirsh": numpy.array([-0.11261, 0.11261]),
        "hirshi": numpy.array([-0.17905023, 0.17905023]),
        "isa": numpy.array([-0.19495561, 0.19495561]),
    }
    cache.do_charges()
    assert(abs(cache.charges - expected[cache.key]).max() < 1e-3)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_charges.txt" % cache.prefix)))


def test_oh2_charges():
    for cache in iter_oh2_sto3g_gaussian_caches():
        yield check_oh2_charges, cache

def check_oh2_charges(cache):
    expected = {
        "hirsh": numpy.array([-0.11247028, 0.11247028]),
        "hirshi": numpy.array([-0.17877806, 0.17877806]),
        "isa": numpy.array([-0.19463722, 0.19463722]),
    }
    cache.do_charges()
    assert(abs(cache.charges - expected[cache.key]).max() < 1e-3)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_charges.txt" % cache.prefix)))


def test_hf_spin_charges():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_spin_charges, cache

def check_hf_spin_charges(cache):
    cache.do_spin_charges()
    assert(abs(cache.spin_charges).max() < 1e-4)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_spin_charges.txt" % cache.prefix)))


def test_oh1_spin_charges():
    for cache in iter_oh1_sto3g_gaussian_caches():
        yield check_oh1_spin_charges, cache

def check_oh1_spin_charges(cache):
    expected = {
        "hirsh": numpy.array([0.96630257, 0.03366921]),
        "hirshi": numpy.array([0.97163764, 0.0283441]),
        "isa": numpy.array([0.97359927, 0.02639019]),
    }
    cache.do_spin_charges()
    assert(abs(cache.spin_charges.sum() - 1.0) < 1e-3)
    assert(abs(cache.spin_charges - expected[cache.key]).max() < 1e-3)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_spin_charges.txt" % cache.prefix)))


def test_oh2_spin_charges():
    for cache in iter_oh2_sto3g_gaussian_caches():
        yield check_oh2_spin_charges, cache

def check_oh2_spin_charges(cache):
    expected = {
        "hirsh": numpy.array([1.00267536, -0.00270729]),
        "hirshi": numpy.array([1.00719451, -0.00721775]),
        "isa": numpy.array([1.00897117, -0.00899064]),
    }
    cache.do_spin_charges()
    assert(abs(cache.spin_charges.sum() - 1.0) < 1e-3)
    assert(abs(cache.spin_charges - expected[cache.key]).max() < 1e-3)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_spin_charges.txt" % cache.prefix)))


def test_hf_dipoles():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_dipoles, cache

def check_hf_dipoles(cache):
    expected = {
        "hirsh": numpy.array([
            [ 7.33577068e-06,  4.21284970e-06, -1.30711487e-01],
            [-1.08521488e-05, -2.42288956e-05, -8.07245252e-02],
        ]),
        "hirshi": numpy.array([
            [-8.37620473e-06, -1.14026188e-05, -6.96008618e-02],
            [-6.05490107e-06, -1.02980542e-05, -3.37416403e-02],
        ]),
        "isa": numpy.array([
            [-4.34535236e-06,  1.78233520e-05, -5.70034272e-02],
            [-1.13215867e-05, -5.19636426e-06, -1.97794421e-02],
        ]),
    }
    cache.do_dipoles()
    assert(abs(cache.dipoles - expected[cache.key]).max() < 1e-3)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_dipoles.txt" % cache.prefix)))


def test_hf_noble_radii():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_noble_radii, cache

def check_hf_noble_radii(cache):
    expected = numpy.array([0.32871748, 0.2])
    cache.do_noble_radii()
    assert(abs(cache.noble_radii - expected).max() < 1e-3)


def test_hf_bond_orders():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_bond_orders, cache

def check_hf_bond_orders(cache):
    expected_bond_orders = {
        "hirsh": numpy.array([
            [0.0, 1.17375318],
            [1.17375318, 0.0],
        ]),
        "hirshi": numpy.array([
            [0.0, 1.11411172],
            [1.11411172, 0.0],
        ]),
        "isa": numpy.array([
            [0.0, 1.09701044],
            [1.09701044, 0.0],
        ]),
    }
    expected_valences = {
        "hirsh": numpy.array([1.17377819, 1.17399224]),
        "hirshi": numpy.array([1.11407561, 1.11407691]),
        "isa": numpy.array([[1.09685209, 1.09681649]]),
    }
    cache.do_bond_orders()
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_bond_orders.txt" % cache.prefix)))
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_alpha_overlap.txt" % cache.prefix)))
    assert(abs(cache.bond_orders.sum(axis=0) - cache.valences).max() < 1e-2)
    assert(abs(cache.bond_orders - expected_bond_orders[cache.key]).max() < 1e-3)
    assert(abs(cache.valences - expected_valences[cache.key]).max() < 1e-3)


def test_oh1_bond_orders():
    raise SkipTest("Work in progress.")
    for cache in iter_oh1_sto3g_gaussian_caches():
        yield check_oh1_bond_orders, cache

def check_oh1_bond_orders(cache):
    expected_bond_orders = {
        "hirsh": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
        "hirshi": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
        "isa": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
    }
    expected_valences = {
        "hirsh": numpy.array([1.0, 1.0]),
        "hirshi": numpy.array([1.0, 1.0]),
        "isa": numpy.array([[1.0, 1.0]]),
    }
    cache.do_bond_orders()
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_bond_orders.txt" % cache.prefix)))
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_alpha_overlap.txt" % cache.prefix)))
    assert(abs(cache.bond_orders - expected_bond_orders[cache.key]).max() < 1e-3)
    assert(abs(cache.valences - expected_valences[cache.key]).max() < 1e-3)


def test_oh2_bond_orders():
    raise SkipTest("Work in progress.")
    for cache in iter_oh2_sto3g_gaussian_caches():
        yield check_oh2_bond_orders, cache

def check_oh2_bond_orders(cache):
    expected_bond_orders = {
        "hirsh": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
        "hirshi": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
        "isa": numpy.array([
            [0.0, 1.0],
            [1.0, 0.0],
        ]),
    }
    expected_valences = {
        "hirsh": numpy.array([0.0, 0.0]),
        "hirshi": numpy.array([0.0, 0.0]),
        "isa": numpy.array([[0.0, 0.0]]),
    }
    cache.do_bond_orders()
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_bond_orders.txt" % cache.prefix)))
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_alpha_overlap.txt" % cache.prefix)))
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_beta_overlap.txt" % cache.prefix)))
    assert(abs(cache.bond_orders - expected_bond_orders[cache.key]).max() < 1e-3)
    assert(abs(cache.valences - expected_valences[cache.key]).max() < 1e-3)


def test_hf_gross_net_populations():
    for cache in iter_hf_sto3g_gaussian_caches():
        yield check_hf_gross_net_populations, cache

def check_hf_gross_net_populations(cache):
    expected = {
        "hirsh": numpy.array([
            [8.89564521, 0.24206497],
            [0.24206497, 0.62019607],
        ]),
        "hirshi": numpy.array([
            [8.96906633, 0.22546657],
            [0.22546657, 0.58001127],
        ]),
        "isa": numpy.array([
            [8.98880362, 0.21955338],
            [0.21955338, 0.57209327],
        ]),
    }
    cache.do_gross_net_populations()
    assert(abs(cache.gross_net_populations - expected[cache.key]).max() < 1e-2)
    assert(os.path.isfile(os.path.join(cache.context.outdir, "%s_gross_net_populations.txt" % cache.prefix)))