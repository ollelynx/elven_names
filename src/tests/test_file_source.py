"""Test utils module."""

import pytest

from elf_name_generator import file_source
from tests.mock_data import (
    elf_name1,
    elf_name2,
    table2_line,
    table2_parsed_line,
    table3_line,
    table3_parsed_line,
)


@pytest.mark.parametrize(
    "row_input,expected",
    [
        [table3_line()[0], table3_parsed_line()[0]],
        [table3_line()[1], table3_parsed_line()[1]],
        [table3_line()[2], table3_parsed_line()[2]],
        [table3_line()[3], table3_parsed_line()[3]],
        [table3_line()[4], table3_parsed_line()[4]],
        [table3_line()[-3], table3_parsed_line()[-3]],
        [table3_line()[-2], table3_parsed_line()[-2]],
        [table3_line()[-1], table3_parsed_line()[-1]],
    ],
)
def test_parse_line_of_table3(row_input, expected):
    result = file_source._parse_data(row_input)
    assert result == expected


@pytest.mark.parametrize(
    "row_input,expected",
    [
        [table2_line()[0], table2_parsed_line()[0]],
        [table2_line()[1], table2_parsed_line()[1]],
        [table2_line()[2], table2_parsed_line()[2]],
        [table2_line()[3], table2_parsed_line()[3]],
        [table2_line()[4], table2_parsed_line()[4]],
        [table2_line()[-3], table2_parsed_line()[-3]],
        [table2_line()[-2], table2_parsed_line()[-2]],
        [table2_line()[-1], table2_parsed_line()[-1]],
    ],
)
def test_parse_line_of_table2(row_input, expected):
    result = file_source._parse_data(row_input)
    assert result == expected


def test_full_name():
    """Create full name based on prefixes and suffixes."""
    fs = file_source.FileSource()
    fs._prefixes = elf_name1.prefixes
    fs._suffixes = elf_name1.suffixes

    first_name = fs.make_a_word(*elf_name1.first_part)
    last_name = fs.make_a_word(*elf_name1.last_part)
    expected = "Shelian Zathusro"
    assert expected == first_name + " " + last_name


def test_first_name():
    """Create first name based on full and first part only."""
    fs = file_source.FileSource()
    fs._prefixes = elf_name2.prefixes
    fs._suffixes = elf_name2.suffixes
    name = fs.make_a_word(*elf_name2.first_part)
    expected = "Eilrah"
    assert expected == name


def test_full_name_definition():
    fs = file_source.FileSource()
    fs._prefixes = elf_name1.prefixes
    fs._suffixes = elf_name1.suffixes

    first_name = fs.make_a_word(*elf_name1.first_part)
    last_name = fs.make_a_word(*elf_name1.last_part)
    first_meaning = fs.retrieve_a_meaning(elf_name1.first_part)
    last_meaning = fs.retrieve_a_meaning(elf_name1.last_part)

    expected_name = "Shelian Zathusro"
    assert expected_name == first_name + " " + last_name

    expected_meaning = ("Age/time master/mistress Royal "
                        "harp,harper/walker,walks")
    assert expected_meaning == first_meaning + " " + last_meaning


def test_source_exception():
    fs = file_source.FileSource()

    with pytest.raises(ValueError) as exc:
        fs.make_a_word(*elf_name2.first_part)
    assert "Run get_table_data(*args) first." in str(exc.value)
