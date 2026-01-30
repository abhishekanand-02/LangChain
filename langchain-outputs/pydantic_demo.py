from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = "Abhishek Anand"
    age : Optional[int] = None
    email : EmailStr  = None
    cgpa : float = Field(gt=0, lt = 10, default= 8 , description= "A decimal value representing the cgpa of a student ")


new_student = {'name':'Abhishek'}
second = {'name': 32}
# third = {'age' : '23', 'email' : 'abc@gmail.com', 'cgpa' : 9}   # It will take default value
third = {}

student = Student(** third)
print(student)
