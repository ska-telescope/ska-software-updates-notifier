INSTALL_DIR=/root/.local/share/sun
CONFIG_DIR=/root/.config/sun
SYSTEMD_DIR=/etc/systemd/system

include .make/base.mk
include .make/python.mk

python-pre-lint:
	apt-get update -y
	apt-get install python3-apt python3-venv python3-pip -y

install-dependencies:
	sudo mkdir -p $(CONFIG_DIR)
	sudo mkdir -p $(INSTALL_DIR)
	sudo apt-get install python3-apt python3-venv python3-pip -y
	poetry config --local virtualenvs.options.system-site-packages true
	poetry config --local virtualenvs.in-project true
	poetry install
	sudo cp -r .venv $(INSTALL_DIR)/venv

start:
	sudo systemctl start sun.service

stop:
	sudo systemctl stop sun.service

restart:
	sudo systemctl restart sun.service

reconfigure:
	sudo cp files/config.yaml $(CONFIG_DIR)
	sudo systemctl restart sun.service

install: install-dependencies
	sudo cp src/*.py $(INSTALL_DIR)
	sudo cp files/sun.service $(SYSTEMD_DIR)/sun.service
	sudo cp files/config.yaml $(CONFIG_DIR) | true
	sudo systemctl start sun.service
	sudo systemctl enable sun.service

uninstall:
	sudo systemctl disable sun.service
	sudo systemctl stop sun.service
	sudo rm -rf $(SYSTEMD_DIR)/sun.service
	sudo rm -rf $(INSTALL_DIR)
	sudo rm -rf $(CONFIG_DIR)

update:
	git pull
	sudo cp src/*.py $(INSTALL_DIR)
	sudo systemctl restart sun.service
