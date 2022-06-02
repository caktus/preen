from wagtail.core import blocks


block_classes = [
    "FieldBlock", "CharBlock", "URLBlock", "RichTextBlock", "RawHTMLBlock", "ChooserBlock",
    "PageChooserBlock", "TextBlock", "BooleanBlock", "DateBlock", "TimeBlock",
    "DateTimeBlock", "ChoiceBlock", "MultipleChoiceBlock", "EmailBlock", "IntegerBlock",
    "FloatBlock", "DecimalBlock", "RegexBlock", "BlockQuoteBlock",
    "ImageChooserBlock", "DocumentChooserBlock", "PageChooserBlock",
]


class Analyzer:
    def __init__(self, block) -> None:
        self.block = block
        self.block_representation = {}
        self.list_blocks = {}
        self.stream_blocks = {}
        self.other_complex = {}

    def to_representation(self):
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
            elif block.__class__.__name__ not in block_classes:
                self.block_representation[name] = self.block_render(block)
                self.other_complex[name] = block
            else:
                self.block_representation[name] = "<insert-value>"

    def _get_iter_blocks(self):
        if hasattr(self.block, 'child_blocks'):
            return self.block.child_blocks
        if hasattr(self.block, 'base_blocks'):
            return self.block.base_blocks

    def list_block_render(self, block):
        analyzer = Analyzer(block.child_block)
        analyzer.to_representation()
        return analyzer.block_representation

    def stream_block_render(self, block_name, block):
        stream_parent = {}
        analyzer = Analyzer(block)
        analyzer.to_representation()
        stream_parent["type"] = block_name
        stream_parent["value"] = analyzer.block_representation
        return stream_parent

    def block_render(self, block):
        analyzer = Analyzer(block)
        analyzer.to_representation()
        return analyzer.block_representation