from PIL import Image as im
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
import numpy as np
import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import pandas as pd
import string
import openpyxl
import csv
import cv2



#THIS SOFTWARE BELONGS TO AND IS OWNED BY CHIEF ENGINEER OLOROGUN ENOCH O. EJOFODOMI AND ENGINEER  FRANCIS OLAWUYI.
#THIS SOFTWARE IS OWNED BY DR. JASON ZARA, DR. VESNA ZDERIC, ENGINEER FRANCIS OLAWUYI, DR MICHAEL OLAWUYI, DR. MATTHEW OLAWUYI, DR. ESTHER OLAWUYI, DR. AHMED JENDOUBI, DR. MOHAMED  CHOUIKHA, ENGINEER  ENOCH  EJOFODOMI, EFEJERA EJOFODOMI, AND LUCKY EJOFODOMI.
#THIS SOFTWARE IS A FLEET DECARBNONIZATION SOFTWARE THAT ENABLES FLEET OWNERS
#PLAN FOR DECARBONIZATION OVER A DECADE.
#July 6, 2024.

#create main window of the application
mainwindow = tk.Tk()
mainwindow.geometry("1400x700")
mainwindow.title('FLEET DECARBONIZATION SOFTWARE BY OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218')
mainwindow['background']='#7F7FFF'
mainwindow.iconbitmap('companylogo.ico')

global textBox1
global textBox2


def FleetAnalysis():

    global textBox1
    global textBox2
    global textBox3
    global textBox4
    global textBox5
    global textBox6
    global textBox7
    global textBox8
    global textBox9
    global textBox10
    global textBox11
    global textBox12
    global textBox13
    global textBox14
    global textBox15
    global textBox16
    global textBox17
    global textBox18
    global textBox19
    global textBox20
    global textBox21
    global textBox22
    global textBox23
    global textBox24
    global textBox25
    global textBox26
    global textBox27
    global textBox28
    global textBox29
    global textBox30
    global textBox31
    

    data1=(textBox1.get("1.0","end-1c")) #print(length)
    data2=(textBox2.get("1.0","end-1c"))  #print(width)
    data3=(textBox3.get("1.0","end-1c")) #print(length)
    data4=(textBox4.get("1.0","end-1c"))  #print(width)
    data5=(textBox5.get("1.0","end-1c")) #print(length)
    data6=(textBox6.get("1.0","end-1c"))  #print(width)
    data7=(textBox7.get("1.0","end-1c")) #print(length)
    data8=(textBox8.get("1.0","end-1c"))  #print(width)
    data9=(textBox9.get("1.0","end-1c")) #print(length)
    data10=(textBox10.get("1.0","end-1c")) #print(length)
    data11=(textBox11.get("1.0","end-1c"))  #print(width)
    data12=(textBox12.get("1.0","end-1c")) #print(length)
    data13=(textBox13.get("1.0","end-1c"))  #print(width)
    data14=(textBox14.get("1.0","end-1c")) #print(length)
    data15=(textBox15.get("1.0","end-1c"))  #print(width)
    data16=(textBox16.get("1.0","end-1c")) #print(length)
    data17=(textBox17.get("1.0","end-1c"))  #print(width)
    data18=(textBox18.get("1.0","end-1c")) #print(length)
    data19=(textBox19.get("1.0","end-1c")) #print(length)
    data20=(textBox20.get("1.0","end-1c"))  #print(width)
    data21=(textBox21.get("1.0","end-1c")) #print(length)
    data22=(textBox22.get("1.0","end-1c"))  #print(width)
    data23=(textBox23.get("1.0","end-1c")) #print(length)
    data24=(textBox24.get("1.0","end-1c"))  #print(width)
    data25=(textBox25.get("1.0","end-1c")) #print(length)
    data26=(textBox26.get("1.0","end-1c"))  #print(width)
    data27=(textBox27.get("1.0","end-1c")) #print(length)
    data28=(textBox28.get("1.0","end-1c")) #print(length)
    data29=(textBox29.get("1.0","end-1c"))  #print(width)
    data30=(textBox30.get("1.0","end-1c")) #print(length)
    data31=(textBox31.get("1.0","end-1c"))  #print(width)



    if(data1 == ''):
       data1=int(0)
    if(data2 == ''):
       data2=int(0)       
    if(data3 == ''):
       data3=int(0)
    if(data4 == ''):
       data4=int(0)
    if(data5 == ''):
       data5=int(0)       
    if(data6 == ''):
       data6=int(0)
    if(data7 == ''):
       data7=int(0)
    if(data8 == ''):
       data8=int(0)
    if(data9 == ''):
       data9=int(0)       
    if(data10 == ''):
       data10=int(0)
    if(data11 == ''):
       data11=int(0)       
    if(data12 == ''):
       data12=int(0)
    if(data13 == ''):
       data13=int(0)
    if(data14 == ''):
       data14=int(0)       
    if(data15 == ''):
       data15=int(0)
    if(data16 == ''):
       data16=int(0)
    if(data17 == ''):
       data17=int(0)
    if(data18 == ''):
       data18=int(0)
    if(data19 == ''):
       data19=int(0)
    if(data20 == ''):
       data20=int(0)       
    if(data21 == ''):
       data21=int(0)
    if(data22 == ''):
       data22=int(0)
    if(data23 == ''):
       data23=int(0)       
    if(data24 == ''):
       data24=int(0)
    if(data25 == ''):
       data25=int(0)
    if(data26 == ''):
       data26=int(0)
    if(data27 == ''):
       data27=int(0)
    if(data28 == ''):
       data28=int(0)
    if(data29 == ''):
       data29=int(0)
    if(data30 == ''):
       data30=int(0)
    if(data31 == ''):
       data31=int(0)

    print("DeCarbonization Data Fleet:")
    print("DeCarbonization Year:")
    print(data1)
    print(data4)
    print(data7)
    print(data10)
    print(data13)
    print(data16)
    print(data19)
    print(data22)
    print(data25)
    print(data28)

    print("Cars in Fleet")
    print(data2)
    print(data5)
    print(data8)
    print(data11)
    print(data14)
    print(data17)
    print(data20)
    print(data23)
    print(data26)
    print(data29)
          


    print("Distance to Be Travelled")
    print(data3)
    print(data6)
    print(data9)
    print(data12)
    print(data15)
    print(data18)
    print(data21)
    print(data24)
    print(data27)
    print(data30)
          

    InputData = [data2, data3, data5, data6, data8, data9, data11, data12, data14, data15, data17, data18, data20, data21, data23, data24, data26, data27, data29, data30]
    
    print("DeCarbonization Scale")
    print(data31)
    #Costwise Overview: Least to Greatest: ELECTRICITY, LNG, BioLNG, HVO,  B20
    #EMISSIONS IS CO2/UNIT FUEL: Least to Greatest: ELECTRICITY,  BioLNG, HVO, LNG, B20

   # ORDER OF ARRANGEMENT IN VARIABLES - ELECTRICITY, BioLNG, HVO, LNG, B20
    FuelType = ["ELECTRICITY", "LNG", "BIOLNG", "HVO",  "B20"]
    Emissions_Per_Unit_Fuel = [0, 0.378439, 0.487624,  2.486188, 3.04858]
    Cost_Per_Unit_Fuel = [0.143687, 1.042536, 1.6748, 0.9685 , 1.346]
    Consumption_Per_Unit_Fuel = [0.8784, 0.1602896, 0.22269, 0.160842, 0.22269]
    YearCost = np.zeros((5,1))
    YearEmission = np.zeros((5,1))
    for k in range(0,5):
        YearCost[k] = Consumption_Per_Unit_Fuel[k] * Cost_Per_Unit_Fuel[k]
    for k in range(0,5):
        YearEmission[k] = Consumption_Per_Unit_Fuel[k] * Emissions_Per_Unit_Fuel[k]

   
   # YearCost[0] = Consumption_Per_Unit_Fuel[0] * Cost_Per_Unit_Fuel[0]
   # YearCost[1] = Consumption_Per_Unit_Fuel[1] * Cost_Per_Unit_Fuel[1]
   # YearCost[2] = Consumption_Per_Unit_Fuel[2] * Cost_Per_Unit_Fuel[2]
   # YearCost[3] = Consumption_Per_Unit_Fuel[3] * Cost_Per_Unit_Fuel[3]
   # YearCost[4] = Consumption_Per_Unit_Fuel[4] * Cost_Per_Unit_Fuel[4]

    print("YEAR COST:")
    print(YearCost)
    print(InputData)
       
    n = 0
    q = 0
    

    CostPerYear = np.zeros((5,1))
    YearMaxCost = np.zeros((10,1))
    YearMinCost = np.zeros((10,1))
    YearMotorMax = np.zeros((10,1))
    YearMotorMin = np.zeros((10,1))
    EmissionPerYear = np.zeros((5,1))
    YearMaxEmission = np.zeros((10,1))
    YearMinEmission = np.zeros((10,1))
    YearMotorMaxEmission = np.zeros((10,1))
    YearMotorMinEmission = np.zeros((10,1))
    YearDeCarbCost = np.zeros((10,1))
    YearDecarbEmission = np.zeros((10,1))
    DeCarbCost = 0
    DeCarbEmission = np.zeros((5,1))
    OptimizedCost =  np.zeros((10,1))
    OptimizedEmission =  np.zeros((10,1))

    
    ya = 0
    yb = 0


    #COST ASSESSMENT
    for j in range(0,10):
        for m in range(0,5):
            CostPerYear[m] = YearCost[m] * int(InputData[n]) * int(InputData[n+1])
        MaxCost = max(CostPerYear)
        MinCost = min(CostPerYear)
        YearMaxCost[j] = MaxCost
        YearMinCost[j] = MinCost

        #Print out Values:
        print("Consumption Cost for the Year:")
        print(CostPerYear)
        print("Max Cost: ")
        print(MaxCost)
        print("Min Cost: ")
        print(MinCost)
        n= n+2
        print("N:")
        print(n)
        for p in range(0,5):
            if(MaxCost == CostPerYear[p]):
                ya = p
                
            if(MinCost == CostPerYear[p]):
                yb = p
                print(yb)
                
        CostPerYear = np.zeros((5,1))
        YearMotorMin[q]= int(yb)
        YearMotorMax[q]= int(ya)
        q=q+1
       
    print("Max Cost Done:")
    print(YearMaxCost)
    print("Min Cost Done:")
    print(YearMinCost)
    
    print("YearMotorMax:")
    print(YearMotorMax)
    print("YearMotorMin:")
    print(YearMotorMin)


    n = 0
    q = 0
   
    #EMISSIONS ASSESSMENT
    for j in range(0,10):
        for m in range(0,5):
            EmissionPerYear[m] = YearEmission[m] * int(InputData[n]) * int(InputData[n+1])
        MaxEmission = max(EmissionPerYear)
        MinEmission = min(EmissionPerYear)
        YearMaxEmission[j] = MaxEmission
        YearMinEmission[j] = MinEmission

        #Print out Values:
        print("CO2 Emission for the Year:")
        print(EmissionPerYear)
        print("Max Emission: ")
        print(MaxEmission)
        print("Min Emission: ")
        print(MinEmission)
        n= n+2
        print("N:")
        print(n)
        for p in range(0,5):
            if(MaxEmission == EmissionPerYear[p]):
                ya = p
                
            if(MinEmission == EmissionPerYear[p]):
                yb = p
                print(yb)
                
        EmissionPerYear = np.zeros((5,1))
        YearMotorMinEmission[q]= int(yb)
        YearMotorMaxEmission[q]= int(ya)
        q=q+1

    print("Max Emission Done:")
    print(YearMaxEmission)
    print("Min Emission Done:")
    print(YearMinEmission)
    
    print("YearMotorMax Emission:")
    print(YearMotorMaxEmission)
    print("YearMotorMin Emission:")
    print(YearMotorMinEmission)

    yz = 0
    n = 0
    TargetedEmissionReduction = int(0)
    MatchDeCarbEmission = 0
    OptimizedFuelType = ["","","","","","","","","",""]
    
    #DECARBONIZATION SCALE
    for j in range(0,10):
        TargetedEmissionReduction = int(data31) * int(YearMaxEmission[j])
        print("Targeted Emission:" )
        print(TargetedEmissionReduction)
        TargetedEmissionReduction2 = TargetedEmissionReduction/100
        print("Targeted Emission 2:" )
        print(TargetedEmissionReduction2)
        TargetedEmissionReduction3 = int(YearMaxEmission[j]) - TargetedEmissionReduction2
        print("Targeted Emission 3:" )
        print(TargetedEmissionReduction3)
        
        #DeCarbCost = YearMaxCost[j]
        for m in range(0,5):
            EmissionPerYear[m] = YearEmission[m] * int(InputData[n]) * int(InputData[n+1])
            DeCarbEmission[m] = abs(EmissionPerYear[m] - TargetedEmissionReduction3)
            MatchDeCarbEmission = min(DeCarbEmission)
        print("Emission Per Year")
        print(EmissionPerYear)
        print("DeCarbEmission")
        print(DeCarbEmission)
        print("MatchDeCarbEmission")
        print(MatchDeCarbEmission)
        for p in range(0,5):
            if(MatchDeCarbEmission == DeCarbEmission[p]):
                print("found you")
                yz = p
                print(yz)
                if(yz == 0):
                    OptimizedFuelType[j] = "ELECTRICITY"
                if(yz == 1):
                    OptimizedFuelType[j] = "LNG"
                if(yz == 2):
                    OptimizedFuelType[j] = "BIOLNG"
                if(yz == 3):
                    OptimizedFuelType[j] = "HVO"
                if(yz == 4):
                    OptimizedFuelType[j] = "B20"
                   
                                           


        OptimizedCost[j] = YearCost[yz] * int(InputData[n]) * int(InputData[n+1])
        print("Optimized Cost")
        print(OptimizedCost)
        OptimizedEmission[j] = YearEmission[yz] * int(InputData[n]) * int(InputData[n+1])
        print("Optimized Emission")
        print(OptimizedEmission)
        n = n+2
          
        for p in range(0,5):
            if(MatchDeCarbEmission == DeCarbEmission[p]):
                print("found you")
                yz = p
                print(yz)

    print("OptimizedCost")
    print(OptimizedCost)
    print("OptimizedEmission")
    print(OptimizedEmission)
    print("OptimizedFuelType")
    print(OptimizedFuelType)

            
    #RESULTS SO FAR
    # PER YEAR
    #1. Cheapest Car Cost is Electric Vehicles
    #2. Most Expensive Car Cost is HVO
    #3. Lowest Emission is Electric Vehicles
    #4. Highest Emission is B2O


    #PRICE SELECT FROM (LOWEST COST TO HIGHEST)
    #1. ELECTRIC
    #2. LNG
    #3. BioLNG
    #4  B20
    #5. HVO

    #EMISSION SELECT FROM (LOWEST EMISSION TO HIGHEST)
    #1. ELECTRICITY
    #2. BioLNG
    #3. HVO
    #4  LNG
    #5. B20 


    #NEXT FOR TOMORROW
    #Targeted Emission Reduction =
    # Maximum Emission - (DeCarbonization Percentage Chosen
    #(E.g. 10/100 -> 0.1) * Maximum Emmision)
    #Then Find Closest Matching Emission in Yearly Emission
    # from 1 to 5 and then print out its Matching Emission and Cost
    #As the Optimized Value.



    
    #sorted_array = np.sort(array)
    #print("Sorted ascending order:",sorted_array)    
    #create window
    tk3 = Toplevel()
    tk3.geometry("1200x1200")
    tk3.title('FLEET DECARBONIZATION SOFTWARE BY OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218')
    tk3['background']='#36454F'

    #Insert RC14668218 COMPANY LOGO AND EL ELYON
    # Create a canvas widget
    canvas=Canvas(tk3, width=1400, height=100)
    canvas.pack()

    # Load the images of RC14668218 LOGO AND EL ELYON
   # img2=PhotoImage(file="LOGO3.png")
   # lb2 = Label(tk3, image=img2)
   # lb2.img2 = img2 #Save reference to image
   # lb2.place(x=50,y=50)
   # img3=ImageTk.PhotoImage(file="ELELYONC.png")
   # lb3 = Label(tk3, image=img3)
   # lb3.img3 = img3 #Save reference to image
   # lb3.place(x=1320,y=50)


    #Insert RC14668218 UKFLAG AND UK
    # Load the images of RC14668218 UKFLAG AND UK

    img3b=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND4.png")
    lb3b = Label(tk3, image=img3b)
    lb3b.img3b = img3b #Save reference to image
    lb3b.place(x=1,y=50)
    img3c=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND5.png")
    lb3c = Label(tk3, image=img3c)
    lb3c.img3c = img3c #Save reference to image
    lb3c.place(x=1,y=1)



    #Insert RC14668218 COMPANY HEADING

    #lb3b = Label(tk3, image=img3b)
   # lb3b.img3b = img3b #Save reference to image
   # lb3b.place(x=1227,y=1)

    label2 = Label(tk3, text="FLEET DECARBONIZATION SOFTWARE OX1 2JD", width=65, height=1, font=('Monotype Corsiva', 18), bg='#ffffff') 

    label2.place(x=260,y=15)
    label3 = Label(tk3, text="OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218", width=98, height=1, font=('Monotype Corsiva', 11), bg='#ffffff') 
    label3.place(x=257,y=60)

    
    #Create Canvas for RC14668218 Irrigation Layout
   # canvas5=Canvas(tk3,bg='#FFFFFF',width=1100,height=400)
   # canvas5.place(x=50,y=120)
  
    #Create RC14668218 Horizontal and Vertical ScrollBars for Irrigation Layout Section
  #  hbar = Scrollbar(canvas5, orient = HORIZONTAL)
   # hbar.config(command=canvas5.xview)
    #hbar.place(x=1, y=440)
    #canvas5.configure(xscrollcommand=hbar.set)
    #canvas5.config(width=1280,height=455, scrollregion=(10,10,10000,10000))

    #vbar = Scrollbar(canvas5, orient = VERTICAL)
    #vbar.config(command=canvas5.yview)
    #vbar.place(x=1, y=1)
    #canvas5.configure(yscrollcommand=vbar.set)
    #canvas5.config(width=1280,height=455, scrollregion=(10,10,10000,10000))
       

    #INSERT LABEL HEADINGS
    label4 = Label(tk3, text="YEAR", width=8, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label4.place(x=10,y=120)
   
    label5a = Label(tk3, text="TYPE OF FUEL USED", width=18, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label5a.place(x=160,y=120)
 
    
    label9a = Label(tk3, text="OPTIMIZED", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label9a.place(x=490,y=120)
    label9b = Label(tk3, text="COST ($)", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label9b.place(x=490,y=160)

    
    label10a = Label(tk3, text="OPTIMIZED", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label10a.place(x=660,y=120)
    label10b = Label(tk3, text="EMISSION (CO2)", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label10b.place(x=660,y=160)


    #INSERT YEAR VALUES
    label1a = Label(tk3, text=data1, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1a.place(x=15,y=220)
    label1b = Label(tk3, text=data4, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1b.place(x=15,y=260)
    label1c = Label(tk3, text=data7, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1c.place(x=15,y=300)
    label1d = Label(tk3, text=data10, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1d.place(x=15,y=340)
    label1e = Label(tk3, text=data13, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1e.place(x=15,y=380)
    label1f = Label(tk3, text=data16, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1f.place(x=15,y=420)
    label1g = Label(tk3, text=data19, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1g.place(x=15,y=460)
    label1h = Label(tk3, text=data22, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1h.place(x=15,y=500)
    label1i = Label(tk3, text=data25, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1i.place(x=15,y=540)
    label1j = Label(tk3, text=data28, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1j.place(x=15,y=580)

    #INSERT TYPE OF FUEL USED
    label6a = Label(tk3, text=(OptimizedFuelType[0]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6a.place(x=220,y=220)
    label6b = Label(tk3, text=(OptimizedFuelType[1]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6b.place(x=220,y=260)
    label6c = Label(tk3, text=(OptimizedFuelType[2]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6c.place(x=220,y=300)
    label6d = Label(tk3, text=(OptimizedFuelType[3]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6d.place(x=220,y=340)
    label6e = Label(tk3, text=(OptimizedFuelType[4]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6e.place(x=220,y=380)
    label6f = Label(tk3, text=(OptimizedFuelType[5]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6f.place(x=220,y=420)
    label6g = Label(tk3, text=(OptimizedFuelType[6]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6g.place(x=220,y=460)
    label6h = Label(tk3, text=(OptimizedFuelType[7]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6h.place(x=220,y=500)
    label6i = Label(tk3, text=(OptimizedFuelType[8]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6i.place(x=220,y=540)
    label6j = Label(tk3, text=(OptimizedFuelType[9]), width=12, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6j.place(x=220,y=580)


    #INSERT OPTIMIZED COST VALUES
    label6a = Label(tk3, text=int(OptimizedCost[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6a.place(x=500,y=220)
    label6b = Label(tk3, text=int(OptimizedCost[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6b.place(x=500,y=260)
    label6c = Label(tk3, text=int(OptimizedCost[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6c.place(x=500,y=300)
    label6d = Label(tk3, text=int(OptimizedCost[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6d.place(x=500,y=340)
    label6e = Label(tk3, text=int(OptimizedCost[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6e.place(x=500,y=380)
    label6f = Label(tk3, text=int(OptimizedCost[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6f.place(x=500,y=420)
    label6g = Label(tk3, text=int(OptimizedCost[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6g.place(x=500,y=460)
    label6h = Label(tk3, text=int(OptimizedCost[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6h.place(x=500,y=500)
    label6i = Label(tk3, text=int(OptimizedCost[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6i.place(x=500,y=540)
    label6j = Label(tk3, text=int(OptimizedCost[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6j.place(x=500,y=580)



    #INSERT OPTIMIZED EMISSION VALUES
    label7a = Label(tk3, text=int(OptimizedEmission[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7a.place(x=690,y=220)
    label7b = Label(tk3, text=int(OptimizedEmission[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7b.place(x=690,y=260)
    label7c = Label(tk3, text=int(OptimizedEmission[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7c.place(x=690,y=300)
    label7d = Label(tk3, text=int(OptimizedEmission[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7d.place(x=690,y=340)
    label7e = Label(tk3, text=int(OptimizedEmission[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7e.place(x=690,y=380)
    label7f = Label(tk3, text=int(OptimizedEmission[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7f.place(x=690,y=420)
    label7g = Label(tk3, text=int(OptimizedEmission[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7g.place(x=690,y=460)
    label7h = Label(tk3, text=int(OptimizedEmission[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7h.place(x=690,y=500)
    label7i = Label(tk3, text=int(OptimizedEmission[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7i.place(x=690,y=540)
    label7j = Label(tk3, text=int(OptimizedEmission[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7j.place(x=690,y=580)




def OptimizeFleet():

    global textBox1
    global textBox2
    global textBox3
    global textBox4
    global textBox5
    global textBox6
    global textBox7
    global textBox8
    global textBox9
    global textBox10
    global textBox11
    global textBox12
    global textBox13
    global textBox14
    global textBox15
    global textBox16
    global textBox17
    global textBox18
    global textBox19
    global textBox20
    global textBox21
    global textBox22
    global textBox23
    global textBox24
    global textBox25
    global textBox26
    global textBox27
    global textBox28
    global textBox29
    global textBox30
    global textBox31
    

    data1=(textBox1.get("1.0","end-1c")) #print(length)
    data2=(textBox2.get("1.0","end-1c"))  #print(width)
    data3=(textBox3.get("1.0","end-1c")) #print(length)
    data4=(textBox4.get("1.0","end-1c"))  #print(width)
    data5=(textBox5.get("1.0","end-1c")) #print(length)
    data6=(textBox6.get("1.0","end-1c"))  #print(width)
    data7=(textBox7.get("1.0","end-1c")) #print(length)
    data8=(textBox8.get("1.0","end-1c"))  #print(width)
    data9=(textBox9.get("1.0","end-1c")) #print(length)
    data10=(textBox10.get("1.0","end-1c")) #print(length)
    data11=(textBox11.get("1.0","end-1c"))  #print(width)
    data12=(textBox12.get("1.0","end-1c")) #print(length)
    data13=(textBox13.get("1.0","end-1c"))  #print(width)
    data14=(textBox14.get("1.0","end-1c")) #print(length)
    data15=(textBox15.get("1.0","end-1c"))  #print(width)
    data16=(textBox16.get("1.0","end-1c")) #print(length)
    data17=(textBox17.get("1.0","end-1c"))  #print(width)
    data18=(textBox18.get("1.0","end-1c")) #print(length)
    data19=(textBox19.get("1.0","end-1c")) #print(length)
    data20=(textBox20.get("1.0","end-1c"))  #print(width)
    data21=(textBox21.get("1.0","end-1c")) #print(length)
    data22=(textBox22.get("1.0","end-1c"))  #print(width)
    data23=(textBox23.get("1.0","end-1c")) #print(length)
    data24=(textBox24.get("1.0","end-1c"))  #print(width)
    data25=(textBox25.get("1.0","end-1c")) #print(length)
    data26=(textBox26.get("1.0","end-1c"))  #print(width)
    data27=(textBox27.get("1.0","end-1c")) #print(length)
    data28=(textBox28.get("1.0","end-1c")) #print(length)
    data29=(textBox29.get("1.0","end-1c"))  #print(width)
    data30=(textBox30.get("1.0","end-1c")) #print(length)
    data31=(textBox31.get("1.0","end-1c"))  #print(width)



    if(data1 == ''):
       data1=int(0)
    if(data2 == ''):
       data2=int(0)       
    if(data3 == ''):
       data3=int(0)
    if(data4 == ''):
       data4=int(0)
    if(data5 == ''):
       data5=int(0)       
    if(data6 == ''):
       data6=int(0)
    if(data7 == ''):
       data7=int(0)
    if(data8 == ''):
       data8=int(0)
    if(data9 == ''):
       data9=int(0)       
    if(data10 == ''):
       data10=int(0)
    if(data11 == ''):
       data11=int(0)       
    if(data12 == ''):
       data12=int(0)
    if(data13 == ''):
       data13=int(0)
    if(data14 == ''):
       data14=int(0)       
    if(data15 == ''):
       data15=int(0)
    if(data16 == ''):
       data16=int(0)
    if(data17 == ''):
       data17=int(0)
    if(data18 == ''):
       data18=int(0)
    if(data19 == ''):
       data19=int(0)
    if(data20 == ''):
       data20=int(0)       
    if(data21 == ''):
       data21=int(0)
    if(data22 == ''):
       data22=int(0)
    if(data23 == ''):
       data23=int(0)       
    if(data24 == ''):
       data24=int(0)
    if(data25 == ''):
       data25=int(0)
    if(data26 == ''):
       data26=int(0)
    if(data27 == ''):
       data27=int(0)
    if(data28 == ''):
       data28=int(0)
    if(data29 == ''):
       data29=int(0)
    if(data30 == ''):
       data30=int(0)
    if(data31 == ''):
       data31=int(0)

    print("DeCarbonization Data Fleet:")
    print("DeCarbonization Year:")
    print(data1)
    print(data4)
    print(data7)
    print(data10)
    print(data13)
    print(data16)
    print(data19)
    print(data22)
    print(data25)
    print(data28)

    print("Cars in Fleet")
    print(data2)
    print(data5)
    print(data8)
    print(data11)
    print(data14)
    print(data17)
    print(data20)
    print(data23)
    print(data26)
    print(data29)
          


    print("Distance to Be Travelled")
    print(data3)
    print(data6)
    print(data9)
    print(data12)
    print(data15)
    print(data18)
    print(data21)
    print(data24)
    print(data27)
    print(data30)
          

    InputData = [data2, data3, data5, data6, data8, data9, data11, data12, data14, data15, data17, data18, data20, data21, data23, data24, data26, data27, data29, data30]
    
    print("DeCarbonization Scale")
    print(data31)
    #Costwise Overview: Least to Greatest: ELECTRICITY, LNG, BioLNG, HVO,  B20
    #EMISSIONS IS CO2/UNIT FUEL: Least to Greatest: ELECTRICITY,  BioLNG, HVO, LNG, B20
    # ORDER OF ARRANGEMENT IN VARIABLES - ELECTRICITY, BioLNG, HVO, LNG, B20
    Emissions_Per_Unit_Fuel = [0, 0.378439, 0.487624,  2.486188, 3.04858]
    Cost_Per_Unit_Fuel = [0.1436871875, 1.002810125, 1.674804375, 0.968477125, 1.4362398125]
    Consumption_Per_Unit_Fuel = [0.8784, 0.1602896, 0.22269, 0.160842, 0.22269]
    YearCost = np.zeros((5,1))
    YearEmission = np.zeros((5,1))
    for k in range(0,5):
        YearCost[k] = Consumption_Per_Unit_Fuel[k] * Cost_Per_Unit_Fuel[k]
    for k in range(0,5):
        YearEmission[k] = Consumption_Per_Unit_Fuel[k] * Emissions_Per_Unit_Fuel[k]

   
   # YearCost[0] = Consumption_Per_Unit_Fuel[0] * Cost_Per_Unit_Fuel[0]
   # YearCost[1] = Consumption_Per_Unit_Fuel[1] * Cost_Per_Unit_Fuel[1]
   # YearCost[2] = Consumption_Per_Unit_Fuel[2] * Cost_Per_Unit_Fuel[2]
   # YearCost[3] = Consumption_Per_Unit_Fuel[3] * Cost_Per_Unit_Fuel[3]
   # YearCost[4] = Consumption_Per_Unit_Fuel[4] * Cost_Per_Unit_Fuel[4]

    print("YEAR COST:")
    print(YearCost)
    print(InputData)
       
    n = 0
    q = 0
    

    CostPerYear = np.zeros((5,1))
    YearMaxCost = np.zeros((10,1))
    YearMinCost = np.zeros((10,1))
    YearMotorMax = np.zeros((10,1))
    YearMotorMin = np.zeros((10,1))
    EmissionPerYear = np.zeros((5,1))
    YearMaxEmission = np.zeros((10,1))
    YearMinEmission = np.zeros((10,1))
    YearMotorMaxEmission = np.zeros((10,1))
    YearMotorMinEmission = np.zeros((10,1))
    YearDeCarbCost = np.zeros((10,1))
    YearDecarbEmission = np.zeros((10,1))
    DeCarbCost = 0
    DeCarbEmission = np.zeros((5,1))
    OptimizedCost =  np.zeros((10,1))
    OptimizedEmission =  np.zeros((10,1))

    
    ya = 0
    yb = 0


    #COST ASSESSMENT
    for j in range(0,10):
        for m in range(0,5):
            CostPerYear[m] = YearCost[m] * int(InputData[n]) * int(InputData[n+1])
        MaxCost = max(CostPerYear)
        MinCost = min(CostPerYear)
        YearMaxCost[j] = MaxCost
        YearMinCost[j] = MinCost

        #Print out Values:
        print("Consumption Cost for the Year:")
        print(CostPerYear)
        print("Max Cost: ")
        print(MaxCost)
        print("Min Cost: ")
        print(MinCost)
        n= n+2
        print("N:")
        print(n)
        for p in range(0,5):
            if(MaxCost == CostPerYear[p]):
                ya = p
                
            if(MinCost == CostPerYear[p]):
                yb = p
                print(yb)
                
        CostPerYear = np.zeros((5,1))
        YearMotorMin[q]= int(yb)
        YearMotorMax[q]= int(ya)
        q=q+1
       
    print("Max Cost Done:")
    print(YearMaxCost)
    print("Min Cost Done:")
    print(YearMinCost)
    
    print("YearMotorMax:")
    print(YearMotorMax)
    print("YearMotorMin:")
    print(YearMotorMin)

    for k in range(0,5):
        YearCost[k] = Consumption_Per_Unit_Fuel[k] * Cost_Per_Unit_Fuel[k]
    for k in range(0,5):
        YearEmission[k] = Consumption_Per_Unit_Fuel[k] * Emissions_Per_Unit_Fuel[k]


    n = 0
    q = 0
   
    #EMISSIONS ASSESSMENT
    for j in range(0,10):
        for m in range(0,5):
            EmissionPerYear[m] = YearEmission[m] * int(InputData[n]) * int(InputData[n+1])
            CostPerYear[m] = YearCost[m] * int(InputData[n]) * int(InputData[n+1])
        MaxEmission = max(EmissionPerYear)
        MinEmission = min(EmissionPerYear)
        YearMaxEmission[j] = MaxEmission
        YearMinEmission[j] = MinEmission

        #Print out Values:
        print("CO2 Emission for the Year:")
        print(EmissionPerYear)
        print("Max Emission: ")
        print(MaxEmission)
        print("Min Emission: ")
        print(MinEmission)
        n= n+2
        print("N:")
        print(n)
        for p in range(0,5):
            if(MaxEmission == EmissionPerYear[p]):
                ya = p
                
            if(MinEmission == EmissionPerYear[p]):
                yb = p
                print(yb)
                
        EmissionPerYear = np.zeros((5,1))
        YearMotorMinEmission[q]= int(yb)
        YearMotorMaxEmission[q]= int(ya)
        q=q+1

    print("Max Emission Done:")
    print(YearMaxEmission)
    print("Min Emission Done:")
    print(YearMinEmission)
    
    print("YearMotorMax Emission:")
    print(YearMotorMaxEmission)
    print("YearMotorMin Emission:")
    print(YearMotorMinEmission)

    for k in range(0,5):
        YearCost[k] = Consumption_Per_Unit_Fuel[k] * Cost_Per_Unit_Fuel[k]
    for k in range(0,5):
        YearEmission[k] = Consumption_Per_Unit_Fuel[k] * Emissions_Per_Unit_Fuel[k]

    yz = 0
    n = 0
    TargetedEmissionReduction = int(0)
    MatchDeCarbEmission = 0
    
    #DECARBONIZATION SCALE
    for j in range(0,10):
        TargetedEmissionReduction = int(data31) * int(YearMaxEmission[j])
        print("Targeted Emission:" )
        print(TargetedEmissionReduction)
        TargetedEmissionReduction2 = TargetedEmissionReduction/100
        print("Targeted Emission 2:" )
        print(TargetedEmissionReduction2)
        TargetedEmissionReduction3 = int(YearMaxEmission[j]) - TargetedEmissionReduction2
        print("Targeted Emission 3:" )
        print(TargetedEmissionReduction3)
        
        #DeCarbCost = YearMaxCost[j]
        for m in range(0,5):
            CostPerYear[m] = YearCost[m] * int(InputData[n]) * int(InputData[n+1])
            EmissionPerYear[m] = YearEmission[m] * int(InputData[n]) * int(InputData[n+1])
            DeCarbEmission[m] = abs(EmissionPerYear[m] - TargetedEmissionReduction3)
            MatchDeCarbEmission = min(DeCarbEmission)
        print("Emission Per Year")
        print(EmissionPerYear)
        print("DeCarbEmission")
        print(DeCarbEmission)
        print("MatchDeCarbEmission")
        print(MatchDeCarbEmission)
        for p in range(0,5):
            if(MatchDeCarbEmission == DeCarbEmission[p]):
                print("found you")
                yz = p
                print(yz)

        print("YearCost")
        print(YearCost)
        OptimizedCost[j] = YearCost[yz] * int(InputData[n]) * int(InputData[n+1])
        print("Optimized Cost")
        print(OptimizedCost)
        OptimizedEmission[j] = YearEmission[yz] * int(InputData[n]) * int(InputData[n+1])
        print("Optimized Emission")
        print(OptimizedEmission)
        n = n+2
          
    
    print("OptimizedCost")
    print(OptimizedCost)
    print("OptimizedEmission")
    print(OptimizedEmission)
 
            
    #RESULTS SO FAR
    # PER YEAR
    #1. Cheapest Car Cost is Electric Vehicles
    #2. Most Expensive Car Cost is HVO
    #3. Lowest Emission is Electric Vehicles
    #4. Highest Emission is B2O


    #PRICE SELECT FROM (LOWEST COST TO HIGHEST)
    #1. ELECTRIC
    #2. LNG
    #3. BioLNG
    #4  B20
    #5. HVO

    #EMISSION SELECT FROM (LOWEST EMISSION TO HIGHEST)
    #1. ELECTRICITY
    #2. BioLNG
    #3. HVO
    #4  LNG
    #5. B20 


    #NEXT FOR TOMORROW
    #Targeted Emission Reduction =
    # Maximum Emission - (DeCarbonization Percentage Chosen
    #(E.g. 10/100 -> 0.1) * Maximum Emmision)
    #Then Find Closest Matching Emission in Yearly Emission
    # from 1 to 5 and then print out its Matching Emission and Cost
    #As the Optimized Value.



    
    #sorted_array = np.sort(array)
    #print("Sorted ascending order:",sorted_array)    
    #create window
    tk3 = Toplevel()
    tk3.geometry("1200x1200")
    tk3.title('FLEET DECARBONIZATION SOFTWARE BY OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218')
    tk3['background']='#36454F'

    #Insert RC14668218 COMPANY LOGO AND EL ELYON
    # Create a canvas widget
    canvas=Canvas(tk3, width=1400, height=100)
    canvas.pack()

    # Load the images of RC14668218 LOGO AND EL ELYON
   # img2=PhotoImage(file="LOGO3.png")
   # lb2 = Label(tk3, image=img2)
   # lb2.img2 = img2 #Save reference to image
   # lb2.place(x=50,y=50)
   # img3=ImageTk.PhotoImage(file="ELELYONC.png")
   # lb3 = Label(tk3, image=img3)
   # lb3.img3 = img3 #Save reference to image
   # lb3.place(x=1320,y=50)


    #Insert RC14668218 UKFLAG AND UK
    # Load the images of RC14668218 UKFLAG AND UK

    img3b=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND4.png")
    lb3b = Label(tk3, image=img3b)
    lb3b.img3b = img3b #Save reference to image
    lb3b.place(x=1,y=50)
    img3c=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND5.png")
    lb3c = Label(tk3, image=img3c)
    lb3c.img3c = img3c #Save reference to image
    lb3c.place(x=1,y=1)



    #Insert RC14668218 COMPANY HEADING

    #lb3b = Label(tk3, image=img3b)
   # lb3b.img3b = img3b #Save reference to image
   # lb3b.place(x=1227,y=1)

    label2 = Label(tk3, text="FLEET DECARBONIZATION SOFTWARE OX1 2JD", width=65, height=1, font=('Monotype Corsiva', 18), bg='#ffffff') 

    label2.place(x=260,y=15)
    label3 = Label(tk3, text="OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218", width=98, height=1, font=('Monotype Corsiva', 11), bg='#ffffff') 
    label3.place(x=257,y=60)

    
    #Create Canvas for RC14668218 Irrigation Layout
   # canvas5=Canvas(tk3,bg='#FFFFFF',width=1100,height=400)
   # canvas5.place(x=50,y=120)
  
    #Create RC14668218 Horizontal and Vertical ScrollBars for Irrigation Layout Section
  #  hbar = Scrollbar(canvas5, orient = HORIZONTAL)
   # hbar.config(command=canvas5.xview)
    #hbar.place(x=1, y=440)
    #canvas5.configure(xscrollcommand=hbar.set)
    #canvas5.config(width=1280,height=455, scrollregion=(10,10,10000,10000))

    #vbar = Scrollbar(canvas5, orient = VERTICAL)
    #vbar.config(command=canvas5.yview)
    #vbar.place(x=1, y=1)
    #canvas5.configure(yscrollcommand=vbar.set)
    #canvas5.config(width=1280,height=455, scrollregion=(10,10,10000,10000))
       

    #INSERT LABEL HEADINGS
    label4 = Label(tk3, text="YEAR", width=8, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label4.place(x=10,y=120)

    
    label5a = Label(tk3, text="MAXIMUM", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label5a.place(x=160,y=120)
    label5b = Label(tk3, text="COST ($)", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label5b.place(x=160,y=160)
   
    label6a = Label(tk3, text="MAXIMUM", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label6a.place(x=330,y=120)
    label6b = Label(tk3, text="EMISSION (CO2)", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label6b.place(x=330,y=160)


    label7a = Label(tk3, text="MINIMUM", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label7a.place(x=560,y=120)
    label7b = Label(tk3, text="COST ($)", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label7b.place(x=560,y=160)

    
    label8a = Label(tk3, text="MINIMUM", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label8a.place(x=730,y=120)
    label8b = Label(tk3, text="EMISSION (CO2)", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label8b.place(x=730,y=160)


    label9a = Label(tk3, text="OPTIMIZED", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label9a.place(x=960,y=120)
    label9b = Label(tk3, text="COST ($)", width=10, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label9b.place(x=960,y=160)

    
    label10a = Label(tk3, text="OPTIMIZED", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label10a.place(x=1130,y=120)
    label10b = Label(tk3, text="EMISSION (CO2)", width=13, height=1, font=('Arial bold', 18), bg='#ffffff') 
    label10b.place(x=1130,y=160)


    #INSERT YEAR VALUES
    label1a = Label(tk3, text=data1, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1a.place(x=15,y=220)
    label1b = Label(tk3, text=data4, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1b.place(x=15,y=260)
    label1c = Label(tk3, text=data7, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1c.place(x=15,y=300)
    label1d = Label(tk3, text=data10, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1d.place(x=15,y=340)
    label1e = Label(tk3, text=data13, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1e.place(x=15,y=380)
    label1f = Label(tk3, text=data16, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1f.place(x=15,y=420)
    label1g = Label(tk3, text=data19, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1g.place(x=15,y=460)
    label1h = Label(tk3, text=data22, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1h.place(x=15,y=500)
    label1i = Label(tk3, text=data25, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1i.place(x=15,y=540)
    label1j = Label(tk3, text=data28, width=8, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label1j.place(x=15,y=580)

    #INSERT MAXIMUM COST VALUES
    label2a = Label(tk3, text=int(YearMaxCost[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2a.place(x=170,y=220)
    label2b = Label(tk3, text=int(YearMaxCost[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2b.place(x=170,y=260)
    label2c = Label(tk3, text=int(YearMaxCost[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2c.place(x=170,y=300)
    label2d = Label(tk3, text=int(YearMaxCost[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2d.place(x=170,y=340)
    label2e = Label(tk3, text=int(YearMaxCost[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2e.place(x=170,y=380)
    label2f = Label(tk3, text=int(YearMaxCost[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2f.place(x=170,y=420)
    label2g = Label(tk3, text=int(YearMaxCost[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2g.place(x=170,y=460)
    label2h = Label(tk3, text=int(YearMaxCost[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2h.place(x=170,y=500)
    label2i = Label(tk3, text=int(YearMaxCost[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2i.place(x=170,y=540)
    label2j = Label(tk3, text=int(YearMaxCost[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label2j.place(x=170,y=580)


    #INSERT MAXIMUM EMISSION VALUES
    label3a = Label(tk3, text=int(YearMaxEmission[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3a.place(x=360,y=220)
    label3b = Label(tk3, text=int(YearMaxEmission[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3b.place(x=360,y=260)
    label3c = Label(tk3, text=int(YearMaxEmission[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3c.place(x=360,y=300)
    label3d = Label(tk3, text=int(YearMaxEmission[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3d.place(x=360,y=340)
    label3e = Label(tk3, text=int(YearMaxEmission[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3e.place(x=360,y=380)
    label3f = Label(tk3, text=int(YearMaxEmission[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3f.place(x=360,y=420)
    label3g = Label(tk3, text=int(YearMaxEmission[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3g.place(x=360,y=460)
    label3h = Label(tk3, text=int(YearMaxEmission[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3h.place(x=360,y=500)
    label3i = Label(tk3, text=int(YearMaxEmission[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3i.place(x=360,y=540)
    label3j = Label(tk3, text=int(YearMaxEmission[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label3j.place(x=360,y=580)


    #INSERT MINIMUM COST VALUES
    label4a = Label(tk3, text=int(YearMinCost[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4a.place(x=570,y=220)
    label4b = Label(tk3, text=int(YearMinCost[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4b.place(x=570,y=260)
    label4c = Label(tk3, text=int(YearMinCost[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4c.place(x=570,y=300)
    label4d = Label(tk3, text=int(YearMinCost[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4d.place(x=570,y=340)
    label4e = Label(tk3, text=int(YearMinCost[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4e.place(x=570,y=380)
    label4f = Label(tk3, text=int(YearMinCost[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4f.place(x=570,y=420)
    label4g = Label(tk3, text=int(YearMinCost[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4g.place(x=570,y=460)
    label4h = Label(tk3, text=int(YearMinCost[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4h.place(x=570,y=500)
    label4i = Label(tk3, text=int(YearMinCost[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4i.place(x=570,y=540)
    label4j = Label(tk3, text=int(YearMinCost[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label4j.place(x=570,y=580)

    
    #INSERT MINIMUM EMISSION VALUES
    label5a = Label(tk3, text=int(YearMinEmission[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5a.place(x=760,y=220)
    label5b = Label(tk3, text=int(YearMinEmission[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5b.place(x=760,y=260)
    label5c = Label(tk3, text=int(YearMinEmission[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5c.place(x=760,y=300)
    label5d = Label(tk3, text=int(YearMinEmission[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5d.place(x=760,y=340)
    label5e = Label(tk3, text=int(YearMinEmission[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5e.place(x=760,y=380)
    label5f = Label(tk3, text=int(YearMinEmission[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5f.place(x=760,y=420)
    label5g = Label(tk3, text=int(YearMinEmission[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5g.place(x=760,y=460)
    label5h = Label(tk3, text=int(YearMinEmission[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5h.place(x=760,y=500)
    label5i = Label(tk3, text=int(YearMinEmission[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5i.place(x=760,y=540)
    label5j = Label(tk3, text=int(YearMinEmission[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label5j.place(x=760,y=580)



    #INSERT OPTIMIZED COST VALUES
    label6a = Label(tk3, text=int(OptimizedCost[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6a.place(x=970,y=220)
    label6b = Label(tk3, text=int(OptimizedCost[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6b.place(x=970,y=260)
    label6c = Label(tk3, text=int(OptimizedCost[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6c.place(x=970,y=300)
    label6d = Label(tk3, text=int(OptimizedCost[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6d.place(x=970,y=340)
    label6e = Label(tk3, text=int(OptimizedCost[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6e.place(x=970,y=380)
    label6f = Label(tk3, text=int(OptimizedCost[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6f.place(x=970,y=420)
    label6g = Label(tk3, text=int(OptimizedCost[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6g.place(x=970,y=460)
    label6h = Label(tk3, text=int(OptimizedCost[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6h.place(x=970,y=500)
    label6i = Label(tk3, text=int(OptimizedCost[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6i.place(x=970,y=540)
    label6j = Label(tk3, text=int(OptimizedCost[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label6j.place(x=970,y=580)



    #INSERT OPTIMIZED EMISSION VALUES
    label7a = Label(tk3, text=int(OptimizedEmission[0]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7a.place(x=1160,y=220)
    label7b = Label(tk3, text=int(OptimizedEmission[1]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7b.place(x=1160,y=260)
    label7c = Label(tk3, text=int(OptimizedEmission[2]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7c.place(x=1160,y=300)
    label7d = Label(tk3, text=int(OptimizedEmission[3]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7d.place(x=1160,y=340)
    label7e = Label(tk3, text=int(OptimizedEmission[4]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7e.place(x=1160,y=380)
    label7f = Label(tk3, text=int(OptimizedEmission[5]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7f.place(x=1160,y=420)
    label7g = Label(tk3, text=int(OptimizedEmission[6]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7g.place(x=1160,y=460)
    label7h = Label(tk3, text=int(OptimizedEmission[7]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7h.place(x=1160,y=500)
    label7i = Label(tk3, text=int(OptimizedEmission[8]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7i.place(x=1160,y=540)
    label7j = Label(tk3, text=int(OptimizedEmission[9]), width=10, height=1, font=('Arial bold', 16), bg='#ffffff') 
    label7j.place(x=1160,y=580)


    button2 = Button(tk3, text='FLEET ANALYSIS',font=('Arial bold', 32), width=15, height=1, bg='#000080', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa', command=FleetAnalysis)
    button2.place(x=935,y=614)

    #Targeted Emission Reduction =
    # Maximum Emission - (DeCarbonization Percentage Chosen
    #(E.g. 10/100 -> 0.1) * Maximum Emmision)
    #Then Find Closest Matching Emission in Yearly Emission
    # from 1 to 5 and then print out its Matching Emission and Cost
    #As the Optimized Value.





     
    #Insert RC14668218 COMPANY LOGO AND EL ELYON
# Create a canvas widget
canvas=Canvas(mainwindow, width=1400, height=100)
canvas.pack()

# Load the images of RC14668218 LOGO AND EL ELYON
img=ImageTk.PhotoImage(file="COMPANYLOGO.png")
img2=ImageTk.PhotoImage(file="ELELYON.png")
# Add the images to the canvas
canvas.create_image(1, 1, image=img)
canvas.create_image(1320, 50, image=img2)



#Insert RC14668218 UKFLAG AND UK
# Load the images of RC14668218 UKFLAG AND UK
img3=ImageTk.PhotoImage(file="UKFLAG.png")
img4=ImageTk.PhotoImage(file="UKMAP.jpeg")
img5=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND4.png")
img6=ImageTk.PhotoImage(file="MEDSOFTWAREUKN BACKGROUND5.png")
img7=ImageTk.PhotoImage(file="SCALE 3.png")
#img7=ImageTk.PhotoImage(file="ISHI.png")

# Add the images to the canvas
canvas.create_image(200, 50, image=img3)
canvas.create_image(1235, 50, image=img4)
canvas.create_image(680, 50, image=img6)

#ADD ISHI
canvas3=Canvas(mainwindow, width=1400, height=100)
canvas3.place(x=1,y=1)
canvas3.create_image(680, 50, image=img6)
canvas3.create_image(50, 50, image=img)
canvas3.create_image(1320, 50, image=img2)


#Insert RC14668218 COMPANY HEADING
label2 = tk.Label(text="FLEET OPTIMIZATION FOR DECARBONIZATION", width=65, height=1, font=('Monotype Corsiva', 18), bg='#ffffff') 
label2.place(x=260,y=15)
label3 = tk.Label(text="OLAWUYI RACETT NIGERIA LTD., WELLINGTON SQUARE, OXFORD, OX1 2JD, LONDON, UNITED KINGDOM RC14668218", width=98, height=1, font=('Monotype Corsiva', 11), bg='#ffffff') 
label3.place(x=257,y=60)



#CREATE SECOND CANVASS
canvas2=Canvas(mainwindow, width=2500, height=700)
canvas2.place(x=1,y=100)


#ADD CANVASS BACKGROND
canvas2.create_image(670, 300, image=img5)
canvas2.create_image(370, 530, image=img7)

#ADD COMPANY LOGO
#canvas2.create_image(360, 140, image=img)

#canvas2.create_image(100, 400, image=img)
#canvas2.create_image(1320, 50, image=img2)



#create Label and Text Box for PATIENT NAME SEARCH
label4 = tk.Label(text="DeCarbonization Year", width=18, height=1, font=('Arial bold', 20)) 
label4.place(x=20,y=120)
label5 = tk.Label(text="Number of Cars in Fleet ", width=20, height=1, font=('Arial bold', 20)) 
label5.place(x=380,y=120)
label6 = tk.Label(text="Distance to be Traveled (Km)", width=24, height=1, font=('Arial bold', 20)) 
label6.place(x=780,y=120)


textBox1=Text(mainwindow, height=2, width=38)
textBox1.place(x=20,y=180)
textBox2=Text(mainwindow, height=2, width=42)
textBox2.place(x=380,y=180)
textBox3=Text(mainwindow, height=2, width=51)
textBox3.place(x=780,y=180)

textBox4=Text(mainwindow, height=2, width=38)
textBox4.place(x=20,y=220)
textBox5=Text(mainwindow, height=2, width=42)
textBox5.place(x=380,y=220)
textBox6=Text(mainwindow, height=2, width=51)
textBox6.place(x=780,y=220)

textBox7=Text(mainwindow, height=2, width=38)
textBox7.place(x=20,y=260)
textBox8=Text(mainwindow, height=2, width=42)
textBox8.place(x=380,y=260)
textBox9=Text(mainwindow, height=2, width=51)
textBox9.place(x=780,y=260)

textBox10=Text(mainwindow, height=2, width=38)
textBox10.place(x=20,y=300)
textBox11=Text(mainwindow, height=2, width=42)
textBox11.place(x=380,y=300)
textBox12=Text(mainwindow, height=2, width=51)
textBox12.place(x=780,y=300)

textBox13=Text(mainwindow, height=2, width=38)
textBox13.place(x=20,y=340)
textBox14=Text(mainwindow, height=2, width=42)
textBox14.place(x=380,y=340)
textBox15=Text(mainwindow, height=2, width=51)
textBox15.place(x=780,y=340)

textBox16=Text(mainwindow, height=2, width=38)
textBox16.place(x=20,y=380)
textBox17=Text(mainwindow, height=2, width=42)
textBox17.place(x=380,y=380)
textBox18=Text(mainwindow, height=2, width=51)
textBox18.place(x=780,y=380)

textBox19=Text(mainwindow, height=2, width=38)
textBox19.place(x=20,y=420)
textBox20=Text(mainwindow, height=2, width=42)
textBox20.place(x=380,y=420)
textBox21=Text(mainwindow, height=2, width=51)
textBox21.place(x=780,y=420)

textBox22=Text(mainwindow, height=2, width=38)
textBox22.place(x=20,y=460)
textBox23=Text(mainwindow, height=2, width=42)
textBox23.place(x=380,y=460)
textBox24=Text(mainwindow, height=2, width=51)
textBox24.place(x=780,y=460)

textBox25=Text(mainwindow, height=2, width=38)
textBox25.place(x=20,y=500)
textBox26=Text(mainwindow, height=2, width=42)
textBox26.place(x=380,y=500)
textBox27=Text(mainwindow, height=2, width=51)
textBox27.place(x=780,y=500)

textBox28=Text(mainwindow, height=2, width=38)
textBox28.place(x=20,y=540)
textBox29=Text(mainwindow, height=2, width=42)
textBox29.place(x=380,y=540)
textBox30=Text(mainwindow, height=2, width=51)
textBox30.place(x=780,y=540) 



textBox31=Text(mainwindow, height=4, width=10)
textBox31.place(x=280,y=597)
canvas2.create_rectangle(275,493,367,568, outline= "navy", width = 10)

button1 = Button(mainwindow, text='OPTIMIZE FLEET',font=('Arial bold', 36), width=18, height=1, bg='#000080', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa', command=OptimizeFleet)
button1.place(x=750,y=600)

#create Label and BUTTON for ADD NEW PATIENT 
label6 = tk.Label(text="DECARBONIZATION SCALE", width=22, height=1, font=('Arial bold', 14)) 
label6.place(x=188,y=678)



#ADD EL ELYON
#canvas2.create_image(360, 420, image=img2)









mainwindow.mainloop()


#button1 = Button(mainwindow, text='PATIENT SEARCH',font=('Arial bold', 17), width=16, height=1, bg='#000080', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa', command=power_distribution)
