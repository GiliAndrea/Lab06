from database import DAO


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

    def getTopSales(self, year: int | None, brand: str | None,
                    retailer: None):
        pass

    def getInfoSales(self, year: int | None, brand: str | None,
                     retailer: None):
        pass