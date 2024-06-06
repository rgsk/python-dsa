## To create new virtual environment run

`python -m venv {name}`

note: venv is created based on python version of terminal
so if you want to create python 3.10 based virtual env,
select anaconda environment python 3.10 and then run command `python -m venv {name}`

## Activate venv in Terminal

`source venv/bin/activate`

## Select venv interpreter in VSCode

press <kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>p</kbd> -> to select interpreter for python virtual env in vs-code

selecting venv interpreter in vscode ensures that whenever we open a new terminal in vscode, the venv is activated

## To install dependencies

install a particular package

`pip install numpy`

save dependencies listing in requirements.txt file

`pip freeze > requirements.txt`

install all dependencies from requirements.txt

`pip install -r requirements.txt`

install a particular version of package

`pip install pandas==1.1.3`
