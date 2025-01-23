from scrapper import *
from technical import *
import customtkinter
import json
import requests
import concurrent.futures
import gui
from summarize import all_pairs

r = requests.get('https://prash.site/d3d-market-scanner/licence.json')
licence_keys = r.json()


def check_licence():
    try:
        with open('licence.json') as f:
            data = json.load(f)
        if data["key"] in licence_keys["key"]:
            launch_app()
        else:
            register_licence()
    except FileNotFoundError:
        register_licence()


def register_licence():
    register = customtkinter.CTk()
    register.geometry("300x120")
    register.minsize(300, 120)
    register.maxsize(300, 120)
    # register.iconbitmap("logo.ico")
    register.resizable(None, None)
    register.title("Product Registration")

    register.grid_columnconfigure(0, weight=1)
    customtkinter.set_appearance_mode("system")
    entry = customtkinter.CTkEntry(master=register, placeholder_text="Licence key")
    entry.grid(row="0", column="0", padx=20, pady=22, sticky="ew")

    def register_event():
        key = (entry.get())
        if key in licence_keys["key"]:
            json_item = {"key": key}
            json_key = json.dumps(json_item, indent=4)
            with open("licence.json", "w") as outfile:
                outfile.write(json_key)
            register.destroy()
            launch_app()
        else:
            entry.configure(border_color="red")

    button = customtkinter.CTkButton(master=register, text="Activate", command=register_event)
    button.grid(padx=20, pady=10)
    button.grid(row="1", column="0", padx=80, pady=0, sticky="ew")
    register.mainloop()


def launch_app():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in fundamental_urls:
            executor.submit(get_fundamental_data, i)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for j in cot_currency_codes:
            executor.submit(get_cot_data, j)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for k in all_pairs:
            executor.submit(get_technical_data, k)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(get_retail_data)

    print(fundamental_data)
    print(cot_data)
    print(retail_data)
    print(technical_data)
    app = gui.App()
    app.mainloop()


if __name__ == "__main__":
    check_licence()

