class Interval(object):
    # two ways to call constructor:
    #
    # Interval(low_note, high_note) returns interval between
    #
    # Interval(its_interval, its_type, its_tonal_flag)

    the_basic_intervals = {}

    tonal_types = \
    {
        "qu.d": -4,
        "tri.d": -3,
        "do.d": -2,
        "d": -1,
        "p": 0,
        "a": 1,
        "do.a": 2,
        "tr.a": 3,
        "qu.a": 4
    }

    modal_types = \
    {
        "qu.d": -5,
        "tri.d": -4,
        "do.d": -3,
        "d": -2,
        "mi": -1,
        "Ma": 0,
        "a": 1,
        "do.a": 2,
        "tr.a": 3,
        "qu.a": 4
    }

    def __init__(self, one, two, three=None):
        if three is None:
            low_note, high_note = one, two

            # TESTING:
            self.low_note, self.high_note = one, two

            # get basic interval from table
            # apply offsets from accidentals
            # overall. set its_interval. its_type and its_tonal_flag
        else:
            self.its_interval = one

            self.its_tonal_flag = three

            if self.its_tonal_flag:
                self.its_type = self.tonal_types[two]
            else:
                self.its_type = self.modal_types[two]

    intervals_str = \
    [
        "unison or octave",
        "second or ninth",
        "third or tenth",
        "fourth or eleventh",
        "fifth or twelvth",
        "sixth or thirteenth",
        "seventh"
    ]

    tonal_types_str = \
    [
        "quadruply dimished",
        "triply dimished",
        "doubly dimished",
        "dimished",
        "perfect",
        "augmented",
        "doubly augmented",
        "triply augmented",
        "quadruply augmented",
    ]

    modal_types_str = \
    [
        "quadruply dimished",
        "triply dimished",
        "doubly dimished",
        "dimished",
        "minor",
        "major",
        "augmented",
        "doubly augmented",
        "triply augmented",
        "quadruply augmented",
    ]

    def __str__(self):
        if self.its_tonal_flag:
            result = self.tonal_types_str[self.its_type + 4]
        else:
            result = self.modal_types_str[self.its_type + 5]

        result += " "

        result += self.intervals_str[self.its_interval - 1]

        return result

    accidental_modifiers = \
    {
        'bb': -2,
        'b': -1,
        '': 0,
        '#': 1,
        'x': 2
    }

    def split_note(self, note_str):
        letter = note_str[0]
        accidental = note_str[1:]

        # note, a regex for doing the same as above is r'([A-G])(?:bb|b|x|#)'

        return [letter, accidental_modifiers[accidental]]

I = Interval

intervals_list = \
[
    I(1, "p", True), I(2, "Ma", False), I(3, "mi", False), I(4, "p", True), I(5, "p", True), I(6, "Ma", False), I(7, "Ma", False),
    I(7, "mi", False), I(1, "p", True), I(2, "Ma", False), I(3, "mi", False), I(4, "p", True), I(5, "p", True), I(6, "Ma", False),
    I(6, "mi", False), I(7, "mi", False), I(1, "p", True), I(2, "mi", False), I(3, "mi", False), I(4, "p", True), I(5, "p", True),
    I(5, "p", True), I(6, "Ma", False), I(7, "Ma", False), I(1, "p", True), I(2, "Ma", False), I(3, "Ma", False), I(4, "a", True), 
    I(4, "p", True), I(5, "p", True), I(6, "Ma", False), I(7, "mi", False), I(1, "p", True), I(2, "Ma", False), I(3, "Ma", False),
    I(3, "mi", False), I(4, "p", True), I(5, "p", True), I(6, "mi", False), I(7, "mi", False), I(1, "p", True), I(2, "Ma", False),
    I(2, "mi", False), I(3, "mi", False), I(4, "p", True), I(5, "d", True), I(6, "mi", False), I(7, "mi", False), I(1, "p", True),
]

# idea for generating the keys, observe the output of [(x,y) for x in range(5) for y in ["a", "b"]]

letter_list = ["C", "D", "E", "F", "G", "A", "B"]

keys_list = [(x,y) for x in letter_list for y in letter_list]

# now set class var
Interval.the_basic_intervals = dict(zip(keys_list, intervals_list))
