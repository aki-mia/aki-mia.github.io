AUTHOR = "aki-mia"
SITENAME = "FrontEnd and DataScience memo"
SITEURL = ""

PATH = "content"
THEME = "themes/Flex"

TIMEZONE = "Asia/Tokyo"

DEFAULT_LANG = "ja"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("View on GitHub", "https://github.com/aki-mia"),
)

# コードハイライトの色指定
PYGMENTS_STYLE = "monokai"

# Social widget
SOCIAL = (
    ("github", "https://github.com/aki-mia"),
    ("twitter", "https://twitter.com/aki_honmono"),
    ("linkedin", "https://www.linkedin.com/in/akihirotanii/"),
)

DEFAULT_PAGINATION = 10

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.fenced_code": {},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.admonition": {},
        "mdx_linkify.mdx_linkify": {},
    },
    "output_format": "html5",
}

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "related_posts",
    "neighbors",
    "plantuml",
]
RELATED_POSTS_MAX = 5

# ページ下部にライセンス表記を追加
COPYRIGHT_NAME = "aki-mia.github.io"
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "1.0",
    "slug": "by-sa",
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
