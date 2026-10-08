# {{ cookiecutter.project_name }}

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
{%- if cookiecutter.org | lower == "scikit-hep" %}
[![Scikit-HEP][sk-badge]](https://scikit-hep.org/) {%- endif %}

{%- if cookiecutter.docs == "sphinx" %}

<!-- SPHINX-START -->
{%- endif %}

<!-- prettier-ignore-start -->
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_name}}
[conda-link]:               https://github.com/conda-forge/{{cookiecutter.project_name}}-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  {{cookiecutter.url}}/discussions
[pypi-link]:                https://pypi.org/project/{{cookiecutter.project_name}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}
[pypi-version]:             https://img.shields.io/pypi/v/{{cookiecutter.project_name}}
{%- if cookiecutter.org | lower == "scikit-hep" %}
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
{%- endif %}

<!-- prettier-ignore-end -->
