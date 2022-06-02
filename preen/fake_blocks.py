from random import randint
from faker import Faker

fake = Faker()
fake.seed(randint(1, 100000))


def fake_char_block(*args):
    return fake.sentence(nb_words=3)


FAKE_BLOCK_MAP = {
    "CharBlock": fake_char_block,
}