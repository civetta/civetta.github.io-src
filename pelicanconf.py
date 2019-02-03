#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kelly Richardson'
SITENAME = "Kelly's Notebook"
SITEURL = 'kellysnotebook.com'
USER_LOGO_URL = "https://avatars1.githubusercontent.com/u/4553650?s=400&u=ed4a46a23eac9c188c95e48a93e97321a500a54a&v=4"
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'
PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
THEME = "voce"
PLUGIN_PATHS = ["voce/plugins"]
PLUGINS = ["assets"]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
