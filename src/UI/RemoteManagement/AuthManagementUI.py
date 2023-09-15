import json

import customtkinter

from src.Constants import Constants
from src.UI.RemoteManagement.KeyGenerationFrame import KeyGenerationFrame
from src.UI.RemoteManagement.RemoteManagementFrame import UpdateURL, RemoteManagementFrame


class AuthManagementUI:
    def __init__(self, parent: customtkinter.CTkTabview):
        self.ID = "Remote Management"
        self.parent = parent
        self.parent.tab(self.ID).grid_columnconfigure(index=(0), weight=1)
        self.parent.tab(self.ID).rowconfigure(index=0, weight=1)

        self.keygen_frame = KeyGenerationFrame(self.parent.tab(self.ID))
        self.keygen_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.remote_frame = RemoteManagementFrame(self.parent.tab(self.ID))
        self.remote_frame.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")


