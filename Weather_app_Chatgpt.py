# import requests
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# def get_weather_data(location):
#     url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey=0e6sfPgztPIM3Ui8tkvVJfZi2CV6BCAn"
#     headers = {"accept": "application/json"}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()

#         # Check if location is not found
#         if "code" in data and data["code"] == 404:
#             messagebox.showerror("Error", "Location not found!")
#             return None

#         # Access the values in the JSON data
#         values = data.get('data', {}).get('values', {})

#         # Convert floating-point values to integers
#         temperature = int(values.get('temperature', 0))
#         humidity = int(values.get('humidity', 0))
#         wind_speed = int(values.get('windSpeed', 0))
#         pressure = int(values.get('pressureSurfaceLevel', 0))
#         precipitation = int(values.get('precipitationProbability', 0))

#         return temperature, humidity, wind_speed, pressure, precipitation

#     except requests.RequestException as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")
#         return None

# def update_labels(location):
#     result = get_weather_data(location)
#     if result is not None:
#         temperature, humidity, wind_speed, pressure, precipitation = result

#         # Update labels with new values
#         temLabel.config(text=f"Temperature: {temperature}°C")
#         humidlabel.config(text=f"Humidity: {humidity}%")
#         windlabel.config(text=f"Wind Speed: {wind_speed * 10}km/h")
#         presslabel.config(text=f"Pressure: {pressure}hPa")
#         preciplabel.config(text=f"Precipitation: {precipitation}%")
#     else:
#         clear_labels()

# def clear_labels():
#     # Clear labels if an error occurs
#     temLabel.config(text="Temperature: ")
#     humidlabel.config(text="Humidity: ")
#     windlabel.config(text="Wind Speed: ")
#     presslabel.config(text="Pressure: ")
#     preciplabel.config(text="Precipitation: ")

# def search_location():
#     location = location_var.get().capitalize()
#     update_labels(location)

# root = tk.Tk()
# root.title("Weather Forecast")
# root.iconbitmap("weather_8356649-_1_.ico")
# root.geometry("640x430+50+50")

# location_var = tk.StringVar()

# locational = ttk.Label(root, text="Location:", font=('Arial', 22))
# locational.grid(column=0, row=0, sticky="n")

# Entry = ttk.Entry(root, width=40, textvariable=location_var)
# Entry.grid(column=1, row=0, sticky="w")

# button = ttk.Button(root, text="Search", command=search_location)
# button.grid(column=2, row=0, sticky="w")

# # Labels for displaying weather information
# temLabel = ttk.Label(root, text="Temperature: ", font=('Arial', 24))
# temLabel.grid(column=0, row=1, padx=5, pady=5, sticky='w', ipadx=8, ipady=8)

# humidlabel = ttk.Label(root, text="Humidity: ", font=('Arial', 24))
# humidlabel.grid(column=0, row=2, padx=5, pady=5, sticky='w', ipadx=8, ipady=8)

# windlabel = ttk.Label(root, text="Wind Speed: ", font=('Arial', 24))
# windlabel.grid(column=0, row=3, padx=5, pady=5, sticky='w', ipadx=8, ipady=8)

# presslabel = ttk.Label(root, text="Pressure: ", font=('Arial', 24))
# presslabel.grid(column=0, row=4, padx=5, pady=5, sticky='w', ipadx=8, ipady=8)

# preciplabel = ttk.Label(root, text="Precipitation: ", font=('Arial', 24))
# preciplabel.grid(column=0, row=5, padx=5, pady=5, sticky='w', ipadx=8, ipady=8)

# root.mainloop()











# import requests
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# def get_weather_data(location):
#     url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey=0e6sfPgztPIM3Ui8tkvVJfZi2CV6BCAn"
#     headers = {"accept": "application/json"}

#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
#         data = response.json()

#         # Check if location is not found
#         if "code" in data and data["code"] == 404:
#             messagebox.showerror("Error", "Location not found!")
#             return None

#         # Access the values in the JSON data
#         values = data.get('data', {}).get('values', {})

#         # Convert floating-point values to integers
#         temperature = int(values.get('temperature', 0))
#         humidity = int(values.get('humidity', 0))
#         wind_speed = int(values.get('windSpeed', 0))
#         pressure = int(values.get('pressureSurfaceLevel', 0))
#         precipitation = int(values.get('precipitationProbability', 0))

#         return temperature, humidity, wind_speed, pressure, precipitation

#     except requests.RequestException as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")
#         return None

# def update_labels(location):
#     result = get_weather_data(location)
#     if result is not None:
#         temperature, humidity, wind_speed, pressure, precipitation = result

#         # Update labels with new values
#         temLabel.config(text=f"Temperature: {temperature}°C")
#         humidlabel.config(text=f"Humidity: {humidity}%")
#         windlabel.config(text=f"Wind Speed: {wind_speed * 10}km/h")
#         presslabel.config(text=f"Pressure: {pressure}hPa")
#         preciplabel.config(text=f"Precipitation: {precipitation}%")
#     else:
#         clear_labels()

# def clear_labels():
#     # Clear labels if an error occurs
#     temLabel.config(text="Temperature: ")
#     humidlabel.config(text="Humidity: ")
#     windlabel.config(text="Wind Speed: ")
#     presslabel.config(text="Pressure: ")
#     preciplabel.config(text="Precipitation: ")

# def search_location():
#     location = location_var.get().capitalize()
#     update_labels(location)

# root = tk.Tk()
# root.title("Weather Forecast")
# root.iconbitmap("weather_8356649-_1_.ico")
# root.geometry("640x430+50+50")

# location_var = tk.StringVar()

# style = ttk.Style()
# style.configure('TLabel', font=('Arial', 18), padding=5)
# style.configure('TButton', font=('Arial', 12),)

# locational = ttk.Label(root, text="Location:")
# locational.grid(column=0, row=0, sticky="n", pady=10)

# Entry = ttk.Entry(root, width=40, textvariable=location_var)
# Entry.grid(column=1, row=0, sticky="w", pady=10)

# button = ttk.Button(root, text="Search", command=search_location)
# button.grid(column=2, row=0, sticky="w", pady=10)


# # Labels for displaying weather information
# temLabel = ttk.Label(root, text="Temperature:")
# temLabel.grid(column=0, row=1, padx=5, pady=5, sticky='w')
# humidlabel = ttk.Label(root, text="Humidity:")
# humidlabel.grid(column=0, row=2, padx=5, pady=5, sticky='w')
# windlabel = ttk.Label(root, text="Wind Speed:")
# windlabel.grid(column=0, row=3, padx=5, pady=5, sticky='w')
# presslabel = ttk.Label(root, text="Pressure:")
# presslabel.grid(column=0, row=4, padx=5, pady=5, sticky='w')
# preciplabel = ttk.Label(root, text="Precipitation:")
# preciplabel.grid(column=0, row=5, padx=5, pady=5, sticky='w')

# root.mainloop()
