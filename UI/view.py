import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._corso = None
        self._cerca = None
        self._matricola = None
        self.txt_cognome = None
        self._btnStud = None
        self._btnCorso = None
        self._btnIscr = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name

        self._corso = ft.Dropdown(
            label="corso",
            width=550,
            hint_text="Selezionare un corso",
            options=[],
            autofocus=True,
            on_change=self._controller.leggi_corso
        )

        self._controller.populate_dd_corso()

        self._cerca = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.cerca_iscritti,
                                        tooltip="cerca gli iscritti al corso selezionato", width=150)
        row1 = ft.Row([self._corso, self._cerca], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._matricola = ft.TextField(label="matricola", width=200, hint_text="Insert your matricola")

        self.txt_name = ft.TextField(
            label="nome",
            width=300,
            hint_text="Insert your name",
            read_only=True
        )

        self.txt_cognome = ft.TextField(
            label="cognome",
            width=300,
            hint_text="Insert your surname",
            read_only=True
        )

        row2 = ft.Row([self._matricola, self.txt_name, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._btnStud = ft.ElevatedButton(text="Cerca studente",
                                          on_click=self._controller.cerca_studente,
                                          tooltip="Verifica se c'è uno studente con la matricola specificata")

        self._btnCorso = ft.ElevatedButton(text="Cerca corsi",
                                           on_click=self._controller.cerca_corsi,
                                           tooltip="cerca i corsi a cui è iscritto lo studente con la "
                                                   "matricola specificata")

        self._btnIscr = ft.ElevatedButton(text="Iscrivi",
                                          on_click=self._controller.iscrivi,
                                          tooltip="iscritto al corso selezionato lo studente con la "
                                                  "matricola specificata")

        row2 = ft.Row([self._btnStud, self._btnCorso, self._btnIscr], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    @property
    def corso(self):
        return self._corso

    @property
    def matricola(self):
        return self._matricola
