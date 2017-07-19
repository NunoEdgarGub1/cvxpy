"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy as np

from cvxpy.expressions.constants import Constant
from cvxpy.expressions.variables.variable import Variable


def max_entries_canon(expr, args):
    x = args[0]
    shape = expr.shape
    axis = expr.axis
    t = Variable(shape)

    if axis is None:  # shape = (1, 1)
        promoted_t = Constant(np.ones(x.shape)) * t
    elif axis == 0:  # shape = (1, n)
        promoted_t = Constant(np.ones((x.shape[0], 1))) * t
    else:  # shape = (m, 1)
        promoted_t = t * Constant(np.ones((1, x.shape[1])))

    constraints = [x <= promoted_t]
    return t, constraints
