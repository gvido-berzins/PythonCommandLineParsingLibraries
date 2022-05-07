import codecs

import click


@click.command()
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def encode(password):
    """Password prompt with hidden input and confirmation"""
    click.echo(f"encoded: {codecs.encode(password, 'rot13')}")


if __name__ == "__main__":
    encode()
