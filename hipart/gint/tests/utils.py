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



import os, tempfile


__all__ = ["setup_fchk", "hf_fchk"]


def setup_fchk(fchk_str):
    tmpdir = tempfile.mkdtemp("hipart")
    fn_fchk = os.path.join(tmpdir, "gaussian.fchk")
    f = open(fn_fchk, "w")
    f.write(fchk_str)
    f.close()
    return tmpdir, fn_fchk


hf_fchk="""\
hcl
SP        RHF                                                         STO-3G
Number of atoms                            I                2
Charge                                     I                0
Multiplicity                               I                1
Number of electrons                        I               10
Number of alpha electrons                  I                5
Number of beta electrons                   I                5
Number of basis functions                  I                6
Number of independant functions            I                6
Number of contracted shells                I                3
Highest angular momentum                   I                1
Largest degree of contraction              I                3
Number of primitive shells                 I                9
SCF Energy                                 R     -9.856961609951867E+01
Total Energy                               R     -9.856961609951867E+01
Atomic numbers                             I   N=           2
           9           1
Nuclear charges                            R   N=           2
  9.00000000E+00  1.00000000E+00
Current cartesian coordinates              R   N=           6
  0.00000000E+00  0.00000000E+00  1.90484394E-01  0.00000000E+00  0.00000000E+00
 -1.71435955E+00
Shell types                                I   N=           3
           0          -1           0
Number of primitives per shell             I   N=           3
           3           3           3
Shell to atom map                          I   N=           3
           1           1           2
Primitive exponents                        R   N=           9
  1.66679134E+02  3.03608123E+01  8.21682067E+00  6.46480325E+00  1.50228124E+00
  4.88588486E-01  3.42525091E+00  6.23913730E-01  1.68855404E-01
Contraction coefficients                   R   N=           9
  1.54328967E-01  5.35328142E-01  4.44634542E-01 -9.99672292E-02  3.99512826E-01
  7.00115469E-01  1.54328967E-01  5.35328142E-01  4.44634542E-01
P(S=P) Contraction coefficients            R   N=           9
  0.00000000E+00  0.00000000E+00  0.00000000E+00  1.55916275E-01  6.07683719E-01
  3.91957393E-01  0.00000000E+00  0.00000000E+00  0.00000000E+00
Alpha Orbital Energies                     R   N=           6
 -2.59083334E+01 -1.44689996E+00 -5.57467136E-01 -4.62288194E-01 -4.62288194E-01
  5.39578910E-01
Alpha MO coefficients                      R   N=          36
  9.94803448E-01  2.18171240E-02  0.00000000E+00  0.00000000E+00 -2.32641328E-03
 -4.79956235E-03 -2.52541943E-01  9.59473606E-01  0.00000000E+00  0.00000000E+00
 -6.43303484E-02  1.39537839E-01 -7.25975847E-02  3.79097630E-01  0.00000000E+00
  0.00000000E+00  6.93582825E-01 -5.48754967E-01  0.00000000E+00  0.00000000E+00
  1.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00
  0.00000000E+00  0.00000000E+00  1.00000000E+00  0.00000000E+00  0.00000000E+00
  7.48777677E-02 -4.62627490E-01  0.00000000E+00  0.00000000E+00  8.05942415E-01
  1.01124712E+00
Total SCF Density                          R   N=          21
  2.11736348E+00 -4.96250301E-01  2.12956120E+00  0.00000000E+00  0.00000000E+00
  2.00000000E+00  0.00000000E+00  0.00000000E+00  0.00000000E+00  2.00000000E+00
 -7.28413014E-02  4.02323157E-01  0.00000000E+00  0.00000000E+00  9.70401883E-01
 -3.50985618E-04 -1.48507094E-01  0.00000000E+00  0.00000000E+00 -7.79144745E-01
  6.41251717E-01
Dipole Moment                              R   N=           3
  0.00000000E+00  0.00000000E+00 -4.73896291E-01
"""
