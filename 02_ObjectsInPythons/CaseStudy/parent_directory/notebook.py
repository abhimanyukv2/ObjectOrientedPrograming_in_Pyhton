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

class Notebook:
    '''Represent a collection of notes that can be taged,
    modified and search.'''

    def __init__(self):
        '''Iiniialize a Notebook with a empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo,tags))

    def _find_note(self,note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
            return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given Id and change its
        memo to given value.'''
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = memo
        #         break
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.tags = tags
        #         break
        self._find_note(note_id).tags = tags

    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]