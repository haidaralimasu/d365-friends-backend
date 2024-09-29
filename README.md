# D365 Friends Backend

This repo contains all models related to d365friends.com

## Project Status

D365 Friends project is active and maintenance by D365 Friends

## Quickstart

**Requirements**

- python v3.12.+

**Clone the repo**

clone the repo

**Setup env file**

```sh
cp .env.development .env
```

or

```sh
cp .env.production .env
```

**Create a virtualenv**

```sh
python3 -m venv venv
```

**Install all dependencies**

```sh
pip3 install -r requirements.txt
```

**Setup enviorment variables in** `.env`

```sh
DJANGO_SECRET_KEY="ABC"
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS="*"
DJANGO_DB_NAME="postgres"
DJANGO_DB_USER="postgres"
DJANGO_DB_PORT="5432"
DJANGO_DB_PASSWORD="ABCD"
DJANGO_DB_HOST="localhost"
DJANGO_CSRF_TRUSTED_ORIGINS="*"
```

**Format code**

```sh
sh scripts/lint.sh
```

**Run locally**

```sh
python3 manage.py runserver
```

## Architecture

See the [Architecture](docs/architecture.png) file for more info.

## License

D365 Friends Backend repo is available under the GNU license. See the [LICENSE](LICENSE) file for more info.
