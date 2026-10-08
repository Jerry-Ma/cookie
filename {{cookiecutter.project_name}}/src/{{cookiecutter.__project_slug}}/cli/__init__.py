"""Command-line interface for {{ cookiecutter.project_name }}."""

import typer

app = typer.Typer()


@app.command()
def main() -> None:
    """Run {{ cookiecutter.project_name }}."""
    typer.echo("This is the {{ cookiecutter.project_name }} command line.")
