from wagtail.core import blocks


class Analyzer:

    def __init__(self, block) -> None:
        self.block = block
        self.declared_blocks = []
        self.base_blocks = []
        self.block_representation = {}

    def analyze_block(self):
        for dblock in self.declared_blocks:
            if isinstance(dblock, blocks.StreamBlock):
                self.declared_blocks.append(Analyzer(dblock))
            else:
                breakpoint()
                self.block_representation[dblock]
        for bblock in self.base_blocks:
            self.base_blocks.append(Analyzer)
