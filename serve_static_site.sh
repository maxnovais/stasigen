#!/bin/bash
rm -fr build
python sitebuilder.py build
cd build && python -m SimpleHTTPServer 8888

