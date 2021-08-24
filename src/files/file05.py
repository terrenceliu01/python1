"""
write json object to json file
"""

import json

with open("data/student.json", "+w") as file:
    json.dump([
        {
            'firstname':'Terry',
            'lastname':'Liu',
            'id':'111'
        },
        {
            'firstname':'John',
            'lastname':'Wang',
            'id':'222'
        },
        {
            'firstname':'David',
            'lastname':'Zhang',
            'id':'333'           
        },
    ], file)

print("Done")