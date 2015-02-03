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

