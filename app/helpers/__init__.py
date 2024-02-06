import os
import shutil
import subprocess
from contextlib import asynccontextmanager
from typing import Union
from zipfile import ZipFile

import requests
from environment import (
    CDN_MODULES,
    FAVICON_INPUT_PATH,
    FAVICON_OUTPUT_FOLDER,
    STATIC_JS,
    TAILWINDCSS_INPUT_PATH,
    TAILWINDCSS_OUTPUT_PATH,
)
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    install_cdn_modules(CDN_MODULES, STATIC_JS)
    install_zip(FAVICON_INPUT_PATH, FAVICON_OUTPUT_FOLDER)
    build_tailwind(TAILWINDCSS_INPUT_PATH, TAILWINDCSS_OUTPUT_PATH)

    yield

    shutil.rmtree(STATIC_JS)
    shutil.rmtree(FAVICON_OUTPUT_FOLDER)
    os.remove(TAILWINDCSS_OUTPUT_PATH)


def install_cdn_modules(
    modules: list[dict[str, Union[str, os.PathLike]]],
    folder: os.PathLike,
):
    os.makedirs(folder, exist_ok=True)

    for module in modules:
        module_contents = requests.get(module["url"]).text
        module_path = module["path"]
        write_file(module_contents, module_path)


def write_file(text: str, file_path: os.PathLike):
    with open(file_path, "w") as f:
        f.write(text)


def install_zip(input: os.PathLike, output: os.PathLike):
    with ZipFile(input, "r") as zip:
        zip.extractall(output)


def build_tailwind(input: os.PathLike, output: os.PathLike):
    command = ["tailwindcss", "-i", str(input), "-o", str(output), "--minify"]
    subprocess.run(command)
