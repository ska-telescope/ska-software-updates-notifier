INSTALL_DIR=/root/.local/share/sun
CONFIG_DIR=/root/.config/sun
SYSTEMD_DIR=/etc/systemd/system

install-dependencies:
	@sudo apt-get install python3-apt -y
	@sudo pip3 install -r requirements.txt

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
	sudo mkdir -p $(CONFIG_DIR)
	sudo mkdir -p $(INSTALL_DIR)
	sudo cp src/*.py $(INSTALL_DIR)
	sudo cp files/sun.service $(SYSTEMD_DIR)
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
