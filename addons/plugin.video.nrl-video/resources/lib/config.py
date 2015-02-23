#
#    NRL Video XBMC Plugin
#    Copyright (C) 2012 Andy Botting
#
#    NRL Video is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    NRL Video is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with NRL Video.  If not, see <http://www.gnu.org/licenses/>.
#

NAME = 'NRL Video'
VERSION = '0.2'

# Video quality static definitions with match the setings.xml
QUAL_LOW = '0'
QUAL_MED = '1'
QUAL_HIGH = '2'

# Standard Bigpond Sport/NRL channels
# Channel number was discovered from http://bigpondvideo.com/
# and using a web proxy, extract the AMF data when clicking each channel
# to find its 'NavID' 
# channel value matches with the teams list in the settings.xml
CHANNELS = [
	{ 'name': 'Club Content',		'channel': 'teams' },
	{ 'name': 'Latest',				'channel': '490' },
	{ 'name': 'Highlights',			'channel': '503' },
	{ 'name': 'Matches',			'channel': '491' },
	{ 'name': 'Round in Review',	'channel': '505' },
	{ 'name': 'Best Hits',			'channel': '506' },	
	{ 'name': 'Best Tries',			'channel': '507' }
]

TEAMS = [
	{'id': '1',		'name': 'Broncos',		'channel': '748',	'thumb': 'Broncos.jpeg' },
	{'id': '2',		'name': 'Bulldogs',		'channel': '749',	'thumb': 'Bulldogs.jpeg' },
	{'id': '3',		'name': 'Cowboys',		'channel': '751',	'thumb': 'Cowboys.jpeg' },
	{'id': '4',		'name': 'Drangons',		'channel': '759',	'thumb': 'Drangons.jpeg' },
	{'id': '5',		'name': 'Eels',			'channel': '755',	'thumb': 'Eels.jpeg'  },
	{'id': '6',		'name': 'Knights',		'channel': '754',	'thumb': 'Knights.jpeg'  },
	{'id': '7',		'name': 'Panthers',		'channel': '756',	'thumb': 'Panthers.jpeg'  },
	{'id': '8',		'name': 'Rabbitohs',	'channel': '758',	'thumb': 'Rabbitohs.jpeg'  },
	{'id': '9',		'name': 'Raiders',		'channel': '756',	'thumb': 'Raiders.jpeg'  },
	{'id': '10',	'name': 'Rooster',		'channel': '760',	'thumb': 'Rooster.jpeg'  },
	{'id': '11',	'name': 'Sea Eagles',	'channel': '752',	'thumb': 'SeaEagles.jpeg'  },
	{'id': '12',	'name': 'Sharks',		'channel': '757',	'thumb': 'Sharks.jpeg'  },
	{'id': '13',	'name': 'Storm',		'channel': '753',	'thumb': 'Storm.jpeg'  },
	{'id': '14',	'name': 'Titans',		'channel': '763',	'thumb': 'Titans.jpeg'  },
	{'id': '15',	'name': 'Warriors',		'channel': '761',	'thumb': 'Warriors.jpeg'  },
	{'id': '16',	'name': 'West Tigers',	'channel': '762',	'thumb': 'WestTigers.jpeg'  }
]

