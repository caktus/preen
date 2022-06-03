from .fake_blocks import FakeBlockProvider

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
    def __init__(self, analyzer: BlockAnalyzer, fake_block_provider: FakeBlockProvider) -> None:
        self.analyzer = analyzer
        self.block_rep = analyzer.block_representation.copy()
        self.fake_block_provider = fake_block_provider

    def _get_block_value(self, block):
        return self.fake_block_provider(block).render()

    def _walk_value_dict(self, stream_value: dict) -> dict:
        internal_block = {}
        for k, v in stream_value.items():
            if isinstance(v, dict):
                internal_block[k] = self._walk_value_dict(v)
                continue
            if isinstance(v, list):
                # Probably a nested stream block
                internal_block[k] = self._walk_stream_block(v)
                continue
            else:
                internal_block[k] = self._get_block_value(v)
        return internal_block

    def _walk_stream_block(self, blocks) -> list[dict]:
        sblock = []
        for parent_block in blocks:
            sblock_item = {'type': '', 'value': {}}
            for name, value in parent_block.items():
                if name == 'type':
                    sblock_item['type'] = value
                else:
                    sblock_item['value'] = self._walk_value_dict(value)
            sblock.append(sblock_item.copy())
        return sblock

    def simple_fake(self):
        for name, block_def in self.block_rep.items():
            if isinstance(block_def, list):
                # This could be either ListBlock or StreamBlock
                if isinstance(block_def[0], dict):
                    # StreamBlock
                    self.block_rep[name] = self._walk_stream_block(block_def)
                else:
                    # List Blocks can only have a single child block
                    self.block_rep[name] = self._get_block_value(block_def[0])
            else:
                self.block_rep[name] = self._get_block_value(block_def)