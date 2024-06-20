import typer
from zipfile import ZipFile
import glob
import time
import os

app = typer.Typer()

@app.command()
def createfiles(number: int):
    """
    Create some files
    """
    for i in range (1, number +1):
          filename = f"file_{i}.txt"
          with open(filename, "w") as file:
               file.write(f"This is content for {filename}\n")
          print(f"Created {filename}")

@app.command()
def zip(filename: str):
    """
    Zip all files with .txt file extensions in the current directory
    """
    files = glob.glob("*.txt")
    with ZipFile(filename + ".zip", "w") as zip_object:
        with typer.progressbar(files) as progress:
                for file in progress:
                      zip_object.write(file)
                      #os.remove(file)
                      time.sleep(1)
    zip_object.close()
    print(f"Zipped {files} in {filename}.zip.")

if __name__ == "__main__":
    app()

# Try
# Create some files:
# python zip_and_move_to_pickup.py createfiles 3

# Zip .txt files:
# python zip_and_move_to_pickup.py zip zippedfiles1

# Help:
# python zip_and_move_to_pickup.py --help

# Specific help:
# python zip_and_move_to_pickup.py zip --help
