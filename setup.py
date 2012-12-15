import os
from setuptools import setup, find_packages

import skrill


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-skrill',
    version=skrill.__version__,
    description='A reuseable Django application for integrating the Skrill (Moneybookers) payment API',
    long_description=read('README.md'),
    license=read('LICENSE'),
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-skrill',
    packages=find_packages(),
    install_requires=[
        'django',
        'django-multiselectfield',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
        'factory_boy',
    ],
    test_suite='skrill.tests',
)
