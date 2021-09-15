# About

This module implements Textalytics (https://textalytics.io) interface core capabilities for open-source NLP libraries.

Support for Spacy (https://spacy.io/usage/linguistic-features#named-entities) and Stanform NLP Stanza (https://github.com/stanfordnlp/stanza/) is currently implemented.

Textalytics build and delivers custom NLP models for NER and entity-resolution for different domains. 
Further Textalytics caters to the needs of organizations that have a need to deploy these models in an air-gappend 
environemnt where no data can go out of internal network.

# PyPi package

This module is availabe in pypi

Usage:

`pip install textalytics-oss-adapters`

# Local development

You will need Python 3.9+ installed.

## Mac M1

Stanza and Spacy have dependencies that don't yet work with pip based dependency management. 

Use conda for the same

### Conda

First install conda and then create a new virtual environment

`conda create -p conda-venv python`

Activate environment

`conda activate ./conda-venv`

Now install dependencies

First for textalytics-core, which is in pypi and not in conda-forge:

`pip install -r pip-requirements.txt`

Now spacy and stanza:

`conda install --file conda-requirements.txt -c conda-forge`

## Other architectures and OS

Using `poetry` to manage dependencies should work. Else switch to conda.

`poetry` can be installed with `brew` on a Mac.

* Get latest code from github
* Create a virtual environment

`python -m venv venv`

* Initialize poetry and install dependencies

`poetry init`

`poetry install`

## Spacy downloading model

`python -m spacy download en_core_web_sm`

## Build 

* At this point you will be able to build

`poetry build`

* Tests can be run with 

`poetry run test`