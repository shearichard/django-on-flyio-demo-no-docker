# Fly.io / Django Demo

A project used to demonstrate deploying a Django app to Fly.io.

## Procedure
### Useful Resources
The process I followed in order to deploy the app is documented [here](https://fly.io/docs/django/getting-started/) but keep reading because I subsequently found fuller descriptions. 

The best documentation I found for extending the app to interact with a database is parts of this [document from learndjango](https://learndjango.com/tutorials/deploy-django-postgresql-flyio) .

I subsequently found this [Fly.io blog post](https://fly.io/blog/deploying-django-to-production/) from February 2023 which covers similar ground to the learndjango piece mentioned above. I haven't had time to read it properly but it looks good.

## Deployment Notes

### Necessary to migrate on fly.io

Although this document https://learndjango.com/tutorials/deploy-django-postgresql-flyio explains the need to create a Django `superuser` for the deployed app I haven't seen any documentation of the need to `migrate` like this ... 
```
$ fly ssh console -C 'python /code/manage.py migrate'
```

### Fly.io Command line interactions 

Fly interactions starting from scratch ...
```
$ fly launch #produce the necessary configuration files locally
$ fly deploy #move the application up to the servers of choice, start the app running
$ fly open #launch a browser window locally with the app visible in it, doesn't always work ?
```

Once the app is running then changes made to the project can be deployed with the single command ...
```
$ fly deploy 
```


## Environment
### Python Version
I found that using Python 3.8 created difficulties when deploying to the fly.io environment so I switched to 3.10

### Distutils
I find that when I tried to install 'Django' from within a 'pipenv' managed virtual environment I got an error ...

`ModuleNotFoundError: No module named 'distutils.cmd'`

... I tried to resolve this using the most popular answer from here https://stackoverflow.com/a/71977089/364088, that is ... 

`sudo apt install python3.10-distutils` . 

And that resolved the issue. 
