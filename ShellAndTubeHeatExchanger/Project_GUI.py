import tkinter as tk
import numpy as np
import time
import datetime
import getpass
from tkinter import messagebox
import numpy as np

root = tk.Tk()
root.title("Heat exchanger design software")
root.configure(bg="#90afff")
root.geometry("900x600")

#get current date
Dt = datetime.date.today()
 
# - set columns minimal size -

root.columnconfigure(0, minsize=300)
root.columnconfigure(1, minsize=300)
root.columnconfigure(2, minsize=300)
root.columnconfigure(3, minsize=300)
root.columnconfigure(4, minsize=300)
root.columnconfigure(5, minsize=300)


# - header -
lbl1 = tk.Label(root, text="Heat Exchanger", bg="#90afff", fg="black", font=("Times", 40, "bold italic"))
lbl1.grid(column=0, row=0, columnspan=5 , sticky = "nwes")

lbl2 = tk.Label(root, text="design software", bg="#90afff", fg="black", font=("Times", 20, "bold italic"))
lbl2.grid(column=0, row=1, columnspan=5, sticky='nwse')

# - menus -
options1 = ["Choose" , "Shell and tube"]

warm_options = ["Choose" , "Water" , "Organic_solvents" , "Light_oils" , "Heavy_oils" , "Gases" , "Steam" , "Flue" , "Flue_gases" , 
"Dowtherm" , "Aqueous_vapours" , "Organic_vapours" , "Oraganics(some non-condesables" , "Vacuum_condensers"]

cold_options = ["Choose" , "Water" , "Organic_solvents" , "Light_oils" , "Heavy_oils" , "Gases" , "Brine" , "Hydrocarbons_vapours" , 
"Aqueous_solutions" , "Light_organics" , "Heavy_organics"]

options3 = ["Choose" , "Warm fluid" , "Cold fluid"]



#Heat exchanger configuration
var1 = tk.StringVar(root)
var1.set(options1[0])
a1 = tk.OptionMenu(root, var1, *options1 )
a1.grid(column=1, row=2, sticky='we', pady = 10)

a1_label = tk.Label(root , text = "Heat exchanger configuration" , bg="#90afff", fg="black")
a1_label.grid(column=0, row=2, sticky='we', pady = 10)

#warm fluid
var2 = tk.StringVar(root)
var2.set(warm_options[0])
a2 = tk.OptionMenu(root, var2 , *warm_options )
a2.grid(column=1, row=3, sticky='we' , pady = 10)

a2_label = tk.Label(root , text = "Warm fluid" , bg="#90afff", fg="black")
a2_label.grid(column=0, row=3, sticky='we', pady = 10)

#cold fluid
var3 = tk.StringVar(root)
var3.set(cold_options[0])
a3 = tk.OptionMenu(root, var3, *cold_options)
a3.grid(column=1, row=4, sticky='we', pady = 10)

a3_label = tk.Label(root , text = "Cold fluid" , bg="#90afff", fg="black")
a3_label.grid(column=0, row=4, sticky='we', pady = 10)

#Shell_side fluid 
var4 = tk.StringVar(root)
var4.set(options3[0])
a4 = tk.OptionMenu(root, var4, *options3)
a4.grid(column=1, row=5, sticky='we' , pady = 10)

a4_label = tk.Label(root , text = "Shell side fluid" , bg="#90afff", fg="black")
a4_label.grid(column=0, row=5, sticky='we', pady = 10)

#Tube_side fluid 
var5 = tk.StringVar(root)
var5.set(options3[0])
a5 = tk.OptionMenu(root, var5, *options3)
a5.grid(column=1, row=6, sticky='we' , pady = 10)

a5_label = tk.Label(root , text = "Tube side fluid" , bg="#90afff", fg="black")
a5_label.grid(column=0, row=6, sticky='we', pady = 10)

#Heat capacity of the warm fluid
warm_HC = tk.Entry(root , bg = "white" , fg = "black")

warm_HC.grid(column=1, row=7, sticky='we', pady = 10)

warm_HC_label = tk.Label(root , text = "Warm fluid heat capacity[W/(Kg.°C])" , bg="#90afff", fg="black")
warm_HC_label.grid(column=0, row=7, sticky='we', pady = 10)

#Heat capacity of the cold fluid
cold_HC = tk.Entry(root , bg = "white" , fg = "black" )
cold_HC.grid(column=1, row=8, sticky='we', pady = 10)

