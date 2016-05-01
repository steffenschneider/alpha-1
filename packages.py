import pip


def main():
    installed_packages = pip.get_installed_distributions()
    flat_installed_packages = [package.project_name for package in installed_packages]
    print(sorted(flat_installed_packages, key=str.lower))  # print installed python packages
    if 'requests' in flat_installed_packages:
        print("requests module available")


if __name__ == "__main__":
    main()
