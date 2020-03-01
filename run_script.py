#!/usr/bin/env python3

# initialize django
from api.models import Category
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
django.setup()

# regular imports

# main script


def main():
    for cat in Category.objects.all():
        print(cat.id, cat.title)


# bootstrap
if __name__ == '__main__':
    main()
