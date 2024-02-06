from pathlib import Path

STATIC_DIRECTORY = "static"
TEMPLATES_DIRECTORY = "templates"
STATIC_JS = Path(STATIC_DIRECTORY, "js")
STATIC_SRC = Path(STATIC_DIRECTORY, "src")
STATIC_CSS = Path(STATIC_DIRECTORY, "style")

# ***** htmx
# config
HTMX_FILENAME = "htmx.min.js"
HTMX_VERSION = "1.9.10"
HTMX_CDN = "https://unpkg.com/htmx.org@{version}/dist/htmx.min.js"
# vars
HTMX_INPUT_URL = HTMX_CDN.format(version=HTMX_VERSION)
HTMX_OUTPUT_PATH = STATIC_JS.joinpath(HTMX_FILENAME)

# ***** Alpinejs
# config
ALPINEJS_FILENAME = "alpinejs.min.js"
ALPINEJS_VERSION = "3.13.5"
ALPINEJS_CDN = "https://cdn.jsdelivr.net/npm/alpinejs@{version}/dist/cdn.min.js"
# vars
ALPINEJS_INPUT_URL = ALPINEJS_CDN.format(version=ALPINEJS_VERSION)
ALPINEJS_OUTPUT_PATH = STATIC_JS.joinpath(ALPINEJS_FILENAME)

# ***** Tailwind CSS
# config
TAILWINDCSS_FILENAME_INPUT = "input.css"
TAILWINDCSS_FILENAME_OUTPUT = "output.css"
# vars
TAILWINDCSS_INPUT_PATH = STATIC_SRC.joinpath(TAILWINDCSS_FILENAME_INPUT)
TAILWINDCSS_OUTPUT_PATH = STATIC_CSS.joinpath(TAILWINDCSS_FILENAME_OUTPUT)

CDN_MODULES = [
    {"url": HTMX_INPUT_URL, "path": HTMX_OUTPUT_PATH},
    {"url": ALPINEJS_INPUT_URL, "path": ALPINEJS_OUTPUT_PATH},
]

# ***** Favicon
FAVICON_FILENAME = "favicon_io.zip"
FAVICON_INPUT_PATH = STATIC_SRC.joinpath(FAVICON_FILENAME)
FAVICON_OUTPUT_FOLDER = Path(STATIC_DIRECTORY, "assets", "favicon")
