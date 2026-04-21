from dataclasses import dataclass

@dataclass
class Retailer:
    code: int
    type: str
    country: str
    name: str

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)

    def __str__(self):
        return f"name: {self.name} - code: {self.code}"
