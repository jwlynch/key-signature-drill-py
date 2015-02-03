class Interval(object):
    
    def __init__(self, one, two, three=None):
        if three is None:
            low_note, high_note = one, two

            # TESTING:
            self.low_note, self.high_note = one, two

            # get basic interval from table
            # apply offsets from accidentals
            # overall. set its_interval. its_type and its_tonal_flag
        else:
            self.its_interval, self.its_type, self.its_tonal_flag = one, two, three

