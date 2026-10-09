# {{ cookiecutter.project_name }}

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
{%- if cookiecutter.org | lower == "scikit-hep" %}
[![Scikit-HEP][sk-badge]](https://scikit-hep.org/) {%- endif %}

{%- if cookiecutter.docs == "sphinx" %}

<!-- SPHINX-START -->
{%- endif %}

<!-- prettier-ignore-start -->
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  {{cookiecutter.url}}/discussions
{%- if cookiecutter.org | lower == "scikit-hep" %}
[sk-badge]:                 https://scikit-hep.org/assets/images/Scikit--HEP-Project-blue.svg
{%- endif %}

<!-- prettier-ignore-end -->