cold_HC_label = tk.Label(root , text = "cold fluid heat capacity[W/(Kg.°C]" , bg="#90afff", fg="black")
cold_HC_label.grid(column=0, row=8, sticky='we', pady = 10)

#warm Fluid density
warm_density = tk.Entry(root , bg = "white" , fg = "black" )
warm_density.grid(column=1, row=9, sticky='we', pady = 10)

warm_density_label = tk.Label(root , text = "Warm fluid density  [Kg/m^3]" , bg="#90afff", fg="black")
warm_density_label.grid(column=0, row=9, sticky='we', pady = 10)

#ColdFluid density
cold_density = tk.Entry(root , bg = "white" , fg = "black" )
cold_density.grid(column=1, row=10, sticky='we', pady = 10)

cold_density_label = tk.Label(root , text = "cold fluid density  [Kg/m^3]" , bg="#90afff", fg="black")
cold_density_label.grid(column=0, row=10, sticky='we', pady = 10)

#Fouling factor(Shell side)
fouling_shell = tk.Entry(root , bg = "white" , fg = "black" )
fouling_shell.grid(column=1, row=11, sticky='we', pady = 10)

fouling_shell_label = tk.Label(root , text = "Fouling factor(Shell side)" , bg="#90afff", fg="black")
fouling_shell_label.grid(column=0, row=11, sticky='we', pady = 10)

#Fouling factor(Tube side)
fouling_tube = tk.Entry(root , bg = "white" , fg = "black" )
fouling_tube.grid(column=1, row=12, sticky='we', pady = 10)

fouling_tube_label = tk.Label(root , text = "Fouling factor(Tube side)" , bg="#90afff", fg="black")
fouling_tube_label.grid(column=0, row=12, sticky='we', pady = 10)

#Operating pressure value(warm fluid)
warm_operating_pressure = tk.Entry(root , bg = "white" , fg = "black" )
warm_operating_pressure.grid(column=1, row=13, sticky='we', pady = 10)

warm_operating_pressure_label = tk.Label(root , text = "Operating pressure(warm fluid)  [Pa]" , bg="#90afff", fg="black")
warm_operating_pressure_label.grid(column=0, row=13, sticky='we', pady = 10)

#Operating pressure value(cold fluid)
cold_operating_pressure = tk.Entry(root , bg = "white" , fg = "black" )
cold_operating_pressure.grid(column=1, row=14, sticky='we', pady = 10)

cold_operating_pressure_label = tk.Label(root , text = "Operating pressure(cold fluid)  [Pa]" , bg="#90afff", fg="black")
cold_operating_pressure_label.grid(column=0, row=14, sticky='we', pady = 10)

#Maximum allowable pressure drop (Shell side)
allowable_pd_shell = tk.Entry(root , bg = "white" , fg = "black" )
allowable_pd_shell.grid(column=1, row=15, sticky='we', pady = 10)

allowable_pd_shell_label = tk.Label(root , text = "Allowable prssure drop(Shell side) [Pa]" , bg="#90afff", fg="black")
allowable_pd_shell_label.grid(column=0, row=15, sticky='we', pady = 10)

#Maximum allowable pressure drop (Tube side)
allowable_pd_tube = tk.Entry(root , bg = "white" , fg = "black" )
allowable_pd_tube.grid(column=1, row=16, sticky='we', pady = 10)

allowable_pd_tube_label = tk.Label(root , text = "Allowable prssure drop(Tube side) [Pa]" , bg="#90afff", fg="black")
allowable_pd_tube_label.grid(column=0, row=16, sticky='we', pady = 10)

#warm fluid flow rate
warm_flow_rate = tk.Entry(root , bg = "white" , fg = "black" )
warm_flow_rate.grid(column=1, row=17, sticky='we', pady = 10)

warm_flow_rate_label = tk.Label(root , text = "Warm fluid flow rate [Kg/s]" , bg="#90afff", fg="black")
warm_flow_rate_label.grid(column=0, row=17, sticky='we', pady = 10)

#Cold fluid flow rate
cold_flow_rate = tk.Entry(root , bg = "white" , fg = "black" )
cold_flow_rate.grid(column=1, row=18, sticky='we', pady = 10)

cold_flow_rate_label = tk.Label(root , text = "Cold fluid flow rate [Kg/s]" , bg="#90afff", fg="black")
cold_flow_rate_label.grid(column=0, row=18, sticky='we', pady = 10)

#Warm fluid temperature :
warm_initial_temp = tk.Entry(root , bg = "white" , fg = "black")
warm_initial_temp.grid(column=1, row=19, sticky='we', pady = 10)

