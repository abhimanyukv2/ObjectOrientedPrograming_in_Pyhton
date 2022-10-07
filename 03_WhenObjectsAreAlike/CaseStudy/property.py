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
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input('Enter number of bedrooms: '),
                    baths=input('Enter number of baths: '))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('''
            APARTMENT DETAILS
        ==========================
            Laundry: {self.laundry}
            Balcony: {self.balcony}''')

    def prompt_init():
        parent_init = Property.prompt_init()

        def get_valid_input(input_string, valid_options):
            input_string += '({})'.format(', '.join(valid_options))
            responce = input(input_string)
            while responce.lower() not in valid_options:
                responce = input(input_string)
            return responce

        '''laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input('What laundry facilities does the property have? ({})'
                            .format(','.join(Apartment.valid_laundries)))'''

        laundry = get_valid_input('What laundry facilities does the property have?',
                                  Apartment.valid_laundries)

        '''balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input('Does the property have a balcony? ({})'
                            .format(','.join(Apartment.valid_balconies)))'''

        balcony = get_valid_input('Does the property have a balcony? ',
                                  Apartment.valid_balconies)

        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)

class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    vallid_fenced = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print('''
            HOUSE DETAILS
        =====================
            Number of stories: {self.num_stories}
            Garage: {self.garage}
            Fenced Yard: {self.fenced}''')

    def prompt_init():
        parent_init = Property.prompt_init()
        
        def get_valid_input(input_string, valid_options):
            input_string += '({})'.format(', '.join(valid_options))
            responce = input(input_string)
            while responce.lower() not in valid_options:
                responce = input(input_string)
            return responce

        fenced = get_valid_input('Is the yard fenced? ',House.vallid_fenced)
        garage = get_valid_input('Is there a garage? ',House.valid_garage)
        num_stories = input('How many stories? ')

        parent_init.update({
            'fenced': fenced,
            'garage': garage,
            'num_stories': num_stories
        })
        return parent_init
    
    prompt_init = staticmethod(prompt_init)