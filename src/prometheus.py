"""Handles the generation of the Prometheus metrics"""


# pylint: disable=line-too-long
def generate_metrics(config: dict, updates: dict) -> str:
    """Generates Prometheus metrics for the provided APT packages"""
    strings = [
        "# TYPE sun_package_version_info gauge",
        "# HELP sun_package_version_info Whether a package is not installed (-1), installed and updated (0), installed and updatable (1)",  # NOQA: E501
    ]

    # Generate prometheus metrics
    for package in config["packages"]["apt"]:
        if package in updates.keys():
            strings.append(
                f'sun_package_version_info{{package="{package}", installed="{updates[package]["current"]}", latest="{updates[package]["latest"]}"}} {int(updates[package]["current"] != updates[package]["latest"])}'  # NOQA: E501
            )
        else:
            strings.append(
                f'sun_package_version_info{{package="{package}", installed="", latest=""}} -1'  # NOQA: E501
            )

    return "\n".join(strings) + "\n"
