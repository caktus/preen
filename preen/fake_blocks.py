import random
from random import randint
from faker import Faker

fake = Faker()
Faker.seed(randint(1, 100000))


class FakeBlockProvider:

    FAKE_BLOCK_MAP = {
        "URLBlock": "fake_url_block",
        "CharBlock": "fake_char_block",
        "RichTextBlock": "fake_rich_text_block",
        "RawHTMLBlock": "fake_raw_html_block",
        "TextBlock": "fake_text_block",
        "BooleanBlock": "fake_boolean_block",
        "DateBlock": "fake_date_block",
        "TimeBlock": "fake_time_block",
        "DateTimeBlock": "fake_date_time_block",
        "EmailBlock": "fake_email_block",
        "IntegerBlock": "fake_integer_block",
        "FloatBlock": "fake_float_block",
        "DecimalBlock": "fake_decimal_block",
        "RegexBlock": "fake_regex_block",
        "BlockQuoteBlock": "fake_block_quote_block",
        "ChoiceBlock": "fake_choice_block",  # pass a choice block you have given choices to
        "MultipleChoiceBlock": "fake_multiple_choice_block",
        "ImageChooserBlock": "fake_image_chooser_block",  # return pk of image
        "DocumentChooserBlock": "fake_document_chooser_block",
        "PageChooserBlock": "fake_page_chooser_block"
    }

    def __init__(self, block_def, **kwargs) -> None:
        self.block = block_def
        import pdb;
        pdb.set_trace()
        self.block_call = getattr(self, FakeBlockProvider.FAKE_BLOCK_MAP.get(self.block.__class__.__name__))
        self.exclude_fields = kwargs.get('exclude_fields', {})
        self.override_block = kwargs.get('override_block', {})
        self.options = kwargs

    def render(self):
        if self.override_block:
            return self.override_block
        return self.block_call()

    def fake_char_block(self):
        return fake.sentence(nb_words=self.options.get('nb_words', 3))

    def fake_url_block(self):
        return fake.url()

    def fake_rich_text_block(self):
        return fake.text(max_nb_chars=self.options.get('max_nb_chars', 20))

    def fake_raw_html_block(self):
        return fake.text(max_nb_chars=20)

    def fake_text_block(self):
        return fake.text(max_nb_chars=20)

    def fake_boolean_block(self):
        return fake.boolean(chance_of_getting_true=50)

    def fake_date_block(self):
        return fake.date()

    def fake_time_block(self):
        return fake.time()

    def fake_date_time_block(self):
        return fake.date_time()

    def fake_email_block(self):
        return fake.email()

    def fake_integer_block(self):
        return randint(1, 10000)

    def fake_float_block(self):
        return fake.pyfloat(positive=True, max_value=1000, right_digits=5)

    def fake_block_quote_block(self):
        return fake.text(max_nb_chars=50)

    def fake_regex_block(self):
        return fake.text(max_nb_chars=50)

    def fake_decimal_block(self):
        return fake.pyfloat(positive=True, max_value=7000, right_digits=6)

    def fake_choice_block(self):
        # 1 in kwargs
        if choices := self.block.__dict__.get("_constructor_args")[1].get("choices", {}):
            return random.choice([x for x, v in choices])
        elif default := self.block.__dict__.get("_constructor_args")[1].get("default", ""):
            return str(default)
        else:
            return "<NO_CHOICES>"

    def fake_multiple_choice_block(self):
        return "EMPTY"

# TODO: These are blocks that require a database. Need to think about best way to approach.
# For now fake pks

    def fake_image_chooser_block(self):
        return randint(1, 100)

    def fake_page_chooser_block(self):
        return randint(1, 100)

    def fake_document_chooser_block(self):
        return randint(1, 100)