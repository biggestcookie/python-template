# python-template

A barebones template for starting Python 3 projects.

## Requirements

[Python 3.8+](https://www.python.org/downloads/)

## Usage

0. (Optional) Consider using a virtual environment manager such as [pipx](https://pypa.github.io/pipx/) or [venv](https://docs.python.org/3/library/venv.html).
   - pipx is the modern recommendation but requires installation
   - For venv which is built-in, simply run 'Python: Create environment' if you are using Visual Studio Code, or `python -m venv .venv` from the terminal. You may need to reload your IDE after running this if you are using one.
1. Install dependencies with `pip install -r requirements.txt`.
2. Run the project by selecting 'Terminal' > 'Run task' > 'python: app.py' if using Visual Studio Code, or `python main.py` in the terminal.
3. (Optional) A VSCode debug profile is also provided, you can use this to run or debug the program. [See the VSCode docs for more info.](https://code.visualstudio.com/docs/python/debugging#_basic-debugging)
