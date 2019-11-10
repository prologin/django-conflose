#!/bin/bash

cd "$( dirname $0 )"

dest="../conflose/static/conflose/vendor/"
mkdir -p "$dest"

npm install

cp -r \
    node_modules/ace-builds/src-min-noconflict/ace.js \
    node_modules/ace-builds/src-min-noconflict/ext-themelist.js \
    node_modules/ace-builds/src-min-noconflict/ext-language_tools.js \
    node_modules/ace-builds/src-min-noconflict/mode-django.js \
    node_modules/ace-builds/src-min-noconflict/worker-css.js \
    "$dest"
