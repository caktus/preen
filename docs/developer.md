# Developing Preen

## Dependencies
* Poetry >= 1.1
* Python >= 3.6
* Pytest >= 7.0

## pyproject.toml
# You will need to add these settings to the generated pyproject.toml file
```
[tool.poetry]
name = "preen"
version = "0.1.0"
description = "Description of your package"
authors = ["Yourname <yourname@gmail.com>"]
keywords = ["keyword", "another_keyword"]
readme = "README.md"
license = "MIT"
homepage = "https://yourdomain.com/username/package_name"
repository = "https://github.com/username/package_name"
include = [
    "LICENSE",
]

[tool.poetry.dependencies]
python = "^3.5"

[tool.poetry.dev-dependencies]

[tool.poetry.scripts]
cli_command_name = 'package_name:function'

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

# Deploying
1. Create or login to your account on [PyPI](https://pypi.org/) and the [PyPI test](https://test.pypi.org/)
2. For security reasons it is strongly recommended to create an [API token](https://pypi.org/help/#apitoken) instead of using your username and password when uploading a package to PyPI. If you haven’t done so, create an API token on both PyPI and the PyPI test server.
3. Store your API tokens for authentication on your .envrc file, 
```
username = __token__
password = pypi-AgEIcH...
``` 
**Note**: replace the password with your API token
1. Ensure that Twine is installed - `pip install --upgrade twine`
2. poetry config repositories.testpypi https://test.pypi.org/legacy/
3. poetry publish –-build -r testpypi
4. poetry config pypi-token.testpypi <API Token>

