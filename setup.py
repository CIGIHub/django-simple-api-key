import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-api-key',
    version='0.1.1',
    packages=['simple_api_key'],
    license='MIT License',
    description='A simple Django app to provide users api keys.',
    long_description=README,
    url='https://github.com/CIGIHub/django-simple-api-key/',
    author='Caroline Simpson',
    author_email='csimpson@cigionline.org',
    install_requires=[
        'south >= 0.8.1',
    ],
    setup_requires=[
        'south >= 0.8.1',
    ],
    requires=[
        'south (>= 0.8.1)',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)