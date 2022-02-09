# Preen
### A library to support testing of Wagtail sites

## What is Preen?

Preen is a library that makes testing even complex, nested Wagtail blocks easier by allowing Django/Wagtail developers to simply pass in the block they'd like to test, along with optional data/config parameters, and recieve a `soup` that can be used to test expected conditions in the block's rendered state.


## Why are we doing this?

Testing Wagtail blocks gets increasingly hairy as they get more complex.  That's because of the way Wagtail encodes and hydrates blocks (and their related data) in complex JSON structures. You cannot simply test one piece of a complex block on its own. Wagtail will require that you provide the full context for each parent block, which can lead to some elaborate, time consuming test-writing and idiosyncratic workarounds. 

Given that so many of Caktus' projects use Wagtail, it doesn't make sense tackle this shared problem on a project-by-project basis. Our goal is to make a standalone library that's easy to install and use on any Wagtail project.  


## What are we using to build it?

- [Poetry] (https://python-poetry.org/docs/): Dependency manager to enable live updates of module in local development environment and easy upload to PyPi.
- [Pytest] (https://docs.pytest.org/en/7.0.x/): A framework for writing tests in python that simplifies Django testing.
- [Factory Boy] (https://factoryboy.readthedocs.io/en/stable/): A fixtures replacement tool that replaces static, hard to maintain fixtures with easy-to-use factories for complex objects.
- [Pytest Fixtures] (https://docs.pytest.org/en/6.2.x/fixture.html): Fixture tool for pytest.
- [Faker] (https://faker.readthedocs.io/en/master/): Test data generator.

## How does it work?

tbd

## Where does it live?

pypi - tbd

## How do I get involved?

only do this if you're up for an adventure at this stage!

