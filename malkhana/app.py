import tkinter as tk
from malkhana.frames.MiscFuncs import MiscFuncs
from malkhana.frames.add_items_frame import AddItemsFrame
# from malkhana.frames.checkin_court_frame import CheckoutCourtFrame
# from malkhana.frames.checkin_frame import CheckinItemFrame
# from malkhana.frames.checkin_fsl_frame import CheckinFSLFrame
from malkhana.frames.checkout_frame import CheckoutItemFrame
# from malkhana.frames.checkout_fsl_frame import CheckoutFSLFrame
# from malkhana.frames.court_records_frame import CourtRecordsFrame
# from malkhana.frames.fsl_records_frame import FSLRecordsFrame
# from malkhana.frames.item_logs_frame import ItemLogsFrame

# from malkhana.frames.print_details_frame import PrintDetailsFrame
# from malkhana.frames.view_items_frame import ViewItemsFrame
from malkhana.frames.login_frame import LoginFrame
from malkhana.frames.main_frame import MainFrame
from malkhana.frames.malkhana_frame import MalkhanaFrame
from malkhana.frames.view_items_frame import ViewItemsFrame


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Malkhana Management System")
        self.state('zoomed')
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Configure the grid system to make sure the frames fill the container
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)

        self.frames = {}
        for F in (LoginFrame, MainFrame, MalkhanaFrame, AddItemsFrame, ViewItemsFrame, CheckoutItemFrame, MiscFuncs):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ViewItemsFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# AddItemsFrame, ViewItemsFrame,  CheckinItemFrame, CheckoutCourtFrame, CheckoutFSLFrame, CheckoutCourtFrame, CheckinFSLFrame, ItemLogsFrame, FSLRecordsFrame, CourtRecordsFrame, MalkhanaFrame, PrintDetailsFrame, MainFrame, LoginFrame
