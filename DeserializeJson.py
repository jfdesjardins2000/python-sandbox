from dataclasses import dataclass
from typing import List
import json

@dataclass
class Person:
    person_id: int
    name: str
    registered: bool

def main():
    json = '''[
        {"person_id":1,"name":"Bryon Hetrick","registered":true},
        {"person_id":2,"name":"Nicole Wilcox","registered":true},
        {"person_id":3,"name":"Adrian Martinson","registered":false},
        {"person_id":4,"name":"Nora Osborn","registered":false}
    ]'''
    
    print("json:", json)
    persons = deserialize_json_to_objects(json)
    print("persons:", persons)

def serialize_objects_to_json(persons: List[Person]) -> str:
    return json.dumps([person.__dict__ for person in persons])

def deserialize_json_to_objects(data_json: str) -> List[Person]:
    data = json.loads(data_json)
    return [Person(**person_data) for person_data in data]

if __name__ == "__main__":
    main()
