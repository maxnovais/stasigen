#!/bin/bash
rm -fr build
python sitebuilder.py build
python -m SimpleHTTPServer 8888 build

