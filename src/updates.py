"""Handles the APT cache updates"""
import apt

CACHE = apt.Cache()


def get_apt_updates(config: dict) -> dict:
    """Updates the APT cache and retuns the data of the desired packages"""
    # Update APT cache
    print("Updating APT cache...")
    CACHE.update()
    CACHE.open(None)

    # Process APT packages
    upgrades = {}
    for package in [
        p
        for p in CACHE
        if p.is_installed and p.name in config["packages"]["apt"]
    ]:
        current = [v.version for v in package.versions if v.is_installed][0]
        latest = package.versions[0].version
        upgrades[package.name] = {"current": current, "latest": latest}

    return upgrades
