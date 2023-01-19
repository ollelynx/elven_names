"""Retrieve names from the file."""
from typing import Optional

from .message import display_d10
from .number import get_pair_numbers, roll_dice
from .typing_ import OptionalStrInt
from .utils import get_table_data


class ElfNameGenerator:
    """Make an Elf Name based on given numbers."""

    def __init__(self,
                 first_part: OptionalStrInt = None,
                 last_part: OptionalStrInt = None,
                 dice_number: Optional[int] = None) -> None:
        """Initialize an object.

        E.g.:
            first_part: [79, 49]
            last_part: [99, [85, 70]]

        Note: Once there's no input data for first_part,
              second_part and dice_number will be ignored
              and generated automatically.
        """
        self._dice_number = dice_number
        self._prefixes = None
        self._suffixes = None

        if first_part:
            self._first_part = first_part
            self._last_part = last_part
        else:
            self._roll_dice()

    def get_name(self) -> str:
        """Get a name by a given number.

        E.g.
            input: (["'", 32], [43, [16, 99]])
            output: Har'Jaavelyth
        """
        self._get_table_data()
        f_name = self._make_a_word(self._first_part)
        l_name = ''
        if self._last_part:
            l_name = ' ' + self._make_a_word(self._last_part)
        return f_name + (l_name[1:] if f_name.endswith("'") else l_name)

    def get_alternatives(self):
        """Retrieve alternative names if any."""
        if not self._prefixes:
            raise NameError('Run name generator to retrieve alternative '
                            'names.')

        raise NotImplementedError('Make a method!')

    def get_definition(self) -> str:
        """Retrieve the meaning of a name.

        E.g.
            input: (["'", 32], [43, [16, 99]])
            output: Wisdom/wise Staff
        """
        if not self._prefixes:
            raise NameError('Run name generator to retrieve its definition.')

        definition = self._make_a_definition(self._first_part)
        if self._last_part:
            definition += ' ' + self._make_a_definition(self._last_part)

        return definition

    def roll_dice_message(self):
        return display_d10(self._dice_number)

    @property
    def dice_number(self):
        if not self._dice_number:
            return "*"
        return self._dice_number

    def _roll_dice(self):
        """Roll dice and get pair numbers."""
        self._dice_number = roll_dice()
        self._first_part, self._last_part = get_pair_numbers(self._dice_number)

    def _make_a_word(self, name_number: OptionalStrInt) -> str:
        """Concatenate prefix and suffix for a name.

        E.g.
            name_number: [79, 49], [99, [85, 70]], None
        """
        if not name_number:
            return ''

        prf_num, prefix = name_number[0], '\''
        if isinstance(prf_num, int):
            prefix = self._prefixes[prf_num]['name'][0]  # for 1st element

        suf_num, suffix = name_number[1], ''
        if isinstance(suf_num, int):
            suffix = self._suffixes[suf_num]['name'][0]  # for 1st element
        elif isinstance(suf_num, list):
            suffix = ''.join([self._suffixes[_]['name'][0]  # for 1st element
                              for _ in suf_num])

        if prefix == "'":
            prefix, suffix = suffix.capitalize(), prefix
        return prefix + suffix

    def _make_a_definition(self, name_number: OptionalStrInt) -> str:
        """Create a word based on a name and values."""
        def delimiter(name):
            return '/' if len(name) > 1 else ''

        def get_meaning(key, t3=False):
            table = self._prefixes if not t3 else self._suffixes
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

    def _get_table_data(self) -> None:
        """Retrieve text from files Table2 and Table3.

        Get text lines of given numbers only.
        """
        last_part_prefix, last_part_suffix = '', ''
        first_part_prefix, first_part_suffix = self._first_part

        if isinstance(self._last_part, list):
            last_part_prefix = self._last_part[0]
            if len(self._last_part) > 1:
                last_part_suffix = self._last_part[1]

        self._prefixes, self._suffixes = get_table_data(
            first_part_prefix, first_part_suffix,
            last_part_prefix, last_part_suffix)
