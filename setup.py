# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from aldryn_django_cms import __version__

setup(
    name="aldryn-django-cms",
    version=__version__,
    description='An opinionated django CMS setup bundled as an Aldryn Addon',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-django-cms',
    packages=find_packages(),
    install_requires=(
        'aldryn-addons',
        'django-cms==3.4.2',
        'requests',

        # NOTE: django-cms doesn't require this, but many of the addons do.
        #       If it is used, however, then it must be >=1.0.9 for CMS 3.3+.
        'aldryn-reversion>=1.0.9',
        'django-treebeard>=4.0.1',         # django-cms
        'djangocms-admin-style>=1.2.0',    # django-cms
        'django-select2>=4.3,<5.0',

        # Other common
        # ------------
        # TODO: mostly to be split out into other packages
        'aldryn-boilerplates>=0.7.4',
        'aldryn-snake',
        'django-compressor',
        # Django Parler 1.6.3 has a few known issues with ckeditor.
        'django-parler<=1.6.2',
        # Django Sortedm2m 1.3 introduced a regression, that was fixed in 1.3.2
        # See https://github.com/gregmuellegger/django-sortedm2m/issues/80
        'django-sortedm2m>=1.2.2,!=1.3.0,!=1.3.1',
        'django-robots',
        'django-simple-captcha',
        'lxml',
        'YURL',
    ),
    include_package_data=True,
    zip_safe=False,
)
