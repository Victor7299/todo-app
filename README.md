# Simple Todo App

This is a simple Todo app made in python using Flask
For styling I used Tailwind
For interactivity I used HTMX

## Run it

This is a very simple proyect (for now) so the foler structure is a mess, for running this you have to:
```bash
# Use a virtulenv
python -m venv venv
source venv/bin/activate 
python -m pip install -r requirements.txt
```
And then you can run the server:

```bash
# if you are using linux/mac
export FLASK_APP=main.py
export FLASK_ENV=development #or production
flask run
```
or 
```bash
# if you are using windows - CMD
set FLASK_APP=main.py
set FLASK_ENV=development #or production
flask run
```