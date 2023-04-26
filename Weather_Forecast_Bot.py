import time
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cur_file1 = open(r'WeatherData.txt', 'w+')

class WeatherData:

    def __init__(self, city_name, headless=True):
        self.city_name = city_name
        self.PATH = ("C:\Program Files (x86)\chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        
        if headless:
            self.options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=self.options,executable_path= self.PATH)

    def get_weather_data(self, save_to_file=False):

        self.driver.get("https://www.weather.gov/box/")

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "inputstring"))
            )

            time.sleep(2)

            element.click()
            element.send_keys(self.city_name)

            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "btnSearch"))
            )

            time.sleep(2)

            button.click()

            temperature_f = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "myforecast-current-lrg"))
            )
            temperature_c = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "myforecast-current-sm"))
            )
            Detailed_forcast = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "current_conditions_detail"))
            )
            Future_forcast = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "detailed-forecast-body"))
            )

            data = ("The temperature in " + self.city_name + " is " + 
                    temperature_f.text + " or " + temperature_c.text + ".\n\n" + 
                    "Today the day will be: " + Detailed_forcast.text + "\n\n" + 
                    "The future forecast is: " + Future_forcast.text)

            messagebox.showinfo("Weather Data", data)
            
            if save_to_file:
                cur_file1.write(data)

        except:
            error = messagebox.showerror("Error", "An error occurred")

            if save_to_file:
                cur_file1.write(error)

        finally:
            self.driver.quit()


class WeatherApp:

    def __init__(self, master):
        self.master = master
        master.title("Weather Data")
        master.configure(bg='#E5F6F4')

        self.city_label = tk.Label(master, text="City Name or Zip Code: ", 
                                   font=('Arial', 14), bg='#E5F6F4')
        
        self.city_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.city_entry = tk.Entry(master, width=30, font=('Arial', 14))
        self.city_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.headless_var = tk.BooleanVar()
        self.headless_check = tk.Checkbutton(master, text="Windowless", variable=self.headless_var, 
                                            font=('Arial', 14), bg='#E5F6F4')
        
        self.headless_check.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.get_button = tk.Button(master, text="Get Weather Data", command=self.get_weather)
        self.get_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

    def get_weather(self):
        
        city_name = self.city_entry.get()
        headless = self.headless_var.get()
        save_to_file = messagebox.askyesno("Save to File", "Do you want to save the weather data to a file?")
        weather = WeatherData(city_name, headless=headless)
        weather_data = weather.get_weather_data(save_to_file=save_to_file)

        if save_to_file:
            cur_file1.write('\n')

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
cur_file1.close()