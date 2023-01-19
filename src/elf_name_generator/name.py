"""Retrieve names from the file."""

from typing import Optional

from .base_source import SourceObject
from .file_source import FileSource
from .message import display_d10
from .number import get_pair_numbers, roll_dice
from .typing_ import OptionalStrInt


def get_source() -> SourceObject:
    """Fabric to use FileData or DB Data."""
    return FileSource()


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

        if first_part:
            self._first_part = first_part
            self._last_part = last_part
        else:
            self._roll_dice()

        self._source = get_source()
        self._source.get_table_data(
            *_prepare_input_numbers_to_prefix_suffix(
                self._first_part, self._last_part)
        )

    def get_name(self) -> str:
        """Get a name by a given number.

        E.g.
            input: (["'", 32], [43, [16, 99]])
            output: Har'Jaavelyth
        """
        f_name = self._source.make_a_word(*self._first_part)
        l_name = ''
        if self._last_part:
            _last_part = (self._last_part
                          if isinstance(self._last_part, list)
                          else [self._last_part])
            l_name = ' ' + self._source.make_a_word(*_last_part)
        return f_name + (l_name[1:] if f_name.endswith("'") else l_name)

    def get_alternatives(self):
        """Retrieve alternative names if any."""
        raise NotImplementedError('Make a method!')

    def get_definition(self) -> str:
        """Retrieve the meaning of a name.

        E.g.
            input: (["'", 32], [43, [16, 99]])
            output: Wisdom/wise Staff
        """
        definition = self._source.retrieve_a_meaning(self._first_part)
        if self._last_part:
            definition += ' ' + self._source.retrieve_a_meaning(
                self._last_part)

        return definition

    def roll_dice_message(self):
        """Display text of run algo to generate a name numbers."""
        return display_d10(self._dice_number)

    @property
    def dice_number(self):
        """Dice number provides the algo to generate the name."""
        if not self._dice_number:
            return "*"
        return self._dice_number

    def _roll_dice(self):
        """Roll dice and get pair numbers."""
        self._dice_number = roll_dice()
        self._first_part, self._last_part = get_pair_numbers(self._dice_number)


def _prepare_input_numbers_to_prefix_suffix(
        first_part_numbers: OptionalStrInt,
        second_part_numbers: OptionalStrInt = None):
    """Divide input numbers to separate variables."""
    first_part_prefix, first_part_suffix = first_part_numbers
    last_part_prefix, last_part_suffix = '', ''

    if isinstance(second_part_numbers, list):
        last_part_prefix = second_part_numbers[0]
        if len(second_part_numbers) > 1:
            last_part_suffix = second_part_numbers[1]

    return (first_part_prefix, first_part_suffix,
            last_part_prefix, last_part_suffix)
