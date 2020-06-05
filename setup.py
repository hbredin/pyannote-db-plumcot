#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)
#
# Copyright (c) 2019 CNRS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# AUTHORS
# Hervé BREDIN - http://herve.niderb.fr/


import versioneer
from setuptools import setup, find_packages

setup(
    name='pyannote.db.plumcot',
    description="Plumcot plugin for pyannote-database",
    author='Hervé Bredin',
    author_email='bredin@limsi.fr',

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),

    scripts=[
        "scripts/characters.py",
        "scripts/episodes.py",
        "scripts/image_features.py",
        "scripts/image_scraping.py",
        "scripts/images.py",
        "scripts/multimodal.py",
        "scripts/normalizeTranscriptsNames.py",
        "scripts/transcripts.py"
    ],
    package_data={
        'Plumcot': [
            'data/*',
        ],
    },
    include_package_data=True,
    install_requires=[
        'spacy >= 2.2.4',
        'pyannote.database >= 4.0',
        'affinegap',
        'termcolor',
        'Unidecode>=1.0.23',
        'docopt>=0.6.2',
        'affinegap>=1.10',
        'scipy>=1.1.0',
        'requests>=2.18.4',
        'numpy>=1.15.4',
        'beautifulsoup4>=4.7.1',
        'lxml'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering"
    ],
    entry_points={
        "pyannote.database.databases": [
            "Plumcot = Plumcot:Plumcot",
            ],
        "pyannote.database.loader": [
            ".txt = Plumcot.loader:TxtLoader",
            ".aligned = Plumcot.loader:AlignedLoader",
            ".csv = Plumcot.loader:CsvLoader",
        ],
    },
)
