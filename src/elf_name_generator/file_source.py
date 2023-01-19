"""Utils module."""

import os
import re
from typing import Tuple

from .base_source import SourceObject
from .typing_ import List, OptionalStrInt

BASE_DIR = os.path.join(os.path.dirname(__file__))
FILE_T2 = '../names/t2.txt'
FILE_T3 = '../names/t3.txt'


class FileSource(SourceObject):
    """Data collects prefixes and suffixes based on given numbers."""

    _prefixes = None
    _suffixes = None

    def make_a_word(self,
                    prefix: OptionalStrInt,
                    suffix: OptionalStrInt = None) -> str:
        """Concatenate prefix and suffix for a name.

        E.g.
            name_number: [79, 49], [99, [85, 70]], None
        """
        if not prefix:
            return ''

        if not self._prefixes:
            raise ValueError('Run get_table_data(*args) first.')

        if isinstance(prefix, int):
            prefix = self._prefixes[prefix]['name'][0]

        # int or list[int]
        if isinstance(suffix, int):
            suffix = self._suffixes[suffix]['name'][0]  # for the 1st element
        elif isinstance(suffix, list):
            suffix = ''.join([self._suffixes[_]['name'][0]  # for 1st element
                              for _ in suffix])
        else:
            suffix = ''

        if prefix == "'":
            prefix, suffix = suffix.capitalize(), prefix
        return prefix + suffix

    def retrieve_a_meaning(self, name_number: OptionalStrInt) -> str:
        """Retrieve meaning based on numbers."""
        if not self._prefixes:
            raise ValueError('Run get_table_data(*args) first.')

        def delimiter(name):
            return '/' if len(name) > 1 else ''

        def get_meaning(key, suffix_table=False):
            table = self._prefixes if not suffix_table else self._suffixes
            return table[key]['meaning']

        prf_num, prefix = name_number[0], ''
        if isinstance(prf_num, int):
            prefix = get_meaning(prf_num)

        suf_num, suffix = name_number[1], ''
        if isinstance(suf_num, int):
            suffix = get_meaning(suf_num, True)
        elif isinstance(suf_num, list):
            suffix = []
            sfx_list = [get_meaning(_, True) for _ in suf_num]
            for s_l in sfx_list:
                delimiter_ = "" if len(s_l) == 1 else ","
                suffix.append(delimiter_.join(s_l))

        definition = delimiter(prefix).join(prefix).capitalize()

        if suffix:
            definition += ' ' + delimiter(suffix).join(suffix)
        return definition.lstrip().capitalize()

    def get_table_data(self, *prefix_suffix_args: list) -> None:
        """Retrieve text from files Table2 and Table3.

        Table2 stands for prefixes
        Table3 stands for suffixes
        Get text lines of given numbers only.
        """
        self._prefixes, self._suffixes = get_table_data(*prefix_suffix_args)


def full_path(file_name: str) -> str:
    """Make an absolute path to a file."""
    return os.path.join(BASE_DIR, file_name)


def get_table_data(first_pref: OptionalStrInt,
                   first_suf: OptionalStrInt,
                   last_pref: OptionalStrInt,
                   last_suf: OptionalStrInt) -> Tuple[dict, dict]:
    """Retrieve table data from a file."""
    def sorted_(input_):
        # List of numbers for a name prefix and suffix
        return sorted(re.findall(r'\d+', str(input_)))

    file2 = full_path(FILE_T2)
    file3 = full_path(FILE_T3)

    if not os.path.exists(file2) or not os.path.exists(file3):
        raise FileNotFoundError(f'{FILE_T2} and/or {FILE_T3} is not found.')

    return (_read_from_file(file2, sorted_([first_pref, last_pref])),
            _read_from_file(file3, sorted_([first_suf, last_suf])))


def _parse_data(row: str) -> dict:
    """Parse str line."""
    str_list = re.findall(r'[A-Za-z\-]+', row)
    word_part, meaning = [], []
    for char in str_list:
        if char.startswith('-'):
            word_part.append(char[1:])
        elif char.istitle():
            word_part.append(char)
        else:
            meaning.append(char)

    return {'name': word_part, 'meaning': meaning}


def _read_from_file(file_name: str,
                    diced_numbers: List[int]) -> dict:
    """Read data from a file."""
    output = {}
    with open(file_name, 'r', encoding='utf-8') as rows:
        for row in rows:
            line_number = re.search(r'\d+', row).group()
            if line_number in diced_numbers:
                output[int(line_number)] = _parse_data(row)
    return output
