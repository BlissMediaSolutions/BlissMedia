#
#    AFL Radio XBMC Plugin
#    Copyright (C) 2012 Andy Botting
#
#    AFL Radio is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    AFL Radio is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with AFL Radio.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys

# Add our resources/lib to the python path
try:
   current_dir = os.path.dirname(os.path.abspath(__file__))
except:
   current_dir = os.getcwd()

sys.path.append( os.path.join( current_dir, "resources", "lib" ) )

import utils, config, stations, play

utils.log('Initialised')

if __name__ == "__main__" :
	params = sys.argv[2]
	p = utils.get_url(params)

	if p.has_key('id'):
		play.play(params)
	else:
		stations.list_stations()

