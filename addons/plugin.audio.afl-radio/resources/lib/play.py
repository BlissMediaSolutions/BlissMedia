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
import config, utils
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

def play(params):
	__addon__ = xbmcaddon.Addon()

	p = utils.get_url(params)

	# Show a dialog
	d = xbmcgui.DialogProgress()
	d.create(config.NAME, "Starting %s..." % p['name'])

	try:
		thumb = os.path.join(__addon__.getAddonInfo('path'), "resources", "img", "%s.jpg" % p['id'])
		labels = {
			"title": p['name'],
			"artist": "AFL Radio",
			"genre": "Sport"
		}
		listitem = xbmcgui.ListItem(p['name'])
		listitem.setInfo(type='music', infoLabels=labels)
		listitem.setThumbnailImage(thumb)

		# PAPlayer or AUTO fails here for some absurd reason
		xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(p['url'], listitem)
	except:
		# user cancelled dialog or an error occurred
		d = xbmcgui.Dialog()
		message = utils.dialog_error("Unable to play %s" % p['name'])
		d.ok(*message)
		utils.log_error();
