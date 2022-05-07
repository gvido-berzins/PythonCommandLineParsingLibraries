import click


@click.command()
def hello():
    """Echo 'Hello World!'. Supports different terminals wth echo"""
    click.echo("Hello World!")


if __name__ == "__main__":
    hello()
