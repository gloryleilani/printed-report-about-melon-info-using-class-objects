############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.name = name
        self.pairings = []
        self.code = code
        self.color = color
        self.first_harvest = first_harvest
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f'Code updated to {new_code}')



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, False, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint') 
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    #print(all_melon_types[0].name) #Should print Muskmelon, which it does.
    #print(all_melon_types[0].pairings)
    #print(all_melon_types[0].code)
    #print(all_melon_types[0].color)
    return all_melon_types

melon_types = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print(f'{melon_type.name} pairs with')
        
        for item in melon_type.pairings:
            print(f'- {item}')
        

print_pairing_info(melon_types)



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types_dict = {}
    #print("melon types list:", melon_types)
    #print("melon code:", melon_types[0].code)

    for melon_type in melon_types:
        if melon_type.code not in melon_types_dict:
            melon_types_dict[melon_type.code] = melon_type
    #print("Melon types dict:", melon_types_dict)

    return melon_types_dict

make_melon_type_lookup(melon_types)




############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_harvested_from, harvested_by):
        """Initialize a melon"""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvested_from = field_harvested_from
        self.harvested_by = harvested_by


    def is_sellable(self):
        """Determines whether a melon is sellable, using logic relating to its attributes""" 

        if (self.shape_rating > 5 and self.color_rating > 5 and self.field_harvested_from != 3): 
            return True 
        else: 
            return False
    

def make_melons(melon_types):
    """Returns a list of Melon objects."""


    all_melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")

    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Marvin")

    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Donnie")

    melon_4 = Melon(melons_by_id["cas"], 8, 7, 2, "Bernie")

    melon_5 = Melon(melons_by_id["cren"], 8, 7, 2, "Lani")

    all_melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5])
 
    print("Print field harvested by for Melon 5", all_melons[4].harvested_by) 
    return all_melons

all_melons = make_melons(melon_types)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        sell_status = "(CAN BE SOLD)" if melon.is_sellable() else "(NOT SELLABLE)"

        print(f"Harvested by {melon.harvested_by} from Field {melon.field_harvested_from} {sell_status}")
        print(f"Melon type: {melon.melon_type.name}")

get_sellability_report(all_melons)




