# Generate metrics parseable by Prometheus
def generate_metrics(config: dict, updates: dict) -> str:
    strings = [
        "# TYPE sun_package_version_info gauge",
        "# HELP sun_package_version_info Whether a package is not installed (-1), installed and updated (0), installed and updatable (1)"
    ]

    # Generate prometheus metrics
    for package in config['packages']['apt']:
        if package in updates.keys():
            strings.append(
                f'sun_package_version_info{{package="{package}", installed="{updates[package]["current"]}", latest="{updates[package]["latest"]}"}} {int(updates[package]["current"] != updates[package]["latest"])}'
            )
        else:
            strings.append(
                f'sun_package_version_info{{package="{package}", installed="", latest=""}} -1'
            )

    return '\n'.join(strings)
