<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-timesince-shortener.svg?longCache=True)](https://pypi.org/project/django-timesince-shortener/)
[![](https://img.shields.io/pypi/v/django-timesince-shortener.svg?maxAge=3600)](https://pypi.org/project/django-timesince-shortener/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-timesince-shortener.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-timesince-shortener.py/)

#### Installation
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
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>