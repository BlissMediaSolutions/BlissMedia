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

NAME = 'AFL Radio'
VERSION = '0.4'

# This URL returns a token if POST'ed to. The token is required in the header to any
# reqeusts against the API
TOKEN_URL = 'http://api.afl.com.au/cfs/afl/WMCTok'

LIVE_AUDIO_URL = 'http://api.afl.com.au/cfs/afl/liveAudioStreams'

# Stations list
STATIONS = [
	{ 'name':'SEN Melbourne',                     'id':'AFL_RADIO1' },
	{ 'name':'ABC774',                            'id':'AFL_RADIO2' },
	{ 'name':'5AA Adelaide',                      'id':'AFL_RADIO3' },
	{ 'name':'6PR Perth',                         'id':'AFL_RADIO4' },
	{ 'name':'3AW Melbourne',                     'id':'AFL_RADIO5' },
	{ 'name':'National Indigenous Radio Service', 'id':'AFL_RADIO6' },
	{ 'name':'Gold FM Gold Coast',                'id':'AFL_RADIO7' },
	{ 'name':'AFL Live',                          'id':'AFL_RADIO8' },
	{ 'name':'Triple M Sydney',                   'id':'AFL_RADIO11' },
	{ 'name':'Triple M Melbourne',                'id':'AFL_RADIO12' },
	{ 'name':'Triple M Brisbane',                 'id':'AFL_RADIO13' },
	{ 'name':'Triple M Adelaide',                 'id':'AFL_RADIO14' },
	{ 'name':'K-Rock Geelong',                    'id':'AFL_RADIO15' },
]
