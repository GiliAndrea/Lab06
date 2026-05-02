import flet as ft
from model.retailer import Retailer


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # the values, they arrive from the data of the button
        self._year = None
        self._brand = None
        self._retailer = None

    # function of the elevated button infoSales
    def getInfoSales(self, e):
        self._view._txtResult.controls.clear()

        # from getInfoSales arrive a dictionary with all the info that are needed to fill
        # some Text fild on the controls
        info = self._model.getInfoSales(year = self._year, brand = self._brand, retailer = self._retailer)
        self._view._txtResult.controls.append(ft.Text(value=f"Statistiche vendite: \n"
                                                            f"Giro d'affari: {info["giro"]} \n"
                                                            f"Numero vendite: {info["numero_vendite"]} \n"
                                                            f"Numero retailers coinvolti: "
                                                            f"{info["numero_retailer"]} \n"
                                                            f"NUmero prodotti coinvolti: "
                                                            f"{info["numero_prodotti"]} \n"))

        self._view.update_page()


    # function of the elevated button top5Sales
    def getTopSales(self, e):
        self._view._txtResult.controls.clear()

        # from getTopSales arrives a list of object Sale that is ordered by the attribute revenue
        for sale in self._model.getTopSales(year = self._year, brand = self._brand, retailer = self._retailer):
            self._view._txtResult.controls.append(ft.Text(value = f"data: {sale.Date}; "
                                                                  f"revenue: {sale.ricavo}; "
                                                                  f"retailer: {sale.Retailer_code}; "
        
                                                                  f"product: {sale.Product_number}",))
        # if there aren't sales with the search parameter asked
        if not self._model.getTopSales(year = self._year, brand = self._brand, retailer = self._retailer):
            self._view._txtResult.controls.append(ft.Text(value = "there is no top sales"))

        self._view.update_page()

    # function fills fild of the button
    def fillDDBYear(self):
        # particular option 'filter none'
        self._view._dDBYear.options.append(ft.dropdown.Option(text = "Nessun filtro",
                                                              data = None,
                                                              on_click = self.getTheDataYear))

        # all other option
        for y in self._model.getAllYears():
            self._view._dDBYear.options.append(
                ft.dropdown.Option(key = y, text = y,
                                   data = y, on_click = self.getTheDataYear)
            )

    # function fills fild of the button
    def fillDDBBrand(self):
        # particular option 'filter none'
        self._view._dDBBrand.options.append(ft.dropdown.Option(text = "Nessun filtro",
                                                              data = None,
                                                              on_click = self.getTheDataBrand))

        # all other option
        for brand in self._model.getAllBrands():
            self._view._dDBBrand.options.append(
                ft.dropdown.Option(key = brand, text = brand,
                                   data = brand, on_click = self.getTheDataBrand)
            )

    # function fills fild of the button
    def fillDDBRetailer(self):
        # particular option 'filter none'
        self._view._dDBRetailer.options.append(ft.dropdown.Option(text = "Nessun filtro",
                                                              data = Retailer(name = "Nessuno", type = "",
                                                                              country = "", code = 0) ,
                                                              on_click = self.getTheDataRetailer))

        # all other option
        for retailer in self._model.getAllRetailers():
            self._view._dDBRetailer.options.append(
                ft.dropdown.Option(key = retailer.code, text = retailer.name,
                                   data = retailer, on_click = self.getTheDataRetailer)
            )

    # three function that has to take the info from the dropdown buttons when the event turn out
    def getTheDataYear(self, e):
        self._year = e.control.data

    def getTheDataBrand(self, e):
        self._brand = e.control.data

    def getTheDataRetailer(self, e):
        self._retailer = e.control.data
