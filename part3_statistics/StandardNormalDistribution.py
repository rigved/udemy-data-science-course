"""
StandardNormalDistribution.py
Copyright (C) 2020 Rigved Rakshit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np


def convert_to_standard_normal_distribution(distribution):
    original_mean = np.mean(distribution)
    original_stdev = np.std(distribution)

    standard_normal_distribution = (distribution - original_mean) / original_stdev

    return standard_normal_distribution


if __name__ == '__main__':
    original_distribution = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    print(convert_to_standard_normal_distribution(original_distribution))
