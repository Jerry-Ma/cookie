from typer.testing import CliRunner

from {{ cookiecutter.__project_slug }}.cli import app


def test_cli() -> None:
    result = CliRunner().invoke(app)
    assert result.exit_code == 0
