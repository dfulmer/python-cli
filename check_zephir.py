import click

zephir = ['1', '2', 'a']

@click.command()
@click.option('--identifier', prompt='What do you want to check in zephir?', help='What you want to check in zephir')

def check_zephir(identifier):
    if identifier in zephir:
        click.echo(f"{identifier} That's in zephir.")
    else:
        click.echo(f"{identifier} That's not in zephir.")
    
if __name__ == '__main__':
    check_zephir()

# Try:
# python check_zephir.py
# python check_zephir.py --identifier 2
# python check_zephir.py --help