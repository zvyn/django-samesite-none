Middleware to work around [#30862](https://code.djangoproject.com/ticket/30862)

Chrome started rolling out changes that brake Django sites with intentionally
empty `SameSite` cookie settings.

This middleware sets the value `"None"` on those cookies explicitly.
Also sets `Secure` to `True` for all altered cookies.

# Installation

Get it from PyPi:

```bash
pip install django-samesite-none
```

Put it first in the `MIDDLEWARE` list in your `settings.py`:

```
MIDDLEWARE = [
    "django_samesite_none.middleware.SameSiteNoneMiddleware",
    ...
]
```
