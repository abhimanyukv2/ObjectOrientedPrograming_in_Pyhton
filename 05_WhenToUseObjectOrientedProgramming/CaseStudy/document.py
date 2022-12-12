class Document:
    def __init__(self):
        self.characters = []
        self.cursor = 0
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        del self.characters[self.cursor]

    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close

    def forward(self):
        self.cursor += 1
    
    def back(self):
        self.cursor -= 1

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1
    
    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to the beginning of file before new line
                break

    def end(self):
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1