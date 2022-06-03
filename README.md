# Preen
### A library to support testing of Wagtail sites

## What is Preen?

Preen is a library that makes testing even complex, nested Wagtail blocks easier by allowing Django/Wagtail developers to simply pass in the block they'd like to test, along with optional data/config parameters, and recieve a `soup` that can be used to test expected conditions in the block's rendered state.


## Why are we doing this?

Testing Wagtail blocks gets increasingly complex.  That's because of the way Wagtail encodes and hydrates blocks (and their related data) in complex JSON structures. One cannot simply test one piece of a complex block on its own. Wagtail requires full context for each parent block, which can lead to some elaborate, time-consuming test-writing, and idiosyncratic workarounds. 

Given that many Caktus projects use Wagtail, it doesn't make sense tackling a shared problem on a project-by-project basis. Our goal is to make a standalone library that's easy to install and use on any Wagtail project.  


## What are we using to build it?

- [Poetry] (https://python-poetry.org/docs/): Dependency manager to enable live updates of module in local development environment and easy upload to PyPi.
- [Pytest] (https://docs.pytest.org/en/7.0.x/): A framework for writing tests in python that simplifies Django testing.
- [Factory Boy] (https://factoryboy.readthedocs.io/en/stable/): A fixtures replacement tool that replaces static, hard to maintain fixtures with easy-to-use factories for complex objects.
- [Pytest Fixtures] (https://docs.pytest.org/en/6.2.x/fixture.html): Fixture tool for pytest.
- [Faker] (https://faker.readthedocs.io/en/master/): Test data generator.

## How does it work?

tbd

## Where does it live?

pypi

## How do I get involved?

Only do this if you're up for an adventure at this stage!

## Dev Setup
In the virtual environment where you will be testing Preen modules, 
install in editable mode with pip.

```shell
    $ pip install -e ../<PATH_TO_YOUR_LOCAL_PREEN>
```