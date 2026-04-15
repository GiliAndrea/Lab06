import flet as ft


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
        pass

    # function of the elevated button top5Sales
    def getTopSales(self, e):
        self._view._txtResult.controls.clear()

        for sale in self._model.getTopSales(year = self._year, brand = self._brand, retailer = self._retailer):
            self._view._txtResult.controls.append(ft.Text(value = sale))

    # function fills fild of the button
    def fillDDBYear(self):
        self._view._dDBYear.options.append(ft.dropdown.Option(text = "Nessun filtro",
                                                              data = None,
                                                              on_click = self.getTheDataYear))

        for y in self._model.getAllYears():
            self._view._dDBYear.options.append(
                ft.dropdown.Option(key = y, text = y,
                                   data = y, on_click = self.getTheDataYear)
            )

    # function fills fild of the button
    def fillDDBBrand(self):
        self._view._dDBBrand.options.append(ft.dropdown.Option(text="Nessun filtro",
                                                              data=None,
                                                              on_click=self.getTheDataBrand))

        for brand in self._model.getAllBrands():
            self._view._dDBBrand.options.append(
                ft.dropdown.Option(key = brand, text = brand,
                                   data = brand, on_click = self.getTheDataBrand)
            )

    # function fills fild of the button
    def fillDDBRetailer(self):
        self._view._dDBRetailer.options.append(ft.dropdown.Option(text="Nessun filtro",
                                                              data=None,
                                                              on_click=self.getTheDataRetailer))

        for retailer in self._model.getAllRetailers():
            self._view._dDBRetailer.options.append(
                ft.dropdown.Option(key = retailer.code, text = retailer,
                                   data = retailer, on_click = self.getTheDataRetailer)
            )

    def getTheDataYear(self, e):
        self._year = e.control.data

    def getTheDataBrand(self, e):
        self._brand = e.control.data

    def getTheDataRetailer(self, e):
        self._retailer = e.control.data
