# README File
This README file is best readable in [markdown
previewer](https://www.digitalocean.com/community/markdown).

## Requirements
- [Python](https://www.python.org/downloads/) 3.9+


## Setup Environment
This setup only tested in GNU/Linux environment. In Windows replacing all
instances of `python3` with `python` may work (not tested).

```bash
$ cd /path/to/project/pattern
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
