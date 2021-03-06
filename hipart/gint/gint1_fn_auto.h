// HiPart is a software toolkit to analyse molecular densities with the hirshfeld partitioning scheme.
// Copyright (C) 2007 - 2010 Toon Verstraelen <Toon.Verstraelen@UGent.be>
//
// This file is part of HiPart.
//
// HiPart is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 3
// of the License, or (at your option) any later version.
//
// HiPart is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, see <http://www.gnu.org/licenses/>
//
// --


#ifndef GINT1_FN_AUTO_H
#define GINT1_FN_AUTO_H

#define MAX_SHELL 3
#define NUM_SHELL_TYPES 7
#define MAX_SHELL_DOF 10
#define CHECK_ALLOC(pointer) if (pointer==NULL) {result = -1; goto EXIT; }
#define CHECK_SHELL(shell_type) if (abs(shell_type) > MAX_SHELL) { result = -2; goto EXIT; }
#define GET_SHELL_DOF(shell_type) ((shell_type<-1)?(-2*shell_type+1):((shell_type==-1)?(4):(((shell_type+1)*(shell_type+2))/2)))

void gint1_fn_pF(double* a, double a_a, double* p, double* out);
void gint1_fn_pD(double* a, double a_a, double* p, double* out);
void gint1_fn_SP(double* a, double a_a, double* p, double* out);
void gint1_fn_S(double* a, double a_a, double* p, double* out);
void gint1_fn_P(double* a, double a_a, double* p, double* out);
void gint1_fn_cD(double* a, double a_a, double* p, double* out);
void gint1_fn_cF(double* a, double a_a, double* p, double* out);
void gint1_fn_dispatch(int a_s, double* a, double a_a, double* p, double* out);

#endif
