# README File
This setup only tested in GNU/Linux environment, for Windows replace all
instances of `python3` with `python` (not tested).

TODO: Check whether setup instruction works for Mac and Windows?

## Requirements
- Git
- Python 3.9+


## Development Environment
```bash
$ git clone https://github.com/sharedmem/platform
$ cd /path/to/project/
$ python3 -m venv --prompt . .venv # Create virtual environment.
$ source .venv/bin/activate # Activate virtual environment.
(marketplace) $ python3 -m pip install pipenv
(marketplace) $ pipenv install # Install dependencies.
```


## Run
### Database Migration
```bash
(marketplace) $ cd src
(marketplace) $ python3 manage.py makemigrations
(marketplace) $ python3 manage.py migrate
```


### Create Admin (optional)
```bash
(marketplace) $ python3 manage.py createsuperuser
```


### Start Development Server
```bash
(marketplace) $ python3 manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in browser.


# Branches
Different git branch contains different implementation of architecture patterns,
see below table for more information.

TODO: Add link to Github branch and their corresponding architecture pattern's
documentation.

| Branch | Architecture Pattern |
| :----: | :------------------: |
|  main  | [Without any pattern](./docs/patterns.md) |
|  mvt   | [Model View Template](./docs/patterns.md) (MVT) |
| service | [Service Layer](./docs/patterns.md) |
| repo | [Repository Pattern](./docs/patterns.md) (optional) |
