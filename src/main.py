"""Elf Name Generator.

Each elf name consists of a prefix (from Table 2) and one or more suffixes
(from Table 3). Definitions have been included in these tables to help
determine what a name means once it has been generated. In the case of
suffixes, male and female endings have been included where appropriate.
Alternate spellings have also been provided in some cases. In Some Cases a
formal house name can be generated as well by rolling randomly on Optional
Table 1B. These formal House names would be used for ancient noble houses,
usually of Grey or Gold Elf Descent.
"""
from environs import Env

from elf_name_generator import ElfNameGenerator, get_pair_numbers, roll_dice

env = Env()
DEBUG = env.bool('DEBUG', 'False')


if __name__ == "__main__":
    if DEBUG:
        # >>> "9": Shelian Zathusro
        # >>> "9": Age/time master/mistress Royal harp,harper/walker,walks
        elf_name_numbers, dice_number = ([79, 49], [99, [85, 70]]), 9
        # elf_name_numbers, dice_number = (["'", 53], [30, [9, 26]]), 10
    else:
        dice_number = roll_dice()
        elf_name_numbers = get_pair_numbers(dice_number)

    elf = ElfNameGenerator(*elf_name_numbers, dice_number=dice_number)
    print(f'>>> "{elf.dice_number}":', elf.roll_dice_message())
    print(f'>>> "{elf.dice_number}":', elf_name_numbers)
    print(f'>>> "{elf.dice_number}":', elf.get_name())
    print(f'>>> "{elf.dice_number}":', elf.get_definition())
