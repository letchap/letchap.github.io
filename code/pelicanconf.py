AUTHOR = u'letchap'
SITENAME = u'letchap'
SITESUBTITLE = u'du Linux, du Python, un peu de Mac'
SITEURL = 'https://letchap.github.io'
TIMEZONE = 'Europe/Paris'

PATH = 'content'

DEFAULT_METADATA = (('Linux', 'Python'),)

STATIC_PATHS = ['images', 'downloads', 'code']

ABSURL = 'letchap.github.io'
SIMPLE_SEARCH = 'https://duckduckgo.com'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.addcode': {},
    },
    'output_format': 'html5',
}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = u'fr'
GOOGLE_ANALYTICS = "G-xxx"
GITHUB_URL = 'https://github.com/letchap/'

FEED_ALL_ATOM = 'atom.xml'



# Social
SOCIAL = (('mastodon', 'https://mastodon.social/@letchap'),
          ('github', 'https://github.com/letchap'),)

# Pagination
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 50

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Paramètrage du thème
THEME = "F6-theme"

# Paramètrage de l'URL
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
