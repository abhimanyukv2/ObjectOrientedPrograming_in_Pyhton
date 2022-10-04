import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each notes.'''

    def __init__(self, memo, tags=''):
        '''Initialize a note with memo and optional
        space seperated tags. Automatically set the note's
        creation date and unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determined if this note natches the filter text.
        Return if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.'''
        return filter in self.memo or filter in self.tags