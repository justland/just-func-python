# Contributing

## Setup

The project uses [uv](https://docs.astral.sh/uv/). Everything else comes from the lockfile.

```shell
uv sync
```

## Verify

CI runs these three commands on Python 3.10 and 3.14 across Linux, macOS and Windows. Run them
before pushing and the pull request will not tell you anything you did not already know.

```shell
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

`uv run ruff format .` rewrites the files rather than reporting on them.

## Pull requests

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/). The default
branch is protected: `code / all-checks` must pass, and merges go through a merge queue that
rebuilds each pull request against the real base before landing it. Use `gh pr merge --auto` and
let the queue take it from there.

Adding a dependency also means committing the updated `uv.lock`, because CI installs with
`uv sync --locked` and will fail on a stale one.

## Releases

A release is a pull request that raises `version` in `pyproject.toml`. When it merges,
`release.yml` compares that version against PyPI, and publishes if it is new. Nothing else
publishes, so a merge that leaves the version alone ships nothing.

Publishing uses [trusted publishing](https://docs.pypi.org/trusted-publishers/) — GitHub's OIDC
token, no stored PyPI credentials.
