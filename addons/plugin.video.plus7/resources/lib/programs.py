#
#   Plus7 XBMC Plugin
#   Copyright (C) 2014 Andy Botting
#
#
#   This plugin is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This plugin is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this plugin. If not, see <http://www.gnu.org/licenses/>.
#

import sys
import utils
import comm

import xbmcgui
import xbmcplugin


def make_programs_list(url):
    try:
        params = utils.get_url(url)
        programs = comm.get_series(params["series_id"])
        num_programs = len(programs)

        ok = True
        for p in programs:

            # Don't show any 'promo' shows. They don't get returned by Brightcove
            if p.duration < 1200:
                utils.log("Skipping program %s (duration <20 mins)" % p.get_list_title())
                num_programs -= 1
                continue

            listitem = xbmcgui.ListItem(label=p.get_list_title(), iconImage=p.get_thumbnail(), thumbnailImage=p.get_thumbnail())
            listitem.setInfo('video', p.get_xbmc_list_item())

            if hasattr(listitem, 'addStreamInfo'):
                listitem.addStreamInfo('audio', p.get_xbmc_audio_stream_info())
                listitem.addStreamInfo('video', p.get_xbmc_video_stream_info())

            # Build the URL for the program, including the list_info
            url = "%s?program_id=%s" % (sys.argv[0], p.id)

            # Add the program item to the list
            ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=False, totalItems=num_programs)

        xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=ok)
        xbmcplugin.setContent(handle=int(sys.argv[1]), content='episodes')
    except:
        utils.handle_error("Unable to fetch program listing")
