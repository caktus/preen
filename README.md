# Preen
### A library to support testing of Wagtail sites

## What is Preen?

Preen is a library that makes testing even complex, nested Wagtail blocks easier by allowing Django/Wagtail developers to simply pass in the block they'd like to test, along with optional data/config parameters, and recieve a `soup` that can be used to test expected conditions in the block's rendered state.

## Installing

```python
pip install preen
```

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

This is still a nascent project, but what it does now is give the user back a block representation that can be used with the following
block render pattern.

### BlockAnalyzer

```python
from preen.block import BlockAnalyzer
from myproject.blocks import my_complex_block

analyzer = BlockAnalyzer(my_complex_block, no_object=True)
my_block_representation = analyzer.block_representation
print(my_block_representation)
```
Most likely `my_block_representation` will need a little tweaking to pass a full clean a la:

```python
html = my_complex_block.render(my_complex_block.clean(my_complex_block.to_python(my_block_representation))
```

but it should `render`:

```python
html = my_complex_block.render(value=block_def)
```

### BlockFaker

There is also a `BlockFaker` class that is currently only a little functional. The goal with `BlockFaker` is 
to return a rendered, faked block with as little intervention as possible.

Currently this should, give you faked output for most Wagtail block types. It does not yet handle faking types that require
a running test environment to make fakes (e.g., PageChooserBlock, DocumentChooserBlock, ImageChooserBlock)

```python
from preen.block import BlockFaker, BlockAnalyzer
from preen.fake_blocks import FakeBlockProvider
from myproject.blocks import my_complex_block

analyzer = BlockAnalyzer(my_complex_block)  # We don't use `no_object` here because we want the block_types to be available
block_faker = BlockFaker(analyzer, FakeBlockProvider)
```

## Where does it live?

https://pypi.org/project/preen/

## How do I get involved?

Only do this if you're up for an adventure at this stage!

## Dev Setup
In the virtual environment where you will be testing Preen modules, 
install in editable mode with pip.

```shell
    $ pip install -e ../<PATH_TO_YOUR_LOCAL_PREEN>
```