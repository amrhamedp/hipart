#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HiPart is a program to analyze the electronic structure of molecules with
# fuzzy-atom partitioning methods.
# Copyright (C) 2007 - 2012 Toon Verstraelen <Toon.Verstraelen@UGent.be>
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
#--


from hipart.opts import parse_command_line

usage = """%prog computes atomic charges and dipoles.

These atomic charges and dipoles are the monopole and dipole terms in the
multipole expansion of each atomic contribution to the density. The atomic
densities are obtained from the 'scheme' specified at the command line."""

context, scheme = parse_command_line(usage)
scheme.do_dipoles()
context.work.clean()
