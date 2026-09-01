# just-func-python

[![pull-request](https://github.com/justland/just-func-python/actions/workflows/pull-request.yml/badge.svg)](https://github.com/justland/just-func-python/actions/workflows/pull-request.yml)
[![release](https://github.com/justland/just-func-python/actions/workflows/release.yml/badge.svg)](https://github.com/justland/just-func-python/actions/workflows/release.yml)
[![PyPI](https://img.shields.io/pypi/v/just-func.svg)](https://pypi.org/project/just-func/)

Python implementation of [just-func](https://github.com/justland/just-func).

## Install

```shell
pip install just-func
```

## Develop

This project uses [uv](https://docs.astral.sh/uv/) for dependency management,
[ruff](https://docs.astral.sh/ruff/) for linting and formatting, and pytest for tests.

```shell
# install dependencies
uv sync

# run tests
uv run pytest

# lint
uv run ruff check .

# format
uv run ruff format .

# start the repl
uv run python -m justfunc
```

## Release

`release.yml` publishes to PyPI from `main` using
[trusted publishing](https://docs.pypi.org/trusted-publishers/) — no API token is stored in the
repository. To cut a release, open a PR that raises `version` in `pyproject.toml`; merging it
publishes that version and tags the commit.
