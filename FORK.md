# Fork notes

A fork of
[scientific-python/cookie](https://github.com/scientific-python/cookie) with our
opinions applied. It generates one kind of project: a pure-Python package built
with setuptools, versioned from git tags, BSD licensed, documented with Sphinx
and hosted on GitHub.

## What you get

| Topic              | cookie                             | This fork                              |
| ------------------ | ---------------------------------- | -------------------------------------- |
| Task runner        | nox                                | `just`                                 |
| Type checker       | mypy                               | ty                                     |
| Lint rules         | About thirty ruff rule families    | Every ruff rule                        |
| Commit gate        | Installed by hand                  | Tracked hook, activated by `install`   |
| Guideline check    | Not in the project                 | `sp-repo-review` hook                  |
| Hygiene hooks      | cookie's list                      | Plus the ones Astropy runs             |
| Docstring check    | None                               | ruff's rules and numpydoc validation   |
| Doctests           | None                               | pytest-doctestplus and Sphinx doctest  |
| Sphinx setup       | Hand-written, napoleon, furo       | Astropy defaults, numpydoc, book theme |
| Docs build         | Unresolved references are warnings | Any warning fails                      |
| Docs hosting       | Read the Docs                      | GitHub Pages                           |
| Docs icon          | None                               | Required; a placeholder is supplied    |
| Python             | 3.11 and newer                     | 3.14 and newer                         |
| Version bounds     | Loose minimums                     | Latest major.minor                     |
| Starting code      | An example class                   | A Typer command                        |
| Pydantic and Typer | No support                         | Docs and lint support                  |
| Dependency updates | Dependabot for GitHub Actions      | Dependabot for uv and the hooks        |
| CI                 | GitHub workflows                   | None                                   |

## Create a project

The fork works through [copier](https://copier.readthedocs.io) only.

```bash
uvx --with copier-templates-extensions copier copy --trust \
  gh:Jerry-Ma/cookie <project-dir>
```

copier asks for the project name, the GitHub organisation or user, your name,
your email and a one-line description. Everything else is fixed.

Then, inside the project:

```bash
git init -b main && git add -A && git commit -m "Initial commit"
just install
```

Replace the placeholder icon `docs/_static/favicon.ico` with the project's own.

## Work in a project

| Recipe            | What it does                                        |
| ----------------- | --------------------------------------------------- |
| `just install`    | create or update the environment, activate the hook |
| `just qa`         | the hooks on all files, the tests, the doc examples |
| `just test`       | pytest, with arguments passed through               |
| `just coverage`   | the tests, with a coverage report                   |
| `just doc-build`  | build the docs; any warning fails                   |
| `just doc-test`   | run the `testcode` examples in the docs             |
| `just doc`        | serve the docs with live reload                     |
| `just doc-deploy` | build the docs and publish them to GitHub Pages     |
| `just build`      | build the sdist and wheel                           |
| `just clean`      | remove what the recipes generate                    |

## Update a project

```bash
uvx --with copier-templates-extensions copier update --trust
```
