"""
Copyright (C) 2014 Erika Baena et Diana Malabard

This file is part of TreeDisplay.

    TreeDisplay is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TreeDisplay is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

from tree import *

def toTikz (t, withLabels = False, fileName = "treeTikz.tex"):
	"Generate an output file which name is fileName with the coordonates of the tree t. Node labels are displayed if withLabels is True"
	f = open (fileName, "w")
	if (withLabels):
		toTikzRecWith (t, f)
	else:
		toTikzRecWithout (t, f)
	f.close()


def toTikzRecWith (t, f):
	f.write("\\node (a%d) at (%f, -%f) {%s};\n" % (id(t), t.x, t.y, t.label,))
	for c in t.children:
		toTikzRecWith (c, f)
		f.write("\\draw (a%d) -- (a%d);\n" % (id(t), id(c),))


def toTikzRecWithout (t, f):
	for c in t.children:
		toTikzRecWithout (c, f)
		f.write("\\draw (%f, -%f) -- (%f, -%f);\n" % (t.x, t.y, c.x, c.y,))