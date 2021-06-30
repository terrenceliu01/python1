def findItemLocation(itemName):
    """
    Return location for given item name.
    """
    locations = { # mock data
        'pliers':'shelf2, row1, column1.',
        'batteray':'kitchen 1st drawer'
    }
    return locations[itemName]


#TDD: Test Driving Development
if __name__ == '__main__':
    itemName = 'batteray'
    location = findItemLocation(itemName)
    print(f"Your {itemName} are located at {location}")
