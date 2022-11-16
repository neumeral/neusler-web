bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
red := $(shell tput setaf 1)
green := $(shell tput setaf 2)

.ONESHELL:

prep:
	pip install --upgrade pip wheel setuptools pip-tools
	npm i minify -g

bundle-css:
	minify website/static/css/vars.css > website/static/css/vars.min.css
	cat website/static/css/vars.min.css website/static/css/style.css website/static/css/colors/green.css > website/static/css/bundle.css

bundle-js:
	minify website/static/js/extras.js > website/static/js/extras.min.js 
	cat website/static/js/plugins.js website/static/js/theme.js website/static/js/extras.min.js > website/static/js/bundle.js 