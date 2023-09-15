import datetime
import json
import os.path

import customtkinter
import csv

from src.CloudUpdate import UpdateSheet
from src.Constants import Constants
from src.UI.Dashboard.MembersFrame import MembersFrame


class KeyGenerationFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.getFromFileText = customtkinter.CTkTextbox(master=self)
        self.getFromFileText.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.getFromFile = customtkinter.CTkButton(master=self,
                                                   text="Update Key",
                                                   fg_color=Constants.BLUE_COLOR,
                                                   bg_color="transparent",
                                                   hover_color=Constants.BLUE_HOVER_COLOR,
                                                   command=self.generate_json)
        self.getFromFile.grid(row=1, column=0, padx=10, pady=10, sticky="sew")

    def generate_json(self):
        f = self.getFromFileText.get("0.0", "end")
        self.getFromFileText.delete("0.0", "end")

        temp = json.loads(f)

        with open(Constants.AUTH_PATH, "w") as f:
            json.dump(temp, f, indent=4)
