import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized.
        # Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._dDBYear = None
        self._dDBBrand = None
        self._dDBRetailer = None
        self._top5Sales = None
        self._infoSales = None
        self._txtResult = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color = "blue", size = 24)
        self._page.controls.append(self._title)

        #ROWS with some controls
        # drop down button for the year
        self._dDBYear = ft.Dropdown(
            label = "year",
            width = 150,
        )
        self._controller.fillDDBYear()

        # drop down button for the brand
        self._dDBBrand = ft.Dropdown(
            label = "brand",
            width = 250,
        )
        self._controller.fillDDBBrand()

        # drop down button for the retailer
        self._dDBRetailer = ft.Dropdown(
            label = "retailer",
            width = 400,
        )
        self._controller.fillDDBRetailer()

        row1 = ft.Row(controls = [self._dDBYear, self._dDBBrand, self._dDBRetailer],
                      alignment = ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # elevated button with the first function
        self._top5Sales = ft.ElevatedButton(text = "Top Sales",
                                            on_click = self._controller.getTopSales)

        # elevated button with the second function
        self._infoSales = ft.ElevatedButton(text = "Salse Info",
                                            on_click = self._controller.getInfoSales)

        row2 = ft.Row(controls = [self._top5Sales, self._infoSales],
                      alignment = ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self._txtResult = ft.ListView(expand = 1, spacing = 10, padding = 20,
                                      auto_scroll = True)
        self._page.controls.append(self._txtResult)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title = ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
