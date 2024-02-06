from typing import Annotated

from __init__ import app_info
from environment import (
    ALPINEJS_OUTPUT_PATH,
    HTMX_OUTPUT_PATH,
    STATIC_DIRECTORY,
    TAILWINDCSS_OUTPUT_PATH,
    TEMPLATES_DIRECTORY,
)
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from helpers import lifespan

app = FastAPI(**app_info, lifespan=lifespan)
app.mount(f"/{STATIC_DIRECTORY}", StaticFiles(directory=STATIC_DIRECTORY))
templates = Jinja2Templates(directory=TEMPLATES_DIRECTORY)


def static_paths() -> dict[str, str]:
    """
    Returns a dict containing the paths to be used in the
    HTML links and scripts for (h)tmx, (a)lpine.js and (t)ailwind
    """

    return {
        "htmx": str(HTMX_OUTPUT_PATH),
        "alpinejs": str(ALPINEJS_OUTPUT_PATH),
        "tailwindcss": str(TAILWINDCSS_OUTPUT_PATH),
    }


@app.get("/", response_class=HTMLResponse)
def root(
    request: Request,
    static_paths: Annotated[dict[str, str], Depends(static_paths)],
):
    """
    Root endpoint
    """

    params = {
        "request": request,
        "name": "index.html",
        "context": {
            **app_info,
            "static_paths": static_paths,
        },
    }

    return templates.TemplateResponse(**params)
