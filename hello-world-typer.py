# https://typer.tiangolo.com/
# Different examples from the getting started document are separatted by: ###

# def main(name: str):
#     print(f"Hello {name}")

# Try
# typer hello-world-typer.py run
# typer hello-world-typer.py run --help
# typer hello-world-typer.py run Camila

###

# import typer

# def main(name: str):
#     print(f"Hello {name}")

# if __name__ == "__main__":
#     typer.run(main)

# Try
# python hello-world-typer.py
# python hello-world-typer.py --help
# python hello-world-typer.py Camila

###

import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

if __name__ == "__main__":
    app()

# Try
# python hello-world-typer.py --help
# python hello-world-typer.py hello Camila
# python hello-world-typer.py goodbye Camila
# python hello-world-typer.py goodbye --formal Camila