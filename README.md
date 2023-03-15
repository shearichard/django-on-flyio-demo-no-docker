# Fly.io / Django Demo

A project used to demonstrate deploying a Django app to Fly.io.


## Environment

### Python Version
I found that using Python 3.8 created difficulties when deploying to the fly.io environment so I switched to 3.10

### Distutils
I find that when I tried to install 'Django' using 'pipenv' I got an error `ModuleNotFoundError: No module named 'distutils.cmd'`. I tried to resolve this using the most popular answer from here https://stackoverflow.com/a/71977089/364088, that is `sudo apt install python3.10-distutils` .
