"""
Copyright (c) 2016-2017 we-get developers (https://github.com/0xl3vi/we-get/)
See the file 'LICENSE' for copying.
"""

import urllib.request
import urllib.parse
from we_get.core.utils import random_user_agent
from html import unescape as html_decode

USER_AGENT = random_user_agent()

class Module(object):
    def __init__(self):
        self.cursor = None

    def http_get_request(self, url):
        """ http_request: create HTTP request.
	        @return: data.
        """
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', USER_AGENT), ("Accept", "*/*")]
        return opener.open(url).read().decode()

    def http_custom_get_request(self, url, headers):
        """ http_custom_get_request: HTTP GET request with custom headers. 
            @return: data.
        """
        opener = urllib.request.build_opener()
        opener.addheaders = headers
        return opener.open(url).read()

    def magnet2name(self, link):
        """ magnet2name: return torrent name from magnet link.
            @param magnet: link.
        """
        return link.split("&")[1].split("dn=")[1]

    def fix_name(self, name):
        """ fix_name: fix the torrent_name (Hello%20%20Worl+d to Hello_World).
            @parma name: torrent_name
        """
        name = html_decode(name)
        return urllib.parse.unquote(name.replace('+', '.')
            .replace('[', '')
            .replace(']', '')
            .replace(' ', '.')
            .replace('\'', ''))
