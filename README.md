# EB Docker Deploy

## Requirments

### Secrets

#### '.secrets/base.json'

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```


## Running

```
# Move projects.directory

pipenv install
pipenv shell
cd app
export DJANGO_SETTINGS_MODULE=config.settings.local
./manage.py runserver
```