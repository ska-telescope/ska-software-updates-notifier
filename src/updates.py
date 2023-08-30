import apt

def get_apt_updates(config: dict) -> dict:
    # Update APT cache
    print('Updating APT cache...') 
    cache = apt.Cache()
    cache.update()
    cache.open(None)

    # Process APT packages
    upgrades = {}
    for package in [p for p in cache if p.is_installed and p.name in config['packages']['apt']]:
        current = [v.version for v in package.versions if v.is_installed][0]
        latest = package.versions[0].version
        upgrades[package.name] = {
            'current': current,
            'latest': latest
        }

    return upgrades
