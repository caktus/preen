import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="preen",  # without the name the package is installed as UNKNOWN
        version="dev-mode",
        packages=["preen"],
        package_dir={"": "./"},
    )