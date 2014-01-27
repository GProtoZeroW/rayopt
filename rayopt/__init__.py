# -*- coding: utf8 -*-
#
#   pyrayopt - raytracing for optical imaging systems
#   Copyright (C) 2012 Robert Jordens <jordens@phys.ethz.ch>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, absolute_import, division

from .material import (fraunhofer, AllGlasses, ModelMaterial,
    SellmeierMaterial, GasMaterial, mirror)
from .elements import Spheroid, Object, Aperture, Image
from .system import System
from .formats import (system_from_text, system_from_zemax,
    system_from_oslo, system_from_yaml, system_to_yaml,
    system_from_json, system_to_json)
from .raytrace import (GeometricTrace, ParaxialTrace, GaussianTrace,
    FullTrace)
from .analysis import Analysis
#from .optimize import (Parameter, MaterialThickness, 
#    demerit_rms_position, demerit_rms_angle, demerit_mean_angle,
#    demerit_aberration3)