warm_initial_temp_label = tk.Label(root , text = "Warm fluid initial temperature [°C]" , bg="#90afff", fg="black")
warm_initial_temp_label.grid(column=0, row=19, sticky='we', pady = 10)

warm_final_temp = tk.Entry(root , bg = "white" , fg = "black" )
warm_final_temp.grid(column=3, row=2, sticky='we', pady = 10)

warm_final_temp_label = tk.Label(root , text = "Warm fluid final temperature [°C]" , bg="#90afff", fg="black")
warm_final_temp_label.grid(column=2, row=2, sticky='we', pady = 10)

#Cold fluid temperature
cold_initial_temp = tk.Entry(root , bg = "white" , fg = "black" )
cold_initial_temp.grid(column=3, row=2, sticky='we', pady = 10)

cold_initial_temp_label = tk.Label(root , text = "Cold fluid initial temperature [°C]" , bg="#90afff", fg="black")
cold_initial_temp_label.grid(column=2, row=2, sticky='we' , pady = 10)

#Creating the quit button 
quit_text = tk.StringVar()
quit_button = tk.Button(root , text = "Quit" , command = quit , height = 2 , width = 5)
quit_button.grid(column = 5 , row = 0 , sticky = "we" , ipadx = 50 , padx = 60 , pady = 10)



    
#Creating the Enter button and storing the input data
def func1(*args) :
    HE_configuration_data = var1.get()
    warm_fluid_data = var2.get()
    cold_fluid_data = var3.get()
    shell_side_fluid_data = var4.get()
    Tube_side_fluid_data = var5.get()
    warm_HC_data = warm_HC.get()
    cold_HC_data = cold_HC.get()
    warm_density_data = warm_density.get()
    cold_density_data = cold_density.get()
    fouling_shell_data = fouling_shell.get()
    fouling_tube_data = fouling_tube.get()
    warm_operating_pressure_data = warm_operating_pressure.get()
    cold_operating_pressure_dta = cold_operating_pressure.get()
    warm_flow_rate_data = warm_flow_rate.get()
    cold_flow_rate_data = cold_flow_rate.get()
    allowable_pd_shell_data = allowable_pd_shell.get()
    allowable_pd_tube_data = allowable_pd_tube.get()
    warm_initial_temp_data = warm_initial_temp.get()
    warm_final_temp_data = warm_final_temp.get()
    cold_initial_temp_data = cold_initial_temp.get()


#estimating the overall heat transfer coefficient (U)
def U_approximate() :
    list = [("Organic_solvents","Organic_solvents",100,300) , ("Water","Water",800,1500) ,("Light_oils" , "Light_oils",100,400) , 
    ("Heavy_oils","Heavy_oils",50,300) , ("Gases","Gases",10,50) , ("Organic_solvents","Water",250,750) , ("Light_oils","Water",350,900) , ("Heavy_oils","Water",60,300) , 
    ("Gases","Water",20,300) , ("Organic_solvents","Brine",150,500) , ("Water","Brine",600,1200) , ("Gases","Brine",15,250) , 
    ("Steam","Water",1500,4000) , ("Steam","Organic_solvents",500,1000) , ("Steam","Light_oils",300,900) , ("Steam","Heavy_oils",60,450) , 
    ("Steam","Gases",30,300) , ("Dowtherm","Heavy_oils",50,300) , ("Dowtherm","Gases",20,200) , ("Flue_gases","Steam",30,100) , ("Flue","Hydrocarbon_vapours",30,100) , 
    ("Aqueous_vapours","water",1000,1500) , ("Organic_vapours","Water",700,1000) , ("Oraganics(some non-condesables","water",500,700) , ("Vacuum_condensers","Water",200,500) , 
    ("Steam","Aqueous_solutions",1000,1500) , ("Steam","Light_organics",900,1200) , ("Steam","Heavy_organics",600,900)]
    warm_fluid_data = var2.get()
    cold_fluid_data = var3.get()
    fluids = (warm_fluid_data , cold_fluid_data)
    print(fluids)
  
    for i in list :
        if fluids == (i[0] , i[1]) :
            U = np.random.randint(low = i[2] , high = i[3] , size = (1,))
            print(U)
        elif  fluids != (i[0] , i[1]):
            continue
        else :
            print("ERROR")

enter_button = tk.Button(root , text = "Submit", command = U_approximate , height = 2 , width = 5)
enter_button.grid(column = 2 , row = 20 , sticky = "we" , ipadx = 50 , padx = 60 , pady = 10)


root.mainloop()



