"""Mock test data."""
from collections import namedtuple

ElfNameMock = namedtuple('ElfNameMock',
                         'first_part last_part t2_data t3_data')

elf_name1 = ElfNameMock(
    [79, 49],
    [99, [85, 70]],
    {
        79: {
            'prefix': ['She'],
            'meaning': ['age', 'time']
        },
        99: {
            'prefix': ['Za'],
            'meaning': ['royal']
        },
    },
    {
        49: {
            'suffix': ['lian', 'lia'],
            'meaning': ['master', 'mistress']
        },
        70: {
            'suffix': ['ro', 'ri', 'ron'],
            'meaning': ['walker', 'walks']
        },
        85: {
            'suffix': ['thus', 'thas', 'aethus', 'aethas'],
            'meaning': ['harp', 'harper']
        }
    }
)


elf_name2 = ElfNameMock(
    [27, 65],
    None,
    {
        27: {
            'prefix': ['Eil'],
            'meaning': ['azure', 'blue']
        }
    },
    {
        65: {
            'suffix': ['rah', 'rae', 'raee'],
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
        'prefix': ['Ty', 'Try']
    }
    row2 = {
        'meaning': ['wizard'],
        'prefix': ['Uth']
    }
    row3 = {
        'meaning': ['peace'],
        'prefix': ['Ver']
    }
    row4 = {
        'meaning': ['finger', 'point'],
        'prefix': ['Vil']
    }
    row5 = {
        'meaning': ['ice'],
        'prefix': ['Von']
    }
    row6 = {
        'meaning': ['bridge', 'path', 'way'],
        'prefix': ['Ya']
    }
    row7 = {
        'meaning': ['royal'],
        'prefix': ['Za']
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
        'suffix': ['ro', 'ri', 'ron']
    }
    row2 = {
        'meaning': ['noble'],
        'suffix': ['ruil', 'aruil', 'eruil']
    }
    row3 = {
        'meaning': ['honey', 'sweet'],
        'suffix': ['sal', 'isal', 'sali']
    }
    row4 = {
        'meaning': ['drink', 'wine'],
        'suffix': ['san']
    }
    row5 = {
        'meaning': ['fist'],
        'suffix': ['spar']
    }
    row6 = {
        'meaning': ['beloved', 'love'],
        'suffix': ['tae', 'itae']
    }
    row7 = {
        'meaning': ['heal', 'healer', 'healing'],
        'suffix': ['thal', 'tha', 'ethal', 'etha']
    }
    return list(locals().values())
