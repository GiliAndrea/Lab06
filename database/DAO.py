from database import DB_connect
from model.retailer import Retailer
from model.sale import Sale


class DAOClass():
    def __init__(self):
        pass

    # function that request the data from the database and return all the object retailer from the dataBase
    @staticmethod
    def getAllRetailers() -> list[Retailer]:
        cnx = DB_connect.DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)

        query = """select * from go_retailers"""

        cursor.execute(query)

        result = []
        for row in cursor:
            newRetailer = Retailer(code = row["Retailer_code"], name = row["Retailer_name"],
                                   country = row["Country"], type = row["Type"])
            result.append(newRetailer)
        cnx.close()
        cursor.close()
        return result

    # function that request the data from the database and return a list of string
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
        cnx.close()
        cursor.close()
        return result

    # function that request the data from the database and return a list of string
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
        cnx.close()
        cursor.close()
        return result

# So, what is written below this comment is actually a part that is correct
# but in the same time is not correct as well, essentially this function (getDataFilter)
# comes out well for some request, so particular selection in the search fild, and comes out
# wrong for other selectio and request

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
                     from go_daily_sales gds"""
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
            new_sale = Sale(Retailer_code = row["Retailer_code"], Product_number = row["Product_number"],
                            Order_method_code = row["Order_method_code"], Date = row["Date"],
                            Quantity = row["Quantity"], Unit_price = row["Unit_price"],
                            Unit_sale_price = row["Unit_sale_price"], ricavo = 0.0)
            new_sale.ricavoSale()
            result.append(new_sale)
        cnx.close()
        cursor.close()
        return result