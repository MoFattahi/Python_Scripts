#Designing a shell and tube heat exchanger
# Units : metric


import numpy as np

#Fluid types
warmfluid = input("Warm fluid (tube side fluid): ")
coldfluid = input("Cold fluid (shell side fluid): ")
fluids = (warmfluid , coldfluid)

#fluid properties 

#fluid viscosity

#fluid heat capacity
warm_HC = input("Warm fluid heat capacity: ")
cold_HC = input("Cold fluid heat capacity: ")

#fluid density
while True :
    if warmfluid == coldfluid :
        density = input("Density of the fluid: ")
        break
    else :
        warm_density = input("Density of the warm fluid: ")
        cold_density = input("Density of the cold fluid: ")
        break

#fouling factors(Shell side / Tube side)



#Design pressure values
warm_design_pressure = input("Design pressure of the warm fluid: ")
cold_design_pressure = input("Design pressure of the cold fluid: ")

#Operating pressure values
warm_operating_pressure = input("Operating pressure of the warm fluid: ")
cold_operating_pressure = input("Operating pressure of the cold fluid: ")

#Maximum allowable pressure drop
warm_max_pressure_drop = input("Maximum allowable pressure drop of the warm fluid: ")
cold_max_pressure_drop = input("Maximum allowable pressure drop of the cold fluid: ")

#fluid flow rates 
warm_FR = input("Warm fluid flow rate: ")
cold_FR = input("Cold fluid flow rate: ")

#Temperatures
Warm_initial_T = input("Enter the warm fluid's initial temperature: ")
Warm_final_T = input("Enter the warm fluid's final temperature: ")
cold_initial_T = input("Enter the cold fluid's initial temperature: ")

#estimating the overall heat transfer coefficient (U)
list = [("water","water",800,1500) , ("organic_solvents","organic_solvents",100,300) ,
("light_oils" , "light_oils",100,400) , ("heavy_oils" , "heavy_oils",50,300) , ("gases" , "gases",10,50)]

for i in list :
    if fluids == (i[0] , i[1]) :
        U = np.random.randint(low = i[2] , high = i[3] , size = (1,))
    
#determining the heat transfer rate (W)
Q = (warm_FR) * (warm_HC) * (Warm_initial_T - Warm_final_T)

#determining the final temperature of the cold fluid
cold_final_T = [ (Q / cold_FR) / cold_HC ] + cold_initial_T

#determinig the log mean temperature difference (LMTD)
LMTD = [ (Warm_initial_T - cold_final_T) - (Warm_final_T - cold_initial_T) ] / [ np.log((Warm_initial_T - cold_final_T) / (Warm_final_T - cold_initial_T)) ]

#correction factor (F)


#estimating the heat transfer area required
A = ( Q / U ) / LMTD







