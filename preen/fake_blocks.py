from random import randint
from faker import Faker

fake = Faker()
Faker.seed(randint(1, 100000))


def fake_char_block(**kwargs):
    return fake.sentence(nb_words=3)


def fake_url_block(**kwargs):
    return fake.url()


def fake_rich_text_block(**kwargs):
    return fake.text(max_nb_chars=20)


def fake_raw_html_block(**kwargs):
    return fake.text(max_nb_chars=20)


def fake_text_block(**kwargs):
    return fake.text(max_nb_chars=20)


def fake_boolean_block(**kwargs):
    return fake.boolean(chance_of_getting_true=50)


def fake_date_block(**kwargs):
    return fake.date()


def fake_time_block(**kwargs):
    return fake.time()


def fake_date_time_block(**kwargs):
    return fake.date_time()


def fake_email_block(**kwargs):
    return fake.email()


def fake_integer_block(**kwargs):
    return randint(1, 10000)


def fake_float_block(**kwargs):
    return fake.pyfloat(positive=True, max_value=1000, right_digits=5)


def fake_block_quote_block(**kwargs):
    return fake.text(max_nb_chars=50)


def fake_regex_block(**kwargs):
    return fake.text(max_nb_chars=50)


def fake_decimal_block(**kwargs):
    return fake.pyfloat(positive=True, max_value=7000, right_digits=6)


def fake_choice_block(**kwargs):
    return "EMPTY"


def fake_multiple_choice_block(**kwargs):
    return "EMPTY"


def fake_image_chooser_block(**kwargs):
    return "EMPTY"


def fake_page_chooser_block(**kwargs):
    return "EMPTY"


def fake_document_chooser_block(**kwargs):
    return "EMPTY"


FAKE_BLOCK_MAP = {
    "URLBlock": fake_url_block,
    "CharBlock": fake_char_block,
    "RichTextBlock": fake_rich_text_block,
    "RawHTMLBlock": fake_raw_html_block,
    "TextBlock": fake_text_block,
    "BooleanBlock": fake_boolean_block,
    "DateBlock": fake_date_block,
    "TimeBlock": fake_time_block,
    "DateTimeBlock": fake_date_time_block,
    "EmailBlock": fake_email_block,
    "IntegerBlock": fake_integer_block,
    "FloatBlock": fake_float_block,
    "DecimalBlock": fake_decimal_block,
    "RegexBlock": fake_regex_block,
    "BlockQuoteBlock": fake_block_quote_block,
    "ChoiceBlock": fake_choice_block,  # pass a choice block you have given choices to
    "MultipleChoiceBlock": fake_multiple_choice_block,
    "ImageChooserBlock": fake_image_chooser_block,  # return pk of image
    "DocumentChooserBlock": fake_document_chooser_block,
    "PageChooserBlock": fake_page_chooser_block
}
