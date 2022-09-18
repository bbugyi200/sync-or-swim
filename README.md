# sync_or_swim

**Sync your data files across all of your machines (tinyurl.com/sync-or-swim)**

_project status badges:_

[![CI Workflow](https://github.com/bbugyi200/sync-or-swim/actions/workflows/ci.yml/badge.svg)](https://github.com/bbugyi200/sync-or-swim/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/bbugyi200/sync-or-swim/branch/master/graph/badge.svg)](https://codecov.io/gh/bbugyi200/sync-or-swim)
[![Documentation Status](https://readthedocs.org/projects/sync-or-swim/badge/?version=latest)](https://sync-or-swim.readthedocs.io/en/latest/?badge=latest)
[![Package Health](https://snyk.io/advisor/python/sync-or-swim/badge.svg)](https://snyk.io/advisor/python/sync-or-swim)

_version badges:_

[![Project Version](https://img.shields.io/pypi/v/sync-or-swim)](https://pypi.org/project/sync-or-swim/)
[![Python Versions](https://img.shields.io/pypi/pyversions/sync-or-swim)](https://pypi.org/project/sync-or-swim/)
[![Cookiecutter: cc-python](https://img.shields.io/static/v1?label=cc-python&message=2022.01.04&color=d4aa00&logo=cookiecutter&logoColor=d4aa00)](https://github.com/python-boltons/cc-python)
[![Docker: pythonboltons/main](https://img.shields.io/static/v1?label=pythonboltons%20%2F%20main&message=2021.12.22&color=8ec4ad&logo=docker&logoColor=8ec4ad)](https://github.com/python-boltons/docker-python)


## Installation 🗹

### Using `pipx` to Install (preferred)

This package _could_ be installed using pip like any other Python package (in
fact, see the section below this one for instructions on how to do just that).
Given that we only need this package's entry points, however, we recommend that
[pipx][11] be used instead:

```shell
# install and setup pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# install sync_or_swim
pipx install sync-or-swim
```

### Using `pip` to Install

To install `sync_or_swim` using [pip][9], run the following
commands in your terminal:

``` shell
python3 -m pip install --user sync-or-swim  # install sync_or_swim
```

If you don't have pip installed, this [Python installation guide][10] can guide
you through the process.


## Command-Line Interface (CLI)

The output from running `sync_or_swim --help` is shown below:

<!-- [[[[[kooky.cog
import subprocess

popen = subprocess.Popen(["sync_or_swim", "--help"], stdout=subprocess.PIPE)
stdout, _ = popen.communicate()
print("```", stdout.decode().strip(), "```", sep="\n")
]]]]] -->
```
usage: sync_or_swim [-h] [-c CONFIG_FILE] [-L [FILE[:LEVEL][@FORMAT]]] [-v]
                    [--version]

Contains the sync_or_swim package's main entry point.

optional arguments:
  -c CONFIG_FILE, --config CONFIG_FILE
                        Absolute or relative path to a YAML file that contains
                        this application's configuration.
  -h, --help            show this help message and exit
  -L [FILE[:LEVEL][@FORMAT]], --log [FILE[:LEVEL][@FORMAT]]
                        This option can be used to enable a new logging
                        handler. FILE should be either a path to a logfile or
                        one of the following special file types: [1] 'stderr'
                        to log to standard error (enabled by default), [2]
                        'stdout' to log to standard out, [3] 'null' to disable
                        all console (e.g. stderr) handlers, or [4] '+[NAME]'
                        to choose a default logfile path (where NAME is an
                        optional basename for the logfile). LEVEL can be any
                        valid log level (i.e. one of ['CRITICAL', 'DEBUG',
                        'ERROR', 'INFO', 'TRACE', 'WARNING']) and FORMAT can
                        be any valid log format (i.e. one of ['color', 'json',
                        'nocolor']). NOTE: This option can be specified
                        multiple times and has a default argument of '+'.
  -v, --verbose         How verbose should the output be? This option can be
                        specified multiple times (e.g. -v, -vv, -vvv, ...).
  --version             show program's version number and exit
```
<!-- [[[[[end]]]]] -->

<!-- [[[[[kooky.cog
from pathlib import Path

lines = Path("./docs/design/design.md").read_text().split("\n")
if any(L.strip() for L in lines):
    fixed_lines = [L.replace("(.", "(./docs/design") if L.startswith("![") else L for L in lines]
    print("## Design Diagrams\n")
    print("\n".join(fixed_lines))
]]]]] -->
<!-- [[[[[end]]]]] -->


## Useful Links 🔗

* [API Reference][3]: A developer's reference of the API exposed by this
  project.
* [cc-python][4]: The [cookiecutter][5] that was used to generate this project.
  Changes made to this cookiecutter are periodically synced with this project
  using [cruft][12].
* [CHANGELOG.md][2]: We use this file to document all notable changes made to
  this project.
* [CONTRIBUTING.md][7]: This document contains guidelines for developers
  interested in contributing to this project.
* [Create a New Issue][13]: Create a new GitHub issue for this project.
* [Documentation][1]: This project's full documentation.


[1]: https://sync-or-swim.readthedocs.io/en/latest
[2]: https://github.com/bbugyi200/sync-or-swim/blob/master/CHANGELOG.md
[3]: https://sync-or-swim.readthedocs.io/en/latest/modules.html
[4]: https://github.com/python-boltons/cc-python
[5]: https://github.com/cookiecutter/cookiecutter
[6]: https://docs.readthedocs.io/en/stable/
[7]: https://github.com/bbugyi200/sync-or-swim/blob/master/CONTRIBUTING.md
[8]: https://github.com/bbugyi200/sync-or-swim
[9]: https://pip.pypa.io
[10]: http://docs.python-guide.org/en/latest/starting/installation/
[11]: https://github.com/pypa/pipx
[12]: https://github.com/cruft/cruft
[13]: https://github.com/bbugyi200/sync-or-swim/issues/new/choose
