class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print('''
        PROPERTY DETAILS
    ===========================
        Square Footage: {self.square_feet}
        Bedrooms: {self.num_bedrooms}
        Bathrooms: {self.num_baths}''')

    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds = input('Enter number of bedrooms: '),
                    baths = input('Enter number of baths: '))

    prompt_init = staticmethod(prompt_init)