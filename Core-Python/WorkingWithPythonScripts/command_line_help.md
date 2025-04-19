# Python Script Execution Commands

This comprehensive guide covers essential command line commands for executing Python scripts, managing environments, and debugging.

## Table of Contents
- [Basic Shell Navigation](#basic-shell-navigation)
- [Basic Execution](#basic-execution)
- [Passing Arguments](#passing-arguments)
- [Running Scripts in Different Ways](#running-scripts-in-different-ways)
- [Debugging and Development](#debugging-and-development)
- [Virtual Environment Management](#virtual-environment-commands)
- [Package Management](#package-management)
- [Common Options](#common-options)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Basic Shell Navigation

```bash
# List directory contents
ls

# List directory contents with details
ls -l

# List all files including hidden ones
ls -a

# Change directory
cd /path/to/directory

# Go back one directory level
cd ..

# Go to home directory
cd ~
cd

# Go to previous directory
cd -

# Clear the terminal screen
clear

# Print working directory (show current location)
pwd

# Create a new directory
mkdir directory_name

# Remove a directory
rmdir directory_name

# Remove a directory and its contents
rm -r directory_name

# Create a new file
touch filename

# Copy a file
cp source_file destination_file

# Move or rename a file
mv old_name new_name

# Remove a file
rm filename

# View file contents
cat filename

# View file contents page by page
less filename

# Search for files
find . -name "pattern"

# Search for text in files
grep "pattern" filename
```

## Basic Execution

```bash
# Execute a Python script
python script.py

# Execute a Python script with Python 3 explicitly
python3 script.py

# Execute a Python script with a specific Python version
python3.9 script.py

# Execute a script with output redirection
python script.py > output.txt

# Execute a script and pipe output to another command
python script.py | grep "pattern"
```

## Passing Arguments

```bash
# Execute a script with positional arguments
python script.py arg1 arg2 arg3

# Execute a script with named arguments
python script.py --name John --age 25

# Execute a script with boolean flags
python script.py --verbose --debug

# Access arguments in your script:
# import sys
# print(sys.argv)  # List of all arguments
```

## Running Scripts in Different Ways

```bash
# Run a script as a module
python -m script

# Run a script with a specific working directory
cd /path/to/directory && python script.py

# Run a script with environment variables
PYTHONPATH=/path/to/modules python script.py

# Run a script with specific Python options
PYTHONOPTIMIZE=1 python script.py

# Run a script with custom Python path
PYTHONPATH=/custom/path python script.py
```

## Debugging and Development

```bash
# Run a script in debug mode
python -m pdb script.py

# Run a script with verbose output
python -v script.py

# Run a script with warnings enabled
python -W all script.py

# Run a script with memory profiling
python -m memory_profiler script.py

# Run a script with line-by-line profiling
python -m cProfile script.py

# Run a script with time profiling
python -m timeit "import script; script.main()"
```

## Virtual Environment Commands

```bash
# Create a virtual environment
python -m venv myenv

# Create a virtual environment with specific Python version
python3.9 -m venv myenv

# Activate virtual environment (Linux/Mac)
source myenv/bin/activate

# Activate virtual environment (Windows)
myenv\Scripts\activate

# Deactivate virtual environment
deactivate

# List installed packages in virtual environment
pip list

# Freeze requirements
pip freeze > requirements.txt

# Create virtual environment with system site packages
python -m venv --system-site-packages myenv
```

## Package Management

```bash
# Install required packages
pip install -r requirements.txt

# Install a specific package
pip install package_name

# Install a specific version
pip install package_name==1.2.3

# Install a package in development mode
pip install -e .

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Check for outdated packages
pip list --outdated

# Install packages with specific index
pip install -i https://pypi.org/simple package_name
```

## Common Options

- `-c`: Execute a command
- `-m`: Run a module as a script
- `-i`: Interactive mode after running script
- `-v`: Verbose output
- `-W`: Warning control
- `-O`: Optimize mode
- `-B`: Don't write .pyc files
- `-u`: Unbuffered binary stdout and stderr
- `-E`: Ignore PYTHON* environment variables
- `-S`: Don't imply 'import site' on initialization

## Best Practices

1. Always use virtual environments for project isolation
2. Use `requirements.txt` for dependency management
3. Use absolute paths when running scripts from different directories
4. Consider using shebang (`#!/usr/bin/env python3`) for executable scripts
5. Document command line arguments in your script's help text
6. Use type hints and docstrings for better code documentation
7. Implement proper error handling and logging
8. Use configuration files for complex settings
9. Follow PEP 8 style guide for Python code
10. Use version control for your scripts

## Troubleshooting

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check installed packages
pip list

# Check Python path
python -c "import sys; print(sys.path)"

# Check environment variables
env | grep PYTHON

# Clear pip cache
pip cache purge

# Fix broken pip installation
python -m pip install --upgrade pip

# Check for syntax errors
python -m py_compile script.py

# Check for style issues
python -m pycodestyle script.py
```

## Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environment Documentation](https://docs.python.org/3/library/venv.html)
- [Python Debugger Documentation](https://docs.python.org/3/library/pdb.html) 