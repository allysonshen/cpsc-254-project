import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import requests
import json

   
class tkinterApp(tk.Tk):
     
    #__init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        #__init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        #creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        #initializing frames to an empty array
        self.frames = {} 
  
        #iterating through a tuple consisting
        #of the different page layouts
        for F in (StartPage, BMI, Ideal_weight, BMR, food_info):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    #to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
#first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(background='#9B00FF')

        #label of frame 
        label = ttk.Label(self, text ="Fitness Tools and Calculators", font = ("JetBrains Mono", 18), background= '#00FFA2')

        label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan=1)


        caption = ttk.Label(self, text ="Using a fitness calculator is the perfect way to make every\npart of your fitness journey more systematic and successful.\nTry out the calculators below to help reach your health goals!", font = ("JetBrains Mono", 10), background= '#9B00FF')

        caption.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan=1)
         
        #BMI calculator button
        button1 = tk.Button(self,
                font= ("JetBrains Mono", 12), 
                bg='#00FFA2',
                fg='black',
                text='BMI Calculator',
                width=30, command = lambda : controller.show_frame(BMI))
     

        button1.grid(row = 2, column = 0, padx = 10, pady = 10)
  
        #Ideal weight calculator button
        button2 = tk.Button(self, 
                font= ("JetBrains Mono", 12),
                bg='#00FFA2',
                fg='black',
                text='Ideal Weight Calculator',
                width=30, command = lambda : controller.show_frame(Ideal_weight))


        button2.grid(row = 3, column = 0, padx = 10, pady = 10)

        #BMR calculator button
        button3 = tk.Button(self, 
                font= ("JetBrains Mono", 12),
                bg='#00FFA2',
                fg='black',
                text='BMR Calculator',
                width=30, command = lambda : controller.show_frame(BMR))


        button3.grid(row = 4, column = 0, padx = 10, pady = 10)


        #Food Nutrition Information button
        button4 = tk.Button(self, 
                font= ("JetBrains Mono", 12),
                bg='#00FFA2',
                fg='black',
                text='Food Nutrition Information',
                width=30, command = lambda : controller.show_frame(food_info))


        button4.grid(row = 5, column = 0, padx = 10, pady = 10)

  
#second window frame BMI calculator
class BMI(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        self.configure(background='#00B9FF')

        #calculate function
        def calculate_bmi():

            try:
                lb = float(entry_lb.get())
                height = float(entry_height.get())

            #error handling if user types in a non-integer value
            except ValueError:
                tk.messagebox.showinfo("BMI Calculator","Invalid weight or height. Re-enter values")

            #calculations
            bmi = round((lb / (height ** 2) * 703), 1)
            label_result['text'] = f"BMI: {bmi}"

            #pop-up window notifying user of their BMI category
            if bmi < 18.5:
                tk.messagebox.showinfo("BMI Calculator","You fall under the BMI category: Underweight")
            elif bmi >= 18.5 and bmi <25:
                tk.messagebox.showinfo("BMI Calculator","You fall under the BMI category: Normal")
            elif bmi >= 25 and bmi < 30:
                tk.messagebox.showinfo("BMI Calculator","You fall under the BMI category: Overweight")
            elif bmi >= 30:
                tk.messagebox.showinfo("BMI Calculator","You fall under the BMI category: Obese")

        #page label
        label = ttk.Label(self, text ="BMI Calculator", font = ("JetBrains Mono", 18), background= '#00FFA2')
        label.grid(row = 0, column = 3, padx = 5, pady = 5)
  
        #main menu button
        button1 = tk.Button(self, 
                font= ("JetBrains Mono", 10),
                bg='#00FFA2',
                fg='black',
                text='Main Menu',
                width=10, command = lambda : controller.show_frame(StartPage))
     
        button1.grid(row = 0, column = 1, padx = 5)
        
        #page elements
        label_lb = tk.Label(self, text="Weight (lb): ", font = ("JetBrains Mono", 9), background='#00B9FF')
        label_lb.grid(column=2, row=1)

        entry_lb = tk.Entry(self)
        entry_lb.grid(column=3, row=1)

        label_height = tk.Label(self, text="Height (in): ", font = ("JetBrains Mono", 9), background='#00B9FF')
        label_height.grid(column=2, row=2)

        entry_height = tk.Entry(self)
        entry_height.grid(column=3, row=2)

        button_calculate = tk.Button(self, text="Calculate", font = ("JetBrains Mono", 9), command=calculate_bmi, background='#00FFA2')
        button_calculate.grid(column=2, row=3, pady=8)

        label_result = tk.Label(self, text="BMI: ", font = ("JetBrains Mono", 9), background='#00B9FF')
        label_result.grid(column=3, row=3)

        categories = ttk.Label(self, text ="BMI Categories:\nUnderweight: Less than 18.5\nNormal: 18.5-24.9\nOverweight: 25-29.9\nObese: 30 or greater", font = ("JetBrains Mono", 9), background= '#00B9FF')

        categories.grid(column=3, row=4)

        caption = ttk.Label(self, text ="Body mass index (BMI)\nis a measure of body\nfat based on height and\nweight that applies to\nadult men and women.", font = ("JetBrains Mono", 9), background= '#00B9FF')

        caption.grid(column=2, row=4)

        
  
  
#third window frame Ideal Weight calculator
class Ideal_weight(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='#FF0070')

        #value in drop down menu
        value = tk.StringVar(self)

        value.set("Gender")

        #calculate function
        def calculate_ibw():

            try:
                height = float(entry_height.get())

            #error handling if user types in a non-integer value   
            except ValueError:
                tk.messagebox.showinfo("Ideal Weight Calculator","Invalid weight or height. Re-enter values")

            #calculations based on gender
            if value.get() == "Male":
                ibw = round((106+6*(height - 60)), 1)

            elif value.get() == "Female":
                ibw = round((100+5*(height - 60)), 1)
            
            #notify user that a gender is not selected
            else:
                tk.messagebox.showinfo("Ideal Weight Calculator","Gender not selected")

            label_result['text'] = f"Ideal body weight: {ibw}"

        #page label
        label = ttk.Label(self, text ="Ideal Weight Calculator", font = ("JetBrains Mono", 12), background= '#00FFA2')
        label.grid(row = 0, column = 3, padx = 5, pady = 5)
  
        #main menu button
        button1 = tk.Button(self, 
                font= ("JetBrains Mono", 10),
                bg='#00FFA2',
                fg='black',
                text='Main Menu',
                width=10, command = lambda : controller.show_frame(StartPage))
     
        #page elements
        button1.grid(row = 0, column = 1, padx = 5)

        label_height = tk.Label(self, text="Height (in): ", font = ("JetBrains Mono", 9), background='#FF0070')
        label_height.grid(column=2, row=1)

        entry_height = tk.Entry(self)
        entry_height.grid(column=3, row=1)

        button_calculate = tk.Button(self, text="Calculate", font = ("JetBrains Mono", 9), command=calculate_ibw, background='#00FFA2')
        button_calculate.grid(column=2, row=2)


        drop_down = tk.OptionMenu(self, value, *["Male", "Female"],)
        drop_down.config(bg='#00FFA2', activebackground='#00FFA2', width=8, highlightthickness=0, font=("JetBrains Mono", 9))
        drop_down.grid(column=3, row=2, pady=8)

        label_result = tk.Label(self, text="Ideal body weight: ", font = ("JetBrains Mono", 9), background='#FF0070')
        label_result.grid(column=3, row=3)

        categories = ttk.Label(self, text ="Factors can impact\nideal weight such as\nhealth conditions, fat\ndistribution, progency,\netc.", font = ("JetBrains Mono", 9), background= '#FF0070')

        categories.grid(column=3, row=4)

        caption = ttk.Label(self, text ="\nThe Ideal Weight\nCalculator computes\nideal body weight\n(IBW) ranges based\non height, gender,\nand age.", font = ("JetBrains Mono", 9), background= '#FF0070')

        caption.grid(column=2, row=4)

#fourth window frame BMR calculator
class BMR(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        self.configure(background='#FF9B00')

        #value in drop down menu
        value = tk.StringVar(self)

        value.set("Gender")

        #calculate function
        def calculate_bmr():

            try:
                lb = float(entry_lb.get())
                height = float(entry_height.get())
                age = float(entry_age.get())

            #error handling if user types in a non-integer value
            except ValueError:
                tk.messagebox.showinfo("BMR Calculator","Invalid weight, height, or age. Re-enter values")

            #calculations
            if value.get() == "Male":
                bmr = round(66.47+(6.24*lb)+(12.7*height)-(6.755*age))

            elif value.get() == "Female":
                bmr = round((655.1+(4.35*lb)+(4.7*height)-(4.7*age)))
            
            #notify user that a gender is not selected
            else:
                tk.messagebox.showinfo("BMR Calculator","Gender not selected")

            label_result['text'] = f"BMR: {bmr} Calories/day"


        #page label
        label = ttk.Label(self, text ="BMR Calculator", font = ("JetBrains Mono", 18), background= '#00FFA2')
        label.grid(row = 0, column = 3, padx = 5, pady = 5)
  
        #main menu button
        button1 = tk.Button(self, 
                font= ("JetBrains Mono", 10),
                bg='#00FFA2',
                fg='black',
                text='Main Menu',
                width=10, command = lambda : controller.show_frame(StartPage))
     
        button1.grid(row = 0, column = 1, padx = 5)
        
        #page elements
        label_lb = tk.Label(self, text="Weight (lb): ", font = ("JetBrains Mono", 9), background='#FF9B00')
        label_lb.grid(column=2, row=1)

        entry_lb = tk.Entry(self)
        entry_lb.grid(column=3, row=1)

        label_height = tk.Label(self, text="Height (in): ", font = ("JetBrains Mono", 9), background='#FF9B00')
        label_height.grid(column=2, row=2)

        entry_height = tk.Entry(self)
        entry_height.grid(column=3, row=2)

        label_age = tk.Label(self, text="Age: ", font = ("JetBrains Mono", 9), background='#FF9B00')
        label_age.grid(column=2, row=3)

        entry_age = tk.Entry(self)
        entry_age.grid(column=3, row=3)

        button_calculate = tk.Button(self, text="Calculate", font = ("JetBrains Mono", 9), command=calculate_bmr, background='#00FFA2')
        button_calculate.grid(column=2, row=4)

        drop_down = tk.OptionMenu(self, value, *["Male", "Female"],)
        drop_down.config(bg='#00FFA2', activebackground='#00FFA2', width=8, highlightthickness=0, font=("JetBrains Mono", 9))
        drop_down.grid(column=3, row=4, pady=8)

        label_result = tk.Label(self, text="BMR: ", font = ("JetBrains Mono", 9), background='#FF9B00')
        label_result.grid(column=3, row=5)

        categories = ttk.Label(self, text ="An accurate BMR\nmeasurement requires that\na person's sympathetic\nnervous system is\ninactive, which means the\nperson must be completely\nrested.", font = ("JetBrains Mono", 9), background= '#FF9B00')

        categories.grid(column=3, row=6)

        caption = ttk.Label(self, text ="The Basal Metabolic\nRate (BMR) Calculator\nestimates your basal\nmetabolic rate—the\namount of energy\nexpended while at rest\nin a neutrally temperate\nenvironment.", font = ("JetBrains Mono", 9), background= '#FF9B00')

        caption.grid(column=2, row=6)

#fifth window frame Food Nutrtition Information
class food_info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(background='#FF6C6C')

        #function to get food nutrition from API
        def food_lookup():
          
            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            query = entry_food.get()

            #requests from API 
            try:
                response = requests.get(api_url + query, headers={'X-Api-Key': 'wbbghksY4sV+eIy8Olodxg==amgobuAQHlCSseC8'})
                info = json.loads(response.text)
                food = info['items'][0]
                
                #parse nutrition information from JSON 
                calories = food.get('calories')
                servin_sz = food.get('serving_size_g')
                protein = food.get('protein_g')
                fat = food.get('fat_total_g')
                carbs = food.get('carbohydrates_total_g')
                sugar = food.get('sugar_g')

                #display nutiriton information
                servin_sz_info = tk.Label(self, text="Serving Size: {} grams".format(servin_sz), font = ("JetBrains Mono", 9), background='#FF6C6C')
                servin_sz_info.grid(column=2, row=4, pady=5)

                calorie_info = tk.Label(self, text="Calories: {}".format(calories), font = ("JetBrains Mono", 9), background='#FF6C6C')
                calorie_info.grid(column=3, row=4, pady=5)

                protein_info = tk.Label(self, text="Protein: {} grams".format(protein), font = ("JetBrains Mono", 9), background='#FF6C6C')
                protein_info.grid(column=2, row=5, pady=5)

                fat_info = tk.Label(self, text="Total Fat: {} grams".format(fat), font = ("JetBrains Mono", 9), background='#FF6C6C')
                fat_info.grid(column=3, row=5, pady=5)

                carbs_info = tk.Label(self, text="Total Carbohydrate: {} grams".format(carbs), font = ("JetBrains Mono", 9), background='#FF6C6C')
                carbs_info.grid(column=2, row=6, pady=5)

                sugar_info = tk.Label(self, text="Sugar: {} grams".format(sugar), font = ("JetBrains Mono", 9), background='#FF6C6C')
                sugar_info.grid(column=3, row=6, pady=5)


            except:
                error_message = "Error:", response.status_code, response.text

                #throw error if food does not exist
                if str(error_message) != "('Error:', 400, 'Invalid API Key.')":
                    tk.messagebox.showinfo("Food Nutrtition Information","Food not found")
                else:
                    print("Invalid API key")



        #page label
        label = ttk.Label(self, text ="Food Nutrition Information", font = ("JetBrains Mono", 12), background= '#00FFA2')
        label.grid(row = 0, column = 3, padx = 5, pady = 5)
  
        #main menu button
        button1 = tk.Button(self, 
                font= ("JetBrains Mono", 10),
                bg='#00FFA2',
                fg='black',
                text='Main Menu',
                width=10, command = lambda : controller.show_frame(StartPage))
     
        #page elements
        button1.grid(row = 0, column = 1, padx = 5)

        caption = ttk.Label(self, text ="Search for food items\nto find their nutrition\ninformation!", font = ("JetBrains Mono", 9), background= '#FF6C6C')

        caption.grid(column=3, row=1, pady = 10)

        label_food = tk.Label(self, text="Enter a food item: ", font = ("JetBrains Mono", 9), background='#FF6C6C')
        label_food.grid(column=2, row=2, pady=5)

        entry_food = tk.Entry(self)
        entry_food.grid(column=3, row=2)


        search_button = tk.Button(self, text="Search", font = ("JetBrains Mono", 9), command=food_lookup, background='#00FFA2')
        search_button.grid(column=3, row=3,pady=10)




# Driver Code
app = tkinterApp()
app.mainloop()