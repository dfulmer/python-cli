# Python CLI tools hello word demonstration

## Getting started

Clone the repository  
```git clone [code from above]``` 

cd into python-cli  
```cd python-cli```

# Create the virtual environment
```python3 -m venv venv```

# Activate the virtual environment (do this from within the folder that contains the virtual environment you just created.)
```source venv/bin/activate```

# Install a package
```python -m pip install [package name]```  
For example:  
```python -m pip install click```  
or:  
```python -m pip install typer```  
Or install from a requirements.txt file, if there is one:  
```python -m pip install -r requirements.txt```

# Try the hello worlds

## hello-world-click.py
This basic script defines a new command, adds an option called 'count' with a default of 1 which is the number of times the greeting will be echoed, adds another option 'name' which will become part of the greeting. There is a prompt for this second option to get the value of 'name' from the input. 'hello' is a function and is the command that will be executed.

```python hello-world-click.py```  

## hello-world-click.py with an option
An option may be supplied in the command. Here we give '3' as the value of 'count' to get 3 greetings.

```python hello-world-click.py --count=3```  

And here we supply a name.

```python hello-world-click.py --name=Sam```  


## check_zephir.py
zephir is ['1', '2', 'a']

Try:
```python check_zephir.py```  
This will ask you what you want to check in zephir and tell you if it's in zephir.

```python check_zephir.py --identifier 2```  
This allows you to specify what you want to check in the command.

```python check_zephir.py --help```  
Shows the docs.


# Deactivate the virtual environment
```deactivate```

