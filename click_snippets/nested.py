import click


@click.group()
def cli():
    """CLI interface of the program"""
    pass


@cli.result_callback()
@cli.command()
def initdb():
    """Initialize the database"""
    click.echo("Initialized the database")


@cli.command()
def dropdb():
    """Drop the database"""
    click.echo("Dropped the database")


if __name__ == "__main__":
    cli()
