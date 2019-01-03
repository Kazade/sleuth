import os
from setuptools import setup

NAME = 'sleuth-mock'
MODULES = ['sleuth']
DESCRIPTION = 'A minimal Python mocking library'
URL = "https://github.com/kazade/sleuth"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
AUTHOR = 'Luke Benstead'
AUTHOR_EMAIL = 'kazade@gmail.com'

setup(
    name=NAME,
    version='0.1',
    py_modules=MODULES,
    # metadata for upload to PyPI
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=(
        "python", "mock", "testing", "test",
        "unittest", "monkeypatch", "patch", "stub"
    ),
    url=URL
)
