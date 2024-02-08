from dataclasses import dataclass
from typing import List
import json

@dataclass
class Personne:
    person_id: int
    name: str
    registered: bool

def serialize_objects_to_json(persons: List[Personne]) -> str:
    return json.dumps([person.__dict__ for person in persons])

def deserialize_json_to_objects(data_json: str) -> List[Personne]:
    data = json.loads(data_json)
    return [Personne(**person_data) for person_data in data]

def main():
    json = '''[
        {"person_id":1,"name":"Bryon Hetrick","registered":true},
        {"person_id":2,"name":"Nicole Wilcox","registered":true},
        {"person_id":3,"name":"Adrian Martinson","registered":false},
        {"person_id":4,"name":"Nora Osborn","registered":false}
    ]'''
    
    # raw json string
    print("json:", json)
    
    # Recupere (deserialise) une liste de Personnes fortement typées
    personnes = deserialize_json_to_objects(json)
    print("persons:", personnes)

    print(f"Personne 1 nom:{personnes[0].name}")
    
    # Retourne en json string
    personnesJson = serialize_objects_to_json(persons=personnes)
    print("personnes (JSON):", personnesJson)

if __name__ == "__main__":
    main()
