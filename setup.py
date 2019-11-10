import os.path
from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name="django-conflose",
    version='0.5',
    author="Association Prologin",
    author_email="info@prologin.org",
    license="GPL3",
    packages=find_namespace_packages(include=['conflose', 'conflose.*']),
    include_package_data=True,
    description=(
        """A Django app to "customize" the CSS of your most annoying users."""
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "django>=2.1",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    project_urls={
        'Source': 'https://github.com/prologin/django-conflose/',
        'Issue Tracker': 'https://github.com/prologin/django-conflose/issues',
    },
)
