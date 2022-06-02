simple_block_types = [
    "FieldBlock",
    "CharBlock",
    "URLBlock",
    "RichTextBlock",
    "RawHTMLBlock",
    "ChooserBlock",
    "TextBlock",
    "BooleanBlock",
    "DateBlock",
    "TimeBlock",
    "DateTimeBlock",
    "EmailBlock",
    "IntegerBlock",
    "FloatBlock",
    "DecimalBlock",
    "RegexBlock",
    "BlockQuoteBlock",
    "RichTextBlock"
]

complex_block_types = [
    "ChoiceBlock",
    "MultipleChoiceBlock",
    "ImageChooserBlock",
    "DocumentChooserBlock",
    "PageChooserBlock",
]

analyzer_simple = simple_block_types + complex_block_types


class BlockAnalyzer:

    def __init__(self, block, **kwargs) -> None:
        self.arguments = kwargs
        self.no_object = self.arguments.get('no_object', False)
        self.block = block
        self.block_representation = {}
        self.list_blocks = {}
        self.stream_blocks = {}
        self.other_complex = {}
        self._build_representation()

    def _build_representation(self):
        for name, block in self._get_iter_blocks().items():
            if block.__class__.__name__ == 'ListBlock':
                self.block_representation[name] = self.list_block_render(block)
                self.list_blocks[name] = block
            if block.__class__.__name__ == 'StreamBlock':
                sub_blocks = []
                for child_name, child_block in block.child_blocks.items():
                    sub_blocks.append(self.stream_block_render(child_name, child_block))
                self.block_representation[name] = sub_blocks
                self.stream_blocks[name] = block
            elif block.__class__.__name__ not in analyzer_simple:
                self.block_representation[name] = self.block_render(block)
                self.other_complex[name] = block
            else:
                self.block_representation[name] = block
                if self.no_object:
                    self.block_representation[name] = block.__class__.__name__

    def _get_iter_blocks(self):
        if hasattr(self.block, 'child_blocks'):
            return self.block.child_blocks
        if hasattr(self.block, 'base_blocks'):
            return self.block.base_blocks

    def list_block_render(self, block):
        analyzer = BlockAnalyzer(block.child_block, **self.arguments)
        return analyzer.block_representation

    def stream_block_render(self, block_name, block):
        stream_parent = {}
        analyzer = BlockAnalyzer(block, **self.arguments)
        stream_parent["type"] = block_name
        stream_parent["value"] = analyzer.block_representation
        return stream_parent

    def block_render(self, block):
        analyzer = BlockAnalyzer(block, **self.arguments)
        return analyzer.block_representation


class BlockRenderer:
    def __init__(self, analyzer: BlockAnalyzer) -> None:
        self.analyzer = analyzer
