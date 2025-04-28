from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(dt=0, lt=10,default=5,description='A decimal value representing the cgpa of the student')



new_student={'name':'Shuchi','age':'32','email':'abc@gmail.com'}

student = Student(**new_student)

print(student)
print(student.name)

student_dict=dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()