"""Mock test data."""

from collections import namedtuple

ElfNameMock = namedtuple('ElfNameMock',
                         'first_part last_part prefixes suffixes')

elf_name1 = ElfNameMock(
    [79, 49],
    [99, [85, 70]],
    {
        79: {
            'name': ['She'],
            'meaning': ['age', 'time']
        },
        99: {
            'name': ['Za'],
            'meaning': ['royal']
        },
    },
    {
        49: {
            'name': ['lian', 'lia'],
            'meaning': ['master', 'mistress']
        },
        70: {
            'name': ['ro', 'ri', 'ron'],
            'meaning': ['walker', 'walks']
        },
        85: {
            'name': ['thus', 'thas', 'aethus', 'aethas'],
            'meaning': ['harp', 'harper']
        }
    }
)


elf_name2 = ElfNameMock(
    [27, 65],
    None,
    {
        27: {
            'name': ['Eil'],
            'meaning': ['azure', 'blue']
        }
    },
    {
        65: {
            'name': ['rah', 'rae', 'raee'],
            'meaning': ['beast']
        }
    }
)


def table2_line():
    row1 = '{93} Ty (Try): crystal'
    row2 = '{94} Uth : wizard'
    row3 = '{95} Ver : peace'
    row4 = '{96} Vil : finger, point'
    row5 = '{97} Von : ice'
    row6 = '{98} Ya : bridge, path, way'
    row7 = '{99} Za : royal'
    return list(locals().values())


def table2_parsed_line():
    row1 = {
        'meaning': ['crystal'],
        'name': ['Ty', 'Try']
    }
    row2 = {
        'meaning': ['wizard'],
        'name': ['Uth']
    }
    row3 = {
        'meaning': ['peace'],
        'name': ['Ver']
    }
    row4 = {
        'meaning': ['finger', 'point'],
        'name': ['Vil']
    }
    row5 = {
        'meaning': ['ice'],
        'name': ['Von']
    }
    row6 = {
        'meaning': ['bridge', 'path', 'way'],
        'name': ['Ya']
    }
    row7 = {
        'meaning': ['royal'],
        'name': ['Za']
    }
    return list(locals().values())


def table3_line():
    row1 = '{70} -ro (-ri; -ron) : walker, walks\n'
    row2 = '{71} -ruil (-aruil; -eruil) : noble\n'
    row3 = '{72} -sal (-isal; -sali) : honey, sweet\n'
    row4 = '{73} -san : drink, wine\n'
    row5 = '{77} -spar : fist\n'
    row6 = '{78} -tae (-itae) : beloved, love\n'
    row7 = '{81} -thal /-tha (-ethal / -etha) : heal, healer, healing'
    return list(locals().values())


def table3_parsed_line():
    row1 = {
        'meaning': ['walker', 'walks'],
        'name': ['ro', 'ri', 'ron']
    }
    row2 = {
        'meaning': ['noble'],
        'name': ['ruil', 'aruil', 'eruil']
    }
    row3 = {
        'meaning': ['honey', 'sweet'],
        'name': ['sal', 'isal', 'sali']
    }
    row4 = {
        'meaning': ['drink', 'wine'],
        'name': ['san']
    }
    row5 = {
        'meaning': ['fist'],
        'name': ['spar']
    }
    row6 = {
        'meaning': ['beloved', 'love'],
        'name': ['tae', 'itae']
    }
    row7 = {
        'meaning': ['heal', 'healer', 'healing'],
        'name': ['thal', 'tha', 'ethal', 'etha']
    }
    return list(locals().values())
