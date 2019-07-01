#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from m2r import parse_from_file
from setuptools import setup, find_packages

{% set djversions = cookiecutter.django_versions.split(',') -%}
{%- set pyversions = cookiecutter.python_versions.split(',') -%}
{%- set license_classifiers = {
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'BSD': 'License :: OSI Approved :: BSD License',
    'ISCL': 'License :: OSI Approved :: ISC License (ISCL)',
    'MIT': 'License :: OSI Approved :: MIT License',
} -%}

def get_version(*file_paths):
    """Retrieves the version from {{ cookiecutter.app_name }}/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def parse_reqs(filepath):
    with open(filepath, 'r') as f:
        reqstr = f.read()
    requirements = []
    for line in reqstr.splitlines():
        line = line.strip()
        if line == '':
            continue
        elif not line or line.startswith('#'):
            # comments are lines that start with # only
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            _, new_filename = line.split()
            new_file_path = os.path.join(os.path.dirname(filepath or '.'),
                                         new_filename)
            requirements.extend(parse_reqs(new_file_path))
        elif line.startswith('-f') or line.startswith('--find-links') or \
                line.startswith('-i') or line.startswith('--index-url') or \
                line.startswith('--extra-index-url') or \
                line.startswith('--no-index'):
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            continue
        else:
            requirements.append(line)
    return requirements

version = get_version("{{ cookiecutter.app_name }}", "__init__.py")
readme = open('README.rst').read()
history = parse_from_file('CHANGELOG.md')

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=['example*', 'tests*', 'docs', 'build', ]),
    include_package_data=True,
    install_requires=parse_reqs('requirements.txt'),
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 3 - Alpha',{% for djver in djversions %}
        'Framework :: Django :: {{ djver }}',{% endfor %}
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',{% for pyver in pyversions %}
        'Programming Language :: Python :: {{ pyver }}',{% endfor %}
    ],
)
