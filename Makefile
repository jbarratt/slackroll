PHONY: build

build:
	mv ~/.pydistutils.cfg.bak ~/.pydistutils.cfg
	gordon build
	mv ~/.pydistutils.cfg ~/.pydistutils.cfg.bak
