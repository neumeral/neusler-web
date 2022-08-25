bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)
red := $(shell tput setaf 1)
green := $(shell tput setaf 2)

.ONESHELL:

prep:
	pip install --upgrade pip wheel setuptools pip-tools
