from .fake_blocks import FAKE_BLOCK_MAP

simple_block_types = [
    "FieldBlock",
    "CharBlock",
    "URLBlock",
    "RichTextBlock",
    "RawHTMLBlock",
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
        if blocks := self._get_iter_blocks():
            for name, block in blocks.items():
                if block.__class__.__name__ == 'ListBlock':
                    self.block_representation[name] = [block.child_block]
                    self.list_blocks[name] = block
                    continue
                if block.__class__.__name__ == 'StreamBlock':
                    sub_blocks = []
                    for child_name, child_block in block.child_blocks.items():
                        sub_blocks.append(self.stream_block_render(child_name, child_block))
                    self.block_representation[name] = sub_blocks
                    self.stream_blocks[name] = block
                    continue
                elif block.__class__.__name__ not in analyzer_simple:
                    self.block_representation[name] = self.block_render(block)
                    self.other_complex[name] = block
                else:
                    self._terminal_block(name, block)
        else:
            # This shouldn't be reached, but it's here to catch problems.
            self._terminal_block("", self.block)

    def _terminal_block(self, name, block):
        if not name:
            name = block.__class__.__name__
        self.block_representation[name] = block
        if self.no_object:
            self.block_representation[name] = name

    def _get_iter_blocks(self):
        if hasattr(self.block, 'child_blocks'):
            return self.block.child_blocks
        if hasattr(self.block, 'base_blocks'):
            return self.block.base_blocks

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

    def simple_fake(self):
        for k, v in self.analyzer.block_representation.items():
            if isinstance(v, list):
                for x in v:
                    print(f"{k}::{FAKE_BLOCK_MAP.get(x.__class__.__name__)()}")
            if isinstance(v, dict):
                for subk, subv in v.items():
                    print(f"{subk}::{FAKE_BLOCK_MAP.get(subv.__class__.__name__)()}")
            else:
                import pdb;
                pdb.set_trace()
                print(f"{k}::{FAKE_BLOCK_MAP.get(v.__class__.__name__)()}")