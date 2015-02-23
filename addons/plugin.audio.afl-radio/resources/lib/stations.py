#
#	 AFL Radio XBMC Plugin
#	 Copyright (C) 2012 Andy Botting
#
#	 AFL Radio is free software: you can redistribute it and/or modify
#	 it under the terms of the GNU General Public License as published by
#	 the Free Software Foundation, either version 3 of the License, or
#	 (at your option) any later version.
#
#	 AFL Radio is distributed in the hope that it will be useful,
#	 but WITHOUT ANY WARRANTY; without even the implied warranty of
#	 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	 GNU General Public License for more details.
#
#	 You should have received a copy of the GNU General Public License
#	 along with AFL Radio.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os
import config, utils, comm
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

def list_stations():

	__addon__ = xbmcaddon.Addon()

	# Show a dialog
	pDialog = xbmcgui.DialogProgress()
	pDialog.create(config.NAME, 'Fetching station list...')

	try:
		stations = comm.get_stations()

		if not stations:
			d = xbmcgui.Dialog()
			msg = utils.dialog_message("No stations found. This is usually because no matches are currently being played. Please try again later.")
			d.ok(*msg)
			return

		utils.log("Found %s stations" % len(stations))

		ok = True
		for s in stations:

			station_name = utils.get_station_name(s['id'])

			thumb = os.path.join(__addon__.getAddonInfo('path'), "resources", "img", "%s.jpg" % s['id'])

			listitem = xbmcgui.ListItem(station_name)
			labels = { "title": station_name,
						  "genre": "Sport" }

			listitem.setInfo(type='music', infoLabels=labels)
			listitem.setThumbnailImage(thumb)

			params = utils.make_url({ "id":   s['id'], 
											  "name": station_name, 
											  "url":  s['streamURL'] })

			url = "%s?%s" % (sys.argv[0], params)

			# Add the item to the list
			ok = xbmcplugin.addDirectoryItem(
						handle = int(sys.argv[1]),
						url = url,
						listitem = listitem,
						isFolder = True,
						totalItems = len(stations)
					)

		xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=ok)
	except:
		# user cancelled dialog or an error occurred
		d = xbmcgui.Dialog()
		msg = utils.dialog_error("Unable to fetch station list")
		d.ok(*msg)
		utils.log_error();
