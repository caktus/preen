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

    def to_representation(self):
        for name, block in self._get_iter_blocks().items():
            if block.__class__.__name__ == 'ListBlock':
                self.block_representation[name] = self.list_block_render(block)
            if block.__class__.__name__ == 'StreamBlock':
                self.block_representation[name] = [self.stream_block_render(block)]
            elif block.__class__.__name__ not in block_classes:
                self.block_representation[name] = self.block_render(block)
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

    def stream_block_render(self, block):
        stream_parent = {}
        items = {}
        for k, v in block.child_blocks.items():
            analyzer = Analyzer(v)
            analyzer.to_representation()
            items[k] = analyzer.block_representation
            stream_parent["type"] = k
            stream_parent["value"] = items
        return stream_parent

    def block_render(self, block):
        analyzer = Analyzer(block)
        analyzer.to_representation()
        return analyzer.block_representation