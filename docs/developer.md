# Developing Preen

## Dependencies
* Poetry >= 1.1
* Python >= 3.6
* Pytest >= 7.0

# Deploying
1. Create or login to your account on [PyPI](https://pypi.org/) and the [PyPI test](https://test.pypi.org/)
2. For security reasons it is strongly recommended to create an [API token](https://pypi.org/help/#apitoken) If you haven’t done so, create an API token on both PyPI and the PyPI test server (for Caktus developers API token is located in LastPass)
3. Configure the repository 

```shell
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

4. Publish the repository

```shell
poetry publish -r testpypi --build
```

5. Push updated version to Pypi

```shell
poetry config pypi-token.testpypi <API Token>
```
