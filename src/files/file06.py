import json

person = """{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}"""

person_dict = json.loads(person)
print(type(person_dict))
print(person_dict)
print(person_dict["menu"]["id"])
print(person_dict['menu']['popup']['menuitem'][1]['onclick'])