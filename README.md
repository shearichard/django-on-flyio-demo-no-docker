# Fly.io / Django Demo

A project used to demonstrate deploying a Django app to Fly.io.

## Procedure
The process I followed in order to deploy the app is documented here https://fly.io/docs/django/getting-started/ . 

## Environment
### Python Version
I found that using Python 3.8 created difficulties when deploying to the fly.io environment so I switched to 3.10

### Distutils
I find that when I tried to install 'Django' from within a 'pipenv' managed virtual environment I got an error ...

`ModuleNotFoundError: No module named 'distutils.cmd'`

... I tried to resolve this using the most popular answer from here https://stackoverflow.com/a/71977089/364088, that is ... 

`sudo apt install python3.10-distutils` . 

And that resolved the issue. 
