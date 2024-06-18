# Python CLI tools hello word demonstration

## Getting started

Clone the repository  
```git clone [code from above]``` 

cd into python-cli  
```cd python-cli```

# Create the virtual environment
```python3 -m venv venv```

# Activate it (make sure you are in the folder that contains the virtual environment you just created.)
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

# check_zephir.py
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

