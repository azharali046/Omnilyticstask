import csv
import json
import math
import os
import random
import string
from constants import  FIELD_NAMES, CSV_FILE, FILE_SIZE, OBJECT_STR_LENGTH, OBJECT_INT_LENGTH, \
    OBJECT_REAL_LENGTH, OBJECT_ALPHA_NUMERIC_LENGTH
from random import randint
import pandas as pd


# function to create random strings
def generate_random_string():
    """
    :return:
    """
    random_str = ''.join(random.choices(string.ascii_letters, k=OBJECT_STR_LENGTH))
    return random_str


# function to create random integers
def generate_random_integers():
    """

    :return:
    """
    random_integers = random_with_N_digits(OBJECT_INT_LENGTH)
    return random_integers


# function to create random realnumber
def generate_random_realnumbers():
    """

    :return:
    """
    random_real_numbers = random_with_N_digits(OBJECT_REAL_LENGTH, type='Real')
    return random_real_numbers



# function to create random alphanumeric
def generate_random_alphanumeric():
    """

    :return:
    """
    random_alpha_numeric = ''.join(random.choices(string.ascii_letters + string.digits, k=OBJECT_ALPHA_NUMERIC_LENGTH))
    return random_alpha_numeric


def random_with_N_digits(n, type=None):
    """

    :param n:
    :return:
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    if type:
        return random.uniform(range_start, range_end)
    else:
        return randint(range_start, range_end)


def generate_csv():
    """
    :return:
    """
    size = 0
    while size <= FILE_SIZE:
        print(size)
        random_str = generate_random_string()
        random_int = generate_random_integers()
        random_alpha_num = generate_random_alphanumeric()
        random_real_num = generate_random_realnumbers()
        # check if file already exist then only append to existing
        if os.path.isfile(CSV_FILE):
            mode = 'a'
        else:
            mode = 'w'
        rows = [{
            "Random String": random_str,
            "Random Integers": random_int,
            "Random Real Numbers": random_real_num,
            "Random Alpha Numeric": random_alpha_num
        }]

        with open(CSV_FILE, mode, encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
            if mode == 'w':
                writer.writeheader()
            writer.writerows(rows)
        size = round(os.stat(CSV_FILE).st_size / 1048576, 2)


def get_default_param(request, key, default):
    """

    :param request:
    :param key:
    :param default:
    :return:
    """
    key = request.args.get(key)
    return key or default


def calaculate_count(file_name):
    """
    :return:
    """
    df = pd.read_csv(file_name)
    random_str_count = len(df['Random String']) * OBJECT_STR_LENGTH
    random_int_count = len(df['Random Integers']) * OBJECT_INT_LENGTH
    random_real_num_count = len(df['Random Real Numbers']) * OBJECT_REAL_LENGTH
    random_alpha_num_count = len(df['Random Alpha Numeric']) * OBJECT_ALPHA_NUMERIC_LENGTH

    data = {
        "Random String Count": random_str_count,
        "Random Integer Count": random_int_count,
        "Random Real Number Count": random_real_num_count,
        "Random Alpha Numeric Count": random_alpha_num_count
    }
    return data



