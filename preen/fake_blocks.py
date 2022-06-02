from random import randint
from faker import Faker

fake = Faker()
Faker.seed(randint(1, 100000))


def fake_char_block(*args):
    return fake.sentence(nb_words=3)

def fake_url_block(*args):
    return fake.url()

def fake_rich_text_block(*args):
    return fake.text(max_nb_chars=20)

def fake_RawTextBlock(*args):
    return fake.text(max_nb_chars=20)

def fake_TextBlock(*args):
    return fake.text(max_nb_chars=20)

def fake_BooleanBlock(*args):
    return fake.boolean(chance_of_getting_true=50)

def fake_DateBlock(*args):
    return fake.date()

def fake_time_block(*args):
    return fake.time()

def fake_date_time_block(*args):
    return fake.date_time()

def fake_email_block(*args):
    return fake.email()

def fake_integer_block(*args):
    return randint(1, 10000)

def fake_float_block(*args):
    return fake.pyfloat(positive=True, max_value=1000, right_digits=5)

def fake_RichTextBlock(*args):
    return fake.text(max_nb_chars=20)

def fake_BlockQuoteBlock(*args):
    return fake.text(max_nb_chars=50)

def fake_RegexBlock(*args):
    return fake.text(max_nb_chars=50)

def fake_DecimalBlock(*args):
    return fake.pyfloat(positive=True, max_value=7000, right_digits=6)

FAKE_BLOCK_MAP = {
    "URLBlock": fake_url_block,
    "CharBlock": fake_char_block,
    "RichTextBlock": fake_rich_text_block,
    "RawHTMLBlock": fake_RawTextBlock,
    "TextBlock": fake_TextBlock,
    "BooleanBlock": fake_BooleanBlock,
    "DateBlock": fake_DateBlock,
    "TimeBlock": fake_time_block,
    "DateTimeBlock": fake_date_time_block,
    "EmailBlock": fake_email_block,
    "IntegerBlock": fake_integer_block,
    "FloatBlock": fake_float_block,
    "DecimalBlock": fake_DecimalBlock,
    "RegexBlock": fake_RegexBlock,
    "BlockQuoteBlock": fake_BlockQuoteBlock,
    "RichTextBlock": fake_RichTextBlock,
    # "ChoiceBlock", # pass a choice block you have given choices to
    # "MultipleChoiceBlock",
    # "ImageChooserBlock", # return pk of image
    # "DocumentChooserBlock",
    # "PageChooserBlock",
}
