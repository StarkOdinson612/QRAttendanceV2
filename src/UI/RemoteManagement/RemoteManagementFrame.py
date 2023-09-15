import json

import customtkinter

from src.Constants import Constants


class RemoteManagementFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=1, weight=1)

        self.url_update = UpdateURL(self)
        self.url_update.grid(row=0, column=0, padx=10, pady=10, sticky="n")


class UpdateURL(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.id_entry_label = customtkinter.CTkLabel(master=self, text="Enter URL: ")
        self.id_entry_label.grid(row=0, column=0, padx=25, pady=(5, 15))
        self.id_entry = customtkinter.CTkEntry(master=self)
        self.id_entry.grid(row=1, column=0, padx=25)

        self.submit_button = customtkinter.CTkButton(master=self,
                                                     text="Update URL",
                                                     fg_color=Constants.GREEN_COLOR,
                                                     bg_color="transparent",
                                                     hover_color=Constants.GREEN_HOVER_COLOR,
                                                     command=self.submit_event)
        self.submit_button.grid(row=2, column=0, padx=25, pady=(10, 15))

    def submit_event(self):
        url = self.id_entry.get()
        self.id_entry.delete(0, "end")

        temp = {
            "url": url
        }

        with open(Constants.SHEET_INFO_PATH, "w") as f:
            json.dump(temp, f, indent=4)
