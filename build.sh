#!/bin/bash

source /home/rafaph/.pyenv/versions/swx/bin/activate
rm -rf dist swx_generator.egg-info
python setup.py sdist --formats=gztar
deactivate