"""
Flask-HTTPAuth
--------------

Basic and Digest HTTP authentication for Flask routes.
"""
from setuptools import setup


setup(
    name='Flask-HTTPAuth',
    version='2.3.1',
    url='http://github.com/miguelgrinberg/flask-httpauth/',
    license='MIT',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='Basic and Digest HTTP authentication for Flask routes',
    long_description=__doc__,
    py_modules=['flask_httpauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite = "test_httpauth",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
