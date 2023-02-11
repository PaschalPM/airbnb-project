#!/usr/bin/python3
'''
This Module creates the BaseModel Class as a template
for other models created
'''

from uuid import uuid4
from datetime import datetime

class BaseModel:
    '''
    A class to represent the base model.
    
    ...

    Attributes
    ----------
    id : str - uuid(uuid4)
    created_at : datetime - current datetime when a new instance is created
    updated_at : datetime - current datetime when a new instance is created and it 
                 will be updated every time an instance of the base model changes

    Methods
    -------
    save():
        updates the public instance attribute updated_at with the current datetime
    to_dict():
        returns a dictionary containing all keys/values of __dict__ of the instance
    '''

    def __init__(self):
        '''
        Constructs all the neccesary attributes for the BaseModel
        Object
        '''
        self.id = uuid4().__str__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        " Returns the string representation of an instance of the Base Model class "
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        " Updates the public instance attribute updated_at with the current datetime "
        self.updated_at = datetime.now()

    def to_dict(self):
        " returns a dictionary containing all keys/values of __dict__ of the instance "
        dict_copy = { **self.__dict__ }
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = datetime.isoformat(self.created_at)
        dict_copy["updated_at"] = datetime.isoformat(self.updated_at)
        return dict_copy