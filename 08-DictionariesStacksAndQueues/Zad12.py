import json


dictionary={
    "title":"wiedzmin",
    "author":"Andrzej Sapkowski",
    "books":"6",
    "released":"2000r"

}
with open("favourite.json",'w') as file:
    json.dump(dictionary,file,indent= " ")