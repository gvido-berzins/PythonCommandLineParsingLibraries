import click


@click.command()
@click.option("--count", default=1, help="number of greetings")
@click.argument("name")
def hello(count, name):
    for x in range(count):
        click.echo(f"{x:>2}. Hello {name}!")


if __name__ == "__main__":
    hello()
