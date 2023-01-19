"""Base class for sources."""

from abc import ABC, abstractmethod

from .typing_aliases import OptionalStrInt


class SourceObject(ABC):
    """Data collects prefixes and suffixes based on given numbers."""

    _prefixes = None
    _suffixes = None

    @abstractmethod
    def make_a_word(self,
                    prefix: OptionalStrInt,
                    suffix: OptionalStrInt = None) -> str:
        """Concatenate prefix and suffix for a name.

        E.g.
            name_number: [79, 49], [99, [85, 70]], None
            The method gets the name by digit and form a name.
        """

    @abstractmethod
    def retrieve_a_meaning(self, name_number: OptionalStrInt) -> str:
        """Retrieve meaning based on numbers."""

    @abstractmethod
    def get_table_data(self, *prefix_suffix_args: list) -> None:
        """Retrieve text from Prefixes and Suffixes."""
