from typing import TypedDict

class PersonInfo(TypedDict):
    name: str
    age: int

def process_person_info(info: PersonInfo) -> None:
    print(f"Name: {info['name']}, Age: {info['age']}")

# 正確使用
person_a: PersonInfo = {"name": "Alice", "age": 30}
process_person_info(person_a)

# 若缺少必須的鍵，靜態檢查工具會報錯
person_b: PersonInfo = {"name": "Bob"}  # error: Missing key 'age'
process_person_info(person_b)