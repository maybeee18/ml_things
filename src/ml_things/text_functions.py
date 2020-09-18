# coding=utf-8
# Copyright 2020 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Functions that deal with text/string"""

import re
import copy
import string


def clean_text(text, full_clean=False, punctuation=False, numbers=False, lower=False, extra_spaces=False,
               control_characters=False, tokenize_whitespace=False, remove_characters=''):
    """Clean text using various techniques.

    :param text: string that needs cleaning
    :param full_clean: remove: punctuation, numbers, extra space, control characters and lower case
    :param punctuation: remove punctuation from text.
    :param numbers: remove digits from text.
    :param lower: lower case all text.
    :param extra_spaces: remove extra spaces - everything beyond one space.
    :param control_characters: remove characters like `\n`, `\t` etc.
    :param tokenize_whitespace: return a list of tokens split on whitespace.
    :param remove_characters: remove defined characters form text.
    :return: cleaned text or list of tokens of cleaned text.
    """

    if not isinstance(text, str):
        # `text` is not type of string
        raise ValueError("`text` is not of type str!")

    if not isinstance(remove_characters, str):
        # remove characters need to be a string
        raise ValueError("`remove_characters` needs to be a string!")

    # all control characters like `\t` `\n` `\r` etc.
    # Stack Overflow: https://stackoverflow.com/a/8115378/11281368
    control_characters_list = ''.join([chr(char) for char in range(1, 32)])

    # define control characters table
    table_control_characters = str.maketrans(dict.fromkeys(control_characters_list))

    # remove punctuation table
    table_punctuation = str.maketrans(dict.fromkeys(string.punctuation))

    # remove numbers table
    table_digits = str.maketrans(dict.fromkeys('0123456789'))

    # remove certain characters table
    table_remove_characters = str.maketrans(dict.fromkeys(remove_characters))

    # make a copy of text to make sure it doesn't affect original text
    cleaned = copy.deepcopy(text)

    if full_clean or punctuation:
        # remove punctuation
        cleaned = cleaned.translate(table_punctuation)

    if full_clean or numbers:
        # remove numbers
        cleaned = cleaned.translate(table_digits)

    if full_clean or extra_spaces:
        # remove extra spaces - also removes control characters
        # Stack Overflow https://stackoverflow.com/a/2077906/11281368
        cleaned = re.sub('\s+', ' ', cleaned).strip()

    if full_clean or lower:
        # lowercase
        cleaned = cleaned.lower()

    if control_characters:
        # remove control characters
        cleaned = cleaned.translate(table_control_characters)

    if tokenize_whitespace:
        # tokenizes text n whitespace
        cleaned = re.split('\s+', cleaned)

    if remove_characters:
        # remove these characters from text
        cleaned = cleaned.translate(table_remove_characters)

    return cleaned
