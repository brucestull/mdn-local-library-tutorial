# Django Tutorial Part 8: User authentication and permissions

* <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication>

## New Concepts

```python
INSTALLED_APPS = [
    # …
    # Core authentication framework and its default models.
    'django.contrib.auth',
    # Django content type system (allows permissions to be associated with models).
    'django.contrib.contenttypes',
    # …

MIDDLEWARE = [
    # …
    # Manages sessions across requests
    'django.contrib.sessions.middleware.SessionMiddleware',
    # …
    # Associates users with requests using sessions.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # …
]
```

* Current position in tutorial:
  * <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#challenge_yourself>

## Links

* <http://localhost:8000/catalog/>
* <http://localhost:8000/accounts/login/>
* <http://localhost:8000/accounts/logout/>
