<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-timesince-shortener.svg?maxAge=3600)](https://pypi.org/project/django-timesince-shortener/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-timesince-shortener.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-timesince-shortener.py/actions)

### Installation
```bash
$ [sudo] pip install django-timesince-shortener
```

#### Examples
```html
{% load timesince_shortener %}

{{ item.created_at|timesince_shortener }} ago
```

`timesince`|`timesince_shortener`
-|-
`1 hour 5 minutes ago`|`1 hour ago`
`1 year 2 months ago`|`1 year ago`

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>