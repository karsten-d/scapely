ifdef CI
	VENV=
	VENV_BIN=
else
	VENV=virtualenv venv
	VENV_BIN=venv/bin/
endif

.make/timestamp:
	mkdir .make
	touch $@

.make/venv.timestamp: .make/timestamp
	$(VENV)
	touch $@

.make/requirements.timestamp: .make/venv.timestamp requirements.txt
	$(VENV_BIN)pip install -r requirements.txt
	touch $@

.PHONY: install
install: .make/requirements.timestamp

.PHONY: test
test: .make/requirements.timestamp
	@echo "No tests defined until now..."

.PHONY: clean
clean:
	rm -rf venv
	rm -rf .make
