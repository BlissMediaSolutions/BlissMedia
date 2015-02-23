__author__ = 'bromix'

import xbmc
import xbmcgui

from ..abstract_context_ui import AbstractContextUI
from ... import constants

class XbmcContextUI(AbstractContextUI):
    def __init__(self, xbmc_addon, context):
        AbstractContextUI.__init__(self)

        self._xbmc_addon = xbmc_addon

        self._context = context
        self._view_mode = None
        pass

    def set_view_mode(self, view_mode):
        print "################################# set view %s" % view_mode
        if isinstance(view_mode, basestring):
            view_mode = self._context.get_settings().get_int(constants.setting.VIEW_X % view_mode, 50)
            print "################################# new view %d" % view_mode
            pass
        self._view_mode = view_mode
        pass

    def get_view_mode(self):
        if self._view_mode is not None:
            return self._view_mode

        return self._context.get_settings().get_int(constants.setting.VIEW_DEFAULT, 50)

    def get_skin_id(self):
        return xbmc.getSkinDir()

    def on_keyboard_input(self, title, default='', hidden=False):
        keyboard = xbmc.Keyboard(default, title, hidden)
        keyboard.doModal()
        if keyboard.isConfirmed() and keyboard.getText():
            text = keyboard.getText()
            """
            It seams kodi returns utf-8 encoded strings. We need unicode (multibyte) strings. We check if the
            text is str and call decode to create afterwards an unicode string.
            """
            if isinstance(text, str):
                text = unicode(text.decode('utf-8'))
                pass
            return True, text

        return False, u''

    def on_numeric_input(self, title, default=''):
        dialog = xbmcgui.Dialog()
        result = dialog.input(title, str(default), type=xbmcgui.INPUT_NUMERIC)
        if result:
            return True, int(result)

        return False, None

    def on_yes_no_input(self, title, text):
        dialog = xbmcgui.Dialog()
        return dialog.yesno(title, text)

    def on_select(self, title, items=[]):
        _dict = {}
        _items = []
        i = 0
        for item in items:
            if isinstance(item, tuple):
                _dict[i] = item[1]
                _items.append(item[0])
                pass
            else:
                _dict[i] = i
                _items.append(item)
                pass

            i += 1
            pass

        dialog = xbmcgui.Dialog()
        result = dialog.select(title, _items)
        return _dict.get(result, -1)

    def show_notification(self, message, header='', image_uri='', time_milliseconds=5000):
        _header = header
        if not _header:
            _header = self._context.get_name()
            pass

        _image = image_uri
        if not _image:
            _image = self._context.get_icon()
            pass

        xbmc.executebuiltin(
            "Notification(%s, %s, %d, %s)" % (_header, message.replace(',', ' '), time_milliseconds, _image))
        pass

    def open_settings(self):
        self._xbmc_addon.openSettings()
        pass

    def refresh_container(self):
        xbmc.executebuiltin("Container.Refresh")
        pass

    pass
