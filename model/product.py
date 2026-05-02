from dataclasses import dataclass

# this class is actually unuseful, so that it is
@dataclass
class Product():
    code = int
    line = str
    name = str
    brand = str
    type = str
    color = str
    price  = int
    cost = int

def __str__(self):
    return f"name: {self.name} - code: {self.code}"

def __eq__(self, other):
    return self.code == other.code

def __hash__(self):
    return hash(self.code)
