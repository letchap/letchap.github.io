#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'letchap'
SITENAME = u'letchap'
SITESUBTITLE = u'du Linux, du Python, un peu de Mac'
SITEURL = 'letchap.github.io'
TIMEZONE = 'Europe/Paris'

DEFAULT_METADATA = (('Linux', 'Python'),)

STATIC_PATHS = ['images', 'downloads', 'code']
PLUGIN_PATH = '/Users/frederic_chaput/pelican/plugins'
PLUGINS = ['liquid_tags.include_code']

ABSURL = 'letchap.github.io'
SIMPLE_SEARCH = 'http://google.com/search'



DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'fr'

GOOGLE_ANALYTICS = 'UA-37436504-2'

GITHUB_URL = 'http://github.com/letchap/'
DISQUS_SITENAME = 'letchap'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = 'atom.xml'

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social
SOCIAL = (('twitter', 'http://twitter.com/letchap'),
          ('github', 'http://github.com/letchap'),)
		  
# Pagination	  
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Paramètrage du thème
THEME = "//Users/frederic_chaput/pelican/mon-theme"

# Paramètrage de l'URL
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"




