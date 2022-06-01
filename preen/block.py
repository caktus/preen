from wagtail.core import blocks
from wagtail.core.blocks import StructBlock


class Analyzer:
    def __init__(self, block) -> None:
        self.block = block
        self.block_representation = {}

    def to_representation(self):
        for bblock in self.block.base_blocks:
            block_class = self.block.base_blocks.get(bblock)
            if self.is_simple(block_class):
                self.block_representation[bblock] = "<insert-value>"
            else:
                analyzer = Analyzer(block_class)
                import pdb;
                pdb.set_trace()
                analyzer.to_representation()
                self.block_representation[bblock] = analyzer.block_representation

    def is_simple(self, block):
        complex_blocks = ['ListBlock', 'StreamBlock']
        if block.__class__.__name__ not in complex_blocks:
            return True
