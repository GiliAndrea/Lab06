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
    def getDataFilter(year: int, brand: str, retailer: Retailer):
        query = ""
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        parametroUno = brand
        parametroDue = retailer.code
        parametroTre = year
        print(parametroUno, parametroDue, parametroTre)

        if year == None and brand != None and retailer.code != 0:
            query = """select *
                    from go_daily_sales gds , go_products gp
                    where gds.Product_number = gp.Product_number
                    and gp.Product_brand = %s
                    and gds.Retailer_code = %s"""
            cursor.execute(query, (parametroUno, parametroDue, ))
        elif year == None and brand == None and retailer.code != 0:
            query = """select *
                    from go_daily_sales gds , go_products gp
                    where gds.Product_number = gp.Product_number
                    and gds.Retailer_code = %s"""
            cursor.execute(query, (parametroDue, ))
        elif year == None and brand == None and retailer.code == 0:
             query = """select *
                     from go_daily_sales gds , go_products gp
                     where gds.Product_number = gp.Product_number"""
             cursor.execute(query)
        elif brand == None and year != None and retailer.code != 0:
            query = """select *
                    from go_daily_sales gds , go_products gp
                    where gds.Product_number = gp.Product_number
                    and gds.Retailer_code = %s
                    and year(gds.`Date`) = %s"""
            cursor.execute(query, (parametroDue, parametroTre,))
        elif retailer.code == 0 and year == None and brand != None:
            query = """select *
                    from go_daily_sales gds , go_products gp 
                    where gds.Product_number = gp.Product_number
                    and gp.Product_brand = %s"""
            cursor.execute(query, (parametroUno, ))
        elif retailer.code == 0 and year != None and brand != None:
            query = """select *
                from go_daily_sales gds , go_products gp 
                where gds.Product_number = gp.Product_number
                and gp.Product_brand = %s
                and year(gds.`Date`) = %s"""
            cursor.execute(query, (parametroUno, parametroTre,))
        elif brand == None and retailer.code == 0 and year != None:
            query = """select *
                from go_daily_sales gds , go_products gp 
                where gds.Product_number = gp.Product_number
                and year(gds.`Date`) = %s"""
            cursor.execute(query, (parametroTre, ))
        elif brand != None and retailer.code != 0 and year != None:
            query = """select *
                    from go_daily_sales gds , go_products gp 
                    where gds.Product_number = gp.Product_number
                    and gp.Product_brand = %s
                    and gds.Retailer_code = %s
                    and year(gds.`Date`) = %s"""
            cursor.execute(query, (parametroUno, parametroDue, parametroTre, ))

        result = []
        for row in cursor:
            vendita = {}
            vendita["Product_brand"] = row["Product_brand"]
            vendita["Retailer_code"] = row["Retailer_code"]
            vendita["Product_number"] = row["Product_number"]
            vendita["Date"] = row["Date"]
            result.append(vendita)
        print(result)
        return result

