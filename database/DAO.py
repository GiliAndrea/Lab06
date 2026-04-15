from database import DB_connect
from model.retailer import Retailer


class DAOClass():
    def __init__(self):
        pass

    # function that request the data from the database
    @staticmethod
    def getAllRetailers():
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = """select * from go_retailers"""

        cursor.execute(query)

        result = []
        for row in cursor:
            newRetailer = Retailer(code = row["Retailer_code"], name = row["Retailer_name"],
                                   country = row["Country"], type = row["Type"])
            result.append(newRetailer)
        return result

    # function that request the data from the database
    @staticmethod
    def getAllYeras():
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = """select distinct year(Date)
                from go_daily_sales gds """

        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["year(Date)"])

        return result

    # function that request the data from the database
    @staticmethod
    def getAllBrands():
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select Product_brand
                from go_products gp 
                group by gp.Product_brand"""

        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row["Product_brand"])
        return result

    @staticmethod
    def getDataFilter(year = str | None, brand = str | None, retailer = None):
        pass
