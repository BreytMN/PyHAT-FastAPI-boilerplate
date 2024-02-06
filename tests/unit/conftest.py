import os
import sys

SYSPATH = "./app"
LOGS_PREFIX = "logs"

sys.path.insert(0, SYSPATH)

dummy_files = (
    f"{LOGS_PREFIX}/info.log",
    f"{LOGS_PREFIX}/debug.log",
)


def pytest_sessionstart(session):
    os.chdir(SYSPATH)

    for name in dummy_files:
        with open(name, "w") as f:
            f.write("")


def pytest_sessionfinish(session, exitstatus):
    os.chdir(SYSPATH)

    for name in dummy_files:
        os.remove(name)
