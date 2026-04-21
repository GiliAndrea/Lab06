from database import DAO
from model.retailer import Retailer


class Model:
    def __init__(self):
        pass

    # function that return data fron DAO
    def getAllYears(self):
        return DAO.DAOClass.getAllYeras()

    # function that return data fron DAO
    def getAllBrands(self):
        return DAO.DAOClass.getAllBrands()

    # function that return data fron DAO
    def getAllRetailers(self):
        return DAO.DAOClass.getAllRetailers()

    def getTopSales(self, year: int, brand: str,
                    retailer: Retailer):
        return DAO.DAOClass.getDataFilter(year = year, brand = brand, retailer = retailer)

    def getInfoSales(self, year: int, brand: str,
                     retailer: str):
        pass