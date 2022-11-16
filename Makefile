bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
red := $(shell tput setaf 1)
green := $(shell tput setaf 2)

.ONESHELL:

prep:
	pip install --upgrade pip wheel setuptools pip-tools
	npm i minify purgecss -g

generate-site:
	. ./gen.sh

bundle-css:
	minify website/static/css/vars.css > website/static/css/vars.min.css
	cat website/static/css/vars.min.css website/static/css/style.css website/static/css/colors/green.css > website/static/css/bundle.css

bundle-js:
	minify website/static/js/extras.js > website/static/js/extras.min.js 
	cat website/static/js/plugins.js website/static/js/theme.js website/static/js/extras.min.js > website/static/js/bundle.js 

purge-css:
	mkdir -p _site/static/cssmin
	purgecss -css _site/static/css/vars.css _site/static/css/style.css _site/static/css/colors/green.css \
		-con _site/index.html _site/product/index.html _site/product/automate/index.html \
		_site/product/engage/index.html _site/product/publishing/index.html \
		_site/pricing/index.html _site/contact/index.html _site/drops/index.html \
		_site/static/js/bundle.js _site/static/js/bootstrap.bundle.min.js \
		-o _site/static/cssmin
	cat _site/static/cssmin/vars.css  _site/static/cssmin/style.css _site/static/cssmin/green.css  > _site/static/cssmin/bundle.css
	cp  _site/static/cssmin/bundle.css _site/static/css/bundle.css

release: bundle-js generate-site purge-css
