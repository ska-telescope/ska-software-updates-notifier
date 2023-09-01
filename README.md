# Software Updates Notifier

This tool allows to setup a Prometheus metrics server that notifies when specified APT packages are outdated.

## Installation

Simply run `make install` to install and run the server on the machine. All dependencies will be installed as well.

Once installed, the APT package metrics will be available on the usual `/metrics` endpoint.

## Configuration

This tool is configured using a simple YAML file, a [sample](files/config.yaml.sample) of which is provided in this repository.

It allows to specify the port in which the HTTP server will listen on, as well as the list of APT packages to monitor.

To use your own configuration file, a `config.yaml` file may be created in the [files](files) folder, which a `make install` or `make reconfigure` will copy over to the correct location.

Alternatively, a `config.yaml` file may be placed directly in the `/root/.config/sun` folder.

## Uninstallation

Simply run `make uninstall` to install and run the server on the machine.
