from database import DAO
from model.retailer import Retailer
from model.sale import Sale


class Model:
    def __init__(self):
        pass

    # function that return data fron DAO
    def getAllYears(self) -> list[str]:
        return DAO.DAOClass.getAllYeras()

    # function that return data fron DAO
    def getAllBrands(self) -> list[str]:
        return DAO.DAOClass.getAllBrands()

    # function that return data fron DAO
    def getAllRetailers(self) -> list[Retailer]:
        # from getAllRetailers arrive an unordered list of Retailer object
        data = DAO.DAOClass.getAllRetailers()
        # the list is sorted by the name of the retailer (Reverse = False)
        ordinated_data = sorted(data, key = lambda i: i.name)
        return ordinated_data

    # function that takes a list of Sales by the work of getDataFillerSecond and sortes the list by
    # the revenue, it is one of the fild of Sales object, al list the function return the first five
    def getTopSales(self, year: int, brand: str,
                    retailer: Retailer) -> list[Sale]:
        data = DAO.DAOClass.getDataFilter(year = year, brand = brand, retailer = retailer)
        ordinated_data = sorted(data, key = lambda i: i.ricavo, reverse = True)
        return ordinated_data[0:5]

    # function that takes a list of Sales by the work of getDataFillerSecond and calculates the info that
    # are placed in a dictionary, after the filling it is returned
    def getInfoSales(self, year: int, brand: str,
                     retailer: Retailer) -> dict:
        result = {}
        data = DAO.DAOClass.getDataFilter(year = year, brand = brand, retailer = retailer)
        result["giro"] = summRevenue(data)
        result["numero_vendite"] = len(data)
        result["numero_prodotti"] = numProduct(data)
        result["numero_retailer"] = numReteiler(data)
        return result

def summRevenue(info: list[Sale]) -> float:
    result = 0

    for s in info:
        result += s.ricavo
    return result

def numProduct(info: list[Sale]) -> int:
    result = 0
    products = []

    for s in info:
        if s.Product_number not in products:
            result += 1
            products.append(s.Product_number)
    return result

def numReteiler(info: list[Sale]) -> int:
    result = 0
    retailers = []

    for s in info:
        if s.Retailer_code not in retailers:
            result += 1
            retailers.append(s.Retailer_code)
    return result
