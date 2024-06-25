
from PIL import Image as im
from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sys
import numpy as np
import imageio
#import imageio.v3 as iio
import ipympl
import matplotlib.pyplot as plt
import skimage as ski
import skimage.feature
import pandas as pd
import scipy.stats as stats
from scipy.stats import entropy
from skimage import feature, measure
from skimage.measure import label, regionprops, regionprops_table
import pyarrow.parquet as pa
import string
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl
import csv
import cv2
import json
from statistics import mode
from statistics import mean
from skimage.io import imread, imshow

#This is the code that belongs to Olorogun Engineer Enoch O. Ejofodomi in his Collaboration with Shell Onward.
#This code also belongs to Engineer Francis Olawuyi in his collaboration with Shell Onward.
#The code also belongs to the following people
#1. GODSWILL OFUALAGBA C.E.O. SWILLAS ENERGY LIMITED.
#2. DR. MICHAEL OLAWUYI
#3. DR. DAMILOLA SUNDAY OLAWUYI
#4. ENGINEER DEBORAH OLAWUYI
#5. ENGINEER JOSHUA OLAWUYI
#6. ENGINEER JOSEPH OLAWUYI
#7. ENGINEER ONOME EJOFODOMI
#8. ENGINEER EFEJERA EJOFODOMI
#9. ENGINEER FRANCIS OLAWUYI
#10. DR. MATTHEW OLAWUYI
#11. ENGINEER ENOCH O. EJOFODOMI
#12. OCHAMUKE EJOFODOMI
#13. ENGINEER ONOME OMIYI
#14. MS. KOME ODU
#15. MR. KAYODE ADEDIPE
#16. MR. OMAFUME EJOFODOMI
#17. MR. NICHOLAS MONYENYE
#18. ENGINEER AYO ADEGITE
#19. ENGINEER ESOSA EHANIRE
#20. Ms. NANAYE INOKOBA
#21. Ms. YINKA OLAREWAJU-ALO
#22. Ms. ERKINAY ABLIZ
#23. Ms. FAEZEH RAZOUYAN
#24. MRS. TEVUKE EJOFODOMI
#25. MR.ONORIODE AGGREH
#26. MS. NDIDI IKEMEFUNA
#27. MS. ENAJITE AGGREH
#28. DR. ESTHER OLAWUYI
#29  MS. ISI OMIYI
#30. DR. JASON ZARA
#31. DR. VESNA ZDERIC
#32. DR. AHMED JENDOUBI
#33. DR. MOHAMMED CHOUIKHA
#34. MS. SHANI ROSS


# JUNE 2, 2024.


#NAME VARIABLES
#Done FUELS SHEET
#Done CARBON EMISSSIONS SHEET


#DATA IS FOR 16 YEARS (2023 - 2038)
Fuel_Type = ["B20" "BioLNG" "Electricity" "HVO" "LNG"]

#YEARLY CARBON EMISSIONS THRESHOLDS FROM 2023 TO 2038 (CO2/Kg)
Yearly_Carbon_Emissions_Threshold = [11677957 10510161 9459145 8513230 7661907 6895716 620145 5585530
                                    5026977 4524279 4071851 3664666 3298199 2968379 2671541 2404387]

#EMISSIONS IS CO2/UNIT FUEL
# LOW TO HIGH - ELECTRICITY, BioLNG, HVO, LNG, B20
Emissions_Per_Unit_Fuel = [3.04858 0.378439 0 0.487624 2.486188]


#FUEL COST IS $/UNIT FUEL
# CHEAP TO HIGH - ELECTRICITY, LNG, BioLNG, B20, HVO
B20FuelCost = [1.220845 1.246802 1.27331 1.300382 1.32803 1.356265 1.385101 1.41455
               1.444625 1.475339 1.506706 1.53874 1.571455 1.604866 1.638987 1.673834]
B20FuelCostUncertainty+- = [0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]

BioLNGFuelCost = [1.087817 1.081461 1.075143 1.068861 1.062616 1.056408 1.050236 1.0441
                  1.038 1.031936 1.025907 1.019913 1.013954 1.00803 1.002141 0.378439]
BioLNGFuelCostUncertainty+- = [0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]

ElectricityFuelCost = [0.191791 0.184113 0.176742 0.169666 0.162873 0.156352 0.150092 0.144083
                       0.138315 0.132778 0.127462 0.122359 0.11746 0.112757 0.108243 0.103909]
ElectricityFuelCostUncertainty+- = [0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]

HVOFuelCost = [1.814314 1.794763 1.775423 1.756291 1.737365 1.718643 1.700123 1.681803
               1.66368 1.645752 1.628018 1.610475 1.593121 1.575954 1.558972 1.542173]
HVOFuelCostUncertainty+- = [0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]

LNGFuelCost = [1.011618 1.005708 0.999832 0.993991 0.988184 0.982411 0.976671 0.970965
               0.965292 0.959652 0.954045 0.948471 0.94293 0.937421 0.931944 0.926499]
LNGFuelCostUncertainty+- = [0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30]


Demand2023_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2023_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2023_3 = [869181 2597094 3292011 414315 995694 1383196 778008 133677 14576 754717 118899 1809 2183475 2431901 1002466 205426]

Demand2024_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2024_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2024_3 = [877242 2716195 3336604 4419981 1043209 1391987 807076 133712 15200 780979 122186 1893 2239440 2453497 1029375 208440]

Demand2025_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2025_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2025_3 = [877707 2836223 3446113 439767 1082065 1410584 821678 137231 15615 791079 123252 1927 21255136 2501227 1053662 218537]

Demand2026_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2026_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2026_3 = [884095 290150 3537030 446478 1090703 1452683 825939 141128 15916 794430 126715 1989 2329773 2524893 1103927 219181]

Demand2027_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2027_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2027_3 = [923004 3023153 3581681 467174 1114957 1480077 862851 146448 16532 829347 129765 2019 2381369 2591566 1137494 224937]

Demand2028_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2028_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2028_3 = [968137 3114155 3731269 469168 1142178 1546703 902415 148036 16863 851953 133929 2066 2448472 2667924 1155329 233462]

Demand2029_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2029_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2029_3 = [1009629 3188349 3892298 484671 1173616 1608555 916617 148322 17544 885863 135803 2113 2497153 2795108 1175528 234155]

Demand2030_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2030_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2030_3 = [1009798 3285854 3959514 496273 1231293 1624238 931478 155565 18168 919290 136344 2114 2518188 2800498 1216569 240767]

Demand2031_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2031_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2031_3 = [1042251 3310718 4061449 518651 1240402 1689196 943472 161977 18747 941960 139696 2198 2619164 2814164 1234148 242813]

Demand2032_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2032_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2032_3 = [1069740 3430934 4237026 542921 1257890 1759215 980430 161977 19298 967461 141391 2230 2708133 2863674 1254261 250479]

Demand2033_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2033_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2033_3 = [1070915 3491886 4290083 563313 1283026 1790314 1007259 168141 19951 1013174 146270 2236 2820991 2974170 1270139 262313]

Demand2034_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2034_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2034_3 = [1080198 3606840 4474763 575445 1344795 1869435 1043936 169472 20807 1057133 146333 2280 2832153 3096840 1320768 273053]

Demand2035_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2035_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2035_3 = [1106719 3746146 4476447 588196 1350533 1934621 1053870 176929 21666 1107787 147590 2369 2908543 3247401 1360337 274741]

Demand2036_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2036_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2036_3 = [1143702 3821393 4599217 602557 1388729 1982301 1103197 180140 22740 1134238 151090 2412 2983351 3269872 1377326 280914]

Demand2037_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2037_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2037_3 = [1196265 3953052 4663966 630092 1402031 2079105 1131832 186733 23254 1146520 156518 2414 3128820 3274991 1384988 292856]

Demand2038_1 = ["S1" "S1" "S1" "S1" "S2" "S2" "S2" "S2" "S4" "S4" "S4" "S4" "S3" "S3" "S3" "S3"]
Demand2038_2 = ["D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4" "D1" "D2" "D3" "D4"]
Demand2038_3 = [1254358 3994169 4847871 642216 1410693 2151804 1187938 190889 23437 1148555 161386 2446 3229278 3297618 1448550 306910]



Car_Cost_Model (Year by Year) = [NO., ID, SIZE, COST OF CAR, YEARLY RANGE, DISTANCE, INSURANCE COST, MAINTENANCE COST, RESALE VALUE, FUEL TYPE, FUEL CONSUMPTION (UNIT_FUEL/KM), FUEL COST, FUEL COST UNCERTAINTY+-%, 
                                 
Vehicle_2023 = [1 BEV_S1_2023 S1 187000 102000 D1 9350 1870 168300 ELECTRICITY 0.893043 0.191791 0]
                                   
Distance_Demand = [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16]
Carbon_Emissions_Threshold = [1 2 3 4 5 6 7 8 9 10 11 12 13 141 5 16]


Vehicle_Size = [1 2 3 4] #[17 44 50 64] TONS
Distance = [1 2 3 4] # UP TO [300 400 500 600] KM DAILY 


mainwindow = tk.Tk()
mainwindow.geometry("1400x700")

            
#Load 362 Images
Imagefile = ["2fpvuk.jpg",  "2otd5q.jpg", "4uhzc7.jpg",
              "4ywofb.jpg", "cgjz2a.jpg", "gp0mak.jpg",
              "jbpvyh.jpg", "n7ozhj.jpg", "ont2xr.jpg",
              "oqr1h3.jpg", "v0t9rk.jpg", "v7dlpt.jpg",
              "vktqud.jpg", "vlridu.jpg", "vyo284.jpg",
              "w7v4b5.jpg", "whvcmt.jpg", "widroh.jpg",
              "wocbyu.jpg", "x4vowt.jpg", "xokfeh.jpg",
              "y0hsj8.jpg", "y3b47k.jpg", "yir071.jpg",
              "zyvdo0.jpg"
             ]

         
#Imagefile2 = ["2fpvuk_pred.npy", "2otd5q_pred.npy", "4uhzc7_pred.npy",
#              "4ywofb_pred.npy", "cgjz2a_pred.npy", "gp0mak_pred.npy",
#              "jbpvyh_pred.npy", "n7ozhj_pred.npy", "ont2xr_pred.npy",
#              "oqr1h3_pred.npy", "v0t9rk_pred.npy", "v7dlpt_pred.npy",
#              "vktqud_pred.npy", "vlridu_pred.npy", "vyo284_pred.npy",
#              "w7v4b5_pred.npy", "whvcmt_pred.npy", "widroh_pred.npy",
#              "wocbyu_pred.npy", "x4vowt_pred.npy", "xokfeh_pred.npy",
#              "y0hsj8_pred.npy", "y3b47k_pred.npy", "yir071_pred.npy",
#              "zyvdo0_pred.npy"
#             ]


for z in range(0,25):
   #Read in Image
   #datab = cv2.imread("jbpvyh.jpg")
   #datab = cv2.imread("yir071.jpg", cv2.IMREAD_UNCHANGED)
   # datab = imageio.v2.imread("w7v4b5.jpg")
   datab = imageio.v2.imread(Imagefile[z])
   img = im.fromarray(datab, mode=None)
   #img = im.fromarray(datab, 'RGB')
  #img.show()

   #Blurs
   datab1 = cv2.medianBlur(datab, 9)  #chosen blur
   #datab2 = cv2.GaussianBlur(datab, (3,3), 0)
   #datab3 = cv2.blur(datab,(5,5))
   #datab4 = cv2.medianBlur(datab,9)
   #datab5 = cv2.bilateralFilter(datab, 9, 75, 75)
   #kernel = np.ones((5,5),np.float32)/25 #blur
   #databbb = cv2.filter2D(databb, -3, kernel)

   #Show Blurred Image
   imgg2 = im.fromarray(datab1, mode=None)
   #imgg2.show()

   #Sharpen Image
   kernel2 = np.array([[0, -1, 0], [-1, 5, -1],[0, -1, 0]]) #sharpen
   databb = cv2.filter2D(datab1, -3, kernel2) #inner value could be -1, -2, or -3

   #Show Sharpened Image
   imgg3 = im.fromarray(databb, mode=None)
   #imgg3.show()   
   
   datac = imageio.imread(Imagefile[z])
  # datad = imageio.imread(Imagefile[z])
   datae = imageio.imread(Imagefile[z])
   dataf = imageio.imread(Imagefile[z])
   datag = imageio.imread(Imagefile[z])
   datah = imageio.imread(Imagefile[z])
   datai = imageio.imread(Imagefile[z])
   dataj = imageio.imread(Imagefile[z])
   datak = imageio.imread(Imagefile[z])
   datal = imageio.imread(Imagefile[z])
   datam = imageio.imread(Imagefile[z])
   datan = imageio.imread(Imagefile[z])
   datao = imageio.imread(Imagefile[z])
   datap = imageio.imread(Imagefile[z])
   dataq = imageio.imread(Imagefile[z])
   datar = imageio.imread(Imagefile[z])
   datas = imageio.imread(Imagefile[z])
   datat = imageio.imread(Imagefile[z])
   datau = imageio.imread(Imagefile[z])
   datav = imageio.imread(Imagefile[z])
   dataw = imageio.imread(Imagefile[z])
   datax = imageio.imread(Imagefile[z])
   datay = imageio.imread(Imagefile[z])
   dataz = imageio.imread(Imagefile[z])
   datafff = imageio.imread(Imagefile[z])



#   datac = imageio.imread("w7v4b5.jpg")
#   datad = imageio.imread("w7v4b5.jpg")
#   datae = imageio.imread("w7v4b5.jpg")
#   img2 = im.fromarray(datae, mode=None)
 #  img = im.fromarray(datab, 'RGB')
#   img2.show()
   
#   dataf = imageio.imread("w7v4b5.jpg")
#   datag = imageio.imread("w7v4b5.jpg")
#   datah = imageio.imread("w7v4b5.jpg")
#   datai = imageio.imread("w7v4b5.jpg")
#   dataj = imageio.imread("w7v4b5.jpg")
#   datak = imageio.imread("w7v4b5.jpg")
#   datal = imageio.imread("w7v4b5.jpg")
#   datam = imageio.imread("w7v4b5.jpg")
#   datan = imageio.imread("w7v4b5.jpg")
#   datao = imageio.imread("w7v4b5.jpg")
#   datap = imageio.imread("w7v4b5.jpg")
#   dataq = imageio.imread("w7v4b5.jpg")
#   datar = imageio.imread("w7v4b5.jpg")
#   datas = imageio.imread("w7v4b5.jpg")
#   datat = imageio.imread("w7v4b5.jpg")
#   datau = imageio.imread("w7v4b5.jpg")
#  datav = imageio.imread("w7v4b5.jpg")
#  dataw = imageio.imread("w7v4b5.jpg")
#   datax = imageio.imread("w7v4b5.jpg")
#  datay = imageio.imread("w7v4b5.jpg")
#   dataz = imageio.imread("w7v4b5.jpg")
#  datafff = imageio.imread("w7v4b5.jpg")



   #datab = cv2.imread(Imagefile[z])
   #datac = cv2.imread(Imagefile[z])
   #datad = cv2.imread(Imagefile[z])
   #datae = cv2.imread(Imagefile[z])
   #dataf = cv2.imread(Imagefile[z])
   #datag = cv2.imread(Imagefile[z])
   #datah = cv2.imread(Imagefile[z])
   #datai = cv2.imread(Imagefile[z])
   #dataj = cv2.imread(Imagefile[z])
   #datak = cv2.imread(Imagefile[z])
   #datal = cv2.imread(Imagefile[z])
   #datam = cv2.imread(Imagefile[z])
   #datan = cv2.imread(Imagefile[z])
   #datao = cv2.imread(Imagefile[z])
   #datap = cv2.imread(Imagefile[z])
   #dataq = cv2.imread(Imagefile[z])
   #datar = cv2.imread(Imagefile[z])
   #datas = cv2.imread(Imagefile[z])
   #datat = cv2.imread(Imagefile[z])
   #datau = cv2.imread(Imagefile[z])
   #datav = cv2.imread(Imagefile[z])
   #dataw = cv2.imread(Imagefile[z])
   #datax = cv2.imread(Imagefile[z])
   #datay = cv2.imread(Imagefile[z])
   #dataz = cv2.imread(Imagefile[z])
   #datafff = cv2.imread(Imagefile[z])

   gray = cv2.cvtColor(databb, cv2.COLOR_BGR2GRAY)
   print(datab)
   print(datab.size)
   print(datab.shape)
   #Display Image
   #img = im.fromarray(datab, 'RGB')
   #img.show()
   #print(gray)
 
   imgtest = databb[160:400,430:700]
   imgtest2 = im.fromarray(imgtest, 'RGB')
   #imgtest2.show()
   print("Img Test: ")

   #ORANGE THRESHOLDING - [255 126  18]
   #YELLOW THRESHOLDING - [255 195  26]
   #BROWN THRESHOLDING - [60 45  4]
   #ORANGE 2-FOLD[156  87  13] [245 131  23]
   #print(imgtest[1,1,:])
   #[118 114 109] [59 44  5] [108 111 118]
   
#print(datab[620,640,:]) #[194 200 229]
#print(imgtest[1,100,:]) [42 248 254][82 83 74]
#DDEEW


#print(datab[120,790,:])
#print(datab[160,790,:])

         
#   for i in range(0,1):
#      data = np.load('4uhzc7_gt.npy',allow_pickle=True)
#      img = im.fromarray(data, 'RGB')
#      print("Test Data")
#      print(data.size)
 #     [a,b] = data.shape
#      print(data)




#   Overlay label on Image
#   data2a = data
#   count12 = 0
#   for i in range(0,a):
#      for j in range(0,b):
 #        if(data[i,j] == 2):
  #          count12 = count12 + 1
            #print(data[i,j])

  # print("count12: ")
  # print(count12)
  # print("DONE")




   #Overlay label on Image
  # data2 = data
   #count = 0
   #for i in range(0,a):
   #   for j in range(0,b):
    #     if(data[i,j] != 0):
     #       data2[i,j] = 255
      #      datac[i,j,:] = 255;
       #     count = count + 1

   #Display Labelled Image
 #  print("Count: ")
 #  print(count)
 #  print(data2)
 #  img2 = im.fromarray(datac, 'RGB')
 #  img2.show()
 

   orange = 0
   yellow = 0
   brown = 0
   gray = 0
   darkgray = 0
   lightgray = 0
   lightgray2 = 0
   lightgray3 = 0



   


   #Color Thresholding for Macerals (Liptinite - Dark Gray/brown,
   # (Vitrinite - Medium to Light Gray) & (Inertinite - White)

   #Color Thresholding for Liptinite - Dark Brown,
   #ORANGE THRESHOLDING - [255 126  18]
   #YELLOW THRESHOLDING - [255 195  26]
   
   [a1,b1,c1] = datab.shape
   print(a1)
   print(b1)
   print(c1)

   datad = np.zeros((a1,b1,3))
   for i in range(0,a1):
      for j in range(0,b1):
         if((datae[i,j,0] > 191) & (datae[i,j,1] < 299)):
            if((datae[i,j,1] > 77) & (datae[i,j,1] < 184)):
               if( ((datae[i,j,2] > 0) & (datae[i,j,2] < 77))):
                  #THRESHOLD ORANGE COLOR 1 [245 131  23]
                  #ADJUSTED THRESHOLD BY ADDING 12
                  #[203 89 0 287 172 65] TO [191 77 0 299 184 77]
                  orange = orange + 1
                  datad[i,j,0] = 255
                  datad[i,j,1] = 255
                  datad[i,j,2] = 255


   for i in range(0,a1):
      for j in range(0,b1):
         if((datae[i,j,0] > 71) & (datae[i,j,0] < 153)):
            if((datae[i,j,1] > 72) & (datae[i,j,1] < 154)):
               if( ((datae[i,j,2] > 77) & (datae[i,j,2] < 159))):
                  #THRESHOLD GRAY COLOR  [112 113 118]
                  #INCREASE GRAY RANGE BY +-20
                  # 91,92,97 TO 133,134,139
                  # ABOVE CHANGED TO 71,72,77 TO 153,154,159
                  gray = gray + 1
                  datad[i,j,0] = 255
                  datad[i,j,1] = 255
                  datad[i,j,2] = 255


   for i in range(0,a1):
      for j in range(0,b1):
         if((datae[i,j,0] > 31) & (datae[i,j,0] < 105)):
            if((datae[i,j,1] > 35) & (datae[i,j,1] < 107)):
               if( ((datae[i,j,2] > 48) & (datae[i,j,2] < 120))):
                  #THRESHOLD DARK GRAY COLOR  [69 71 84]
                  darkgray =  darkgray + 1
                  datad[i,j,0] = 255
                  datad[i,j,1] = 255
                  datad[i,j,2] = 255




   data1 = np.zeros((a1,b1,3))
   for i in range(0,a1):
      for j in range(0,b1):
           if((datad[i,j,0] == 255) & (datad[i,j,1] == 255) & (datad[i,j,2] == 255) ):
              data1[i,j,0] = 255
              data1[i,j,1] = 255
              data1[i,j,2] = 255

          	   
   img3 = im.fromarray(data1, 'RGB')
  # img3.show()
   print("No Color Threshold Image")

 
   #Converge Liptinite Thresholding (Dark Brown) Color Winnowing 1 & 2 into
   # ONE Single Image
   data6 = datai
   for i in range(0,a1):
      for j in range(0,b1):
         if(((data1[i,j,0] == 0) & (data1[i,j,1] == 0) & (data1[i,j,2] == 0))):
              data6[i,j,0] = 0
              data6[i,j,1] = 0
              data6[i,j,2] = 0


   img7 = im.fromarray(data6, 'RGB')
   #img7.show()
   print("Brown Image for Liptinite:")
   


   graytest = cv2.cvtColor(data6, cv2.COLOR_BGR2GRAY)
   #Grayscale Thresholding to extract lines in Test Image
   [d,e] = graytest.shape
   graytest2 = cv2.cvtColor(data6, cv2.COLOR_BGR2GRAY)
   #perform Region Props on Thresholded Test Image
   lineimagecctest = np.array(graytest)
   #Select Pixels Greater than 100 with a mask
   masktest = lineimagecctest > 1
   labelstest = measure.label(masktest)

   #Segment out Regions
   regionstest = measure.regionprops(labelstest, lineimagecctest)
   numlabelstest = len(regionstest)
   regionstest = regionprops_table(labelstest, properties=('area', 'coords'))
   #regionstest = regionprops_table(labelstest, properties=('area', 'perimeter'))
   #print(regions)
   pd.DataFrame(regionstest)
   y = pd.DataFrame(regionstest)
   #Get Shape and Size of Regions
   [a1,b1] = y.shape

   #Select Only Regions Greater than 500 Pixels and Get their Line Count
   linecounttest = 0
   #Array Variable to hold Number of Lines Detected
   TotalRegions = 0
   graytest3 = np.zeros((d,e))
   gray1 = np.zeros((7000,1))
   gray1b = np.zeros((7000,1))
   gray2 = np.zeros((7000,2))
   threshold = np.zeros((d,e))





   one = 0
   two = 0

   for j in range(0,a1):
      if((y.values[j,0] > 500)):#values[j,0] < 20000)):
         gray1[linecounttest,0] = y.values[j,0]
         linecounttest = linecounttest + 1
         gray1b[linecounttest] = j
         #one = y.values[j,1]),1][j,0]
         #two = y.values[int(gray1[0,0]),1][j,1]
         #gray2[linecounttest,0] = one
         #gray2[linecounttest,1] = two

    
   print("linecounttest")
   print(linecounttest)
   #print("one")
   #print(gray2[:,0])
   #print("two:")
   #print(gray2[:,1])



   img8 = im.fromarray(np.uint8(graytest3 * 255), 'L')
   img8.show()
   for m in range(0,linecounttest+1):
      [size1, size2] = y.values[int(gray1b[m]),1].shape
      print("starting")
      print(size1)
      print(size2)
      for p in range(0, size1-1):
      #img8.putpixel((int(y.values[int(gray1b[j]),1][0,0]),int(y.values[int(gray1b[j]),1][0,1])), 200)
         img8.putpixel((int(y.values[int(gray1b[m]),1][p,1]),int(y.values[int(gray1b[m]),1][p,0])), 255)

         #print("starting 2")

   #print(y.values[29,1][0,0])
   #print("Final Image for Liptinite - Dark Brown:")
   img8.show()


   
   #Transposing to right size. Transpose and then Rotate to see Final Image
  # img8.show()
   img9 = img8.transpose(1)
   #img9.show()
   img10 = img9.rotate(-90)
   #img10.show()
   LiptiniteBrown = img8
   [a1,b1,c1] = datab.shape
   FinalImageMacerel = np.zeros((e,d))
   FinalImageMacerelb = np.zeros((d,e))
   FinalImageMacerel2 = img8
   print(a1)
   print(b1)
   print(c1)
   for i in range(0,b1):
      for j in range(0,a1):
         if((LiptiniteBrown.getpixel((i,j)) != 0)):
            FinalImageMacerel2.putpixel((i,j), 255)
            FinalImageMacerel[i,j] = 255
         else:
            FinalImageMacerel2.putpixel((i,j), 0)
            #get value inserted
   print("Final Macerel Image 2:")           
   #imgfinal = im.fromarray(FinalImageMacerel, 'RGB')
   FinalImageMacerel2.show()
   img333 = im.fromarray(FinalImageMacerel)
   #img333.show()
   img334 = img333.rotate(-90)
   #img334.show()
   img335 = img334.transpose(0)
   #img335.show()

   for i in range(0,a1):
      for j in range(0,b1):
         if((img333.getpixel((i,j)) != 0)):
            FinalImageMacerelb[i,j] = 2
            #get value inserted
   
   np.save(Imagefile3[z],FinalImageMacerelb)

      
   colorthresholdcount = [orange, gray, darkgray]
   chosencolorcount = max(colorthresholdcount)
   datad = np.zeros((a1,b1,3))
   if(chosencolorcount == orange):
      print("Orange!")
      for i in range(0,a1):
         for j in range(0,b1):
            if((datae[i,j,0] > 191) & (datae[i,j,1] < 299)):
               if((datae[i,j,1] > 77) & (datae[i,j,1] < 184)):
                  if( ((datae[i,j,2] > 0) & (datae[i,j,2] < 77))):
                     #THRESHOLD ORANGE COLOR 1 [245 131  23]
                     #ADJUSTED THRESHOLD BY ADDING 12
                     #[203 89 0 287 172 65] TO [191 77 0 299 184 77]
                     orange = orange + 1
                     datad[i,j,0] = 255
                     datad[i,j,1] = 255
                     datad[i,j,2] = 255




   if(chosencolorcount == gray):
      print("Gray!")
      for i in range(0,a1):
         for j in range(0,b1):
            if((datae[i,j,0] > 71) & (datae[i,j,0] < 153)):
               if((datae[i,j,1] > 72) & (datae[i,j,1] < 154)):
                  if( ((datae[i,j,2] > 77) & (datae[i,j,2] < 159))):
                  #THRESHOLD GRAY COLOR  [112 113 118]
                     gray = gray + 1
                     datad[i,j,0] = 255
                     datad[i,j,1] = 255
                     datad[i,j,2] = 255



   if(chosencolorcount == darkgray):
      print("Dark Gray!")
      for i in range(0,a1):
         for j in range(0,b1):
            if((datae[i,j,0] > 31) & (datae[i,j,0] < 105)):
               if((datae[i,j,1] > 35) & (datae[i,j,1] < 107)):
                  if( ((datae[i,j,2] > 48) & (datae[i,j,2] < 120))):
                  #THRESHOLD DARK GRAY COLOR  [69 71 84]
                     darkgray =  darkgray + 1
                     datad[i,j,0] = 255
                     datad[i,j,1] = 255
                     datad[i,j,2] = 255



   data1 = np.zeros((a1,b1,3))
   for i in range(0,a1):
      for j in range(0,b1):
           if((datad[i,j,0] == 255) & (datad[i,j,1] == 255) & (datad[i,j,2] == 255) ):
              data1[i,j,0] = 255
              data1[i,j,1] = 255
              data1[i,j,2] = 255

          	   
   img3 = im.fromarray(data1, 'RGB')
   #img3.show()
   print("No Color Threshold Image")

 
   #Converge Liptinite Thresholding (Dark Brown) Color Winnowing 1 & 2 into
   # ONE Single Image
   data6 = datai
   for i in range(0,a1):
      for j in range(0,b1):
         if(((data1[i,j,0] == 0) & (data1[i,j,1] == 0) & (data1[i,j,2] == 0))):
              data6[i,j,0] = 0
              data6[i,j,1] = 0
              data6[i,j,2] = 0


   img7 = im.fromarray(data6, 'RGB')
   #img7.show()
   print("Brown Image for Liptinite 2:")
   print("Color Threshold Selected")



   graytest = cv2.cvtColor(data6, cv2.COLOR_BGR2GRAY)
   #Grayscale Thresholding to extract lines in Test Image
   [d,e] = graytest.shape
   graytest2 = cv2.cvtColor(data6, cv2.COLOR_BGR2GRAY)
   #perform Region Props on Thresholded Test Image
   lineimagecctest = np.array(graytest)
   #Select Pixels Greater than 100 with a mask
   masktest = lineimagecctest > 1
   labelstest = measure.label(masktest)

   #Segment out Regions
   regionstest = measure.regionprops(labelstest, lineimagecctest)
   numlabelstest = len(regionstest)
   regionstest = regionprops_table(labelstest, properties=('area', 'coords'))
   #regionstest = regionprops_table(labelstest, properties=('area', 'perimeter'))
   #print(regions)
   pd.DataFrame(regionstest)
   y = pd.DataFrame(regionstest)
   #Get Shape and Size of Regions
   [a1,b1] = y.shape

   #Select Only Regions Greater than 500 Pixels and Get their Line Count
   linecounttest = 0
   #Array Variable to hold Number of Lines Detected
   TotalRegions = 0
   graytest3 = np.zeros((d,e))
   gray1 = np.zeros((7000,1))
   gray1b = np.zeros((7000,1))
   gray2 = np.zeros((7000,2))
   threshold = np.zeros((d,e))





   one = 0
   two = 0

   for j in range(0,a1):
      if((y.values[j,0] > 500)):#values[j,0] < 20000)):
         gray1[linecounttest,0] = y.values[j,0]
         linecounttest = linecounttest + 1
         gray1b[linecounttest] = j
         #one = y.values[j,1]),1][j,0]
         #two = y.values[int(gray1[0,0]),1][j,1]
         #gray2[linecounttest,0] = one
         #gray2[linecounttest,1] = two

    
   print("linecounttest")
   print(linecounttest)
   #print("one")
   #print(gray2[:,0])
   #print("two:")
   #print(gray2[:,1])



   img8 = im.fromarray(np.uint8(graytest3 * 255), 'L')
   img8.show()
   for m in range(0,linecounttest+1):
      [size1, size2] = y.values[int(gray1b[m]),1].shape
      print("starting")
      print(size1)
      print(size2)
      for p in range(0, size1-1):
      #img8.putpixel((int(y.values[int(gray1b[j]),1][0,0]),int(y.values[int(gray1b[j]),1][0,1])), 200)
         img8.putpixel((int(y.values[int(gray1b[m]),1][p,1]),int(y.values[int(gray1b[m]),1][p,0])), 255)

         #print("starting 2")

   #print(y.values[29,1][0,0])
   print("Final Image for Liptinite - Dark Brown:")
   #img8.show()


   
   #Transposing to right size. Transpose and then Rotate to see Final Image
  # img8.show()
   img9 = img8.transpose(1)
   #img9.show()
   img10 = img9.rotate(-90)
   #img10.show()
   LiptiniteBrown = img8
   [a1,b1,c1] = datab.shape
   FinalImageMacerel = np.zeros((e,d))
   FinalImageMacerelb = np.zeros((d,e))
   FinalImageMacerel2 = img8
   print(a1)
   print(b1)
   print(c1)
   for i in range(0,b1):
      for j in range(0,a1):
         if((LiptiniteBrown.getpixel((i,j)) != 0)):
            FinalImageMacerel2.putpixel((i,j), 255)
            FinalImageMacerel[i,j] = 255
         else:
            FinalImageMacerel2.putpixel((i,j), 0)
            #get value inserted
   print("Final Macerel Image 2:")           
   #imgfinal = im.fromarray(FinalImageMacerel, 'RGB')
   TestImage = FinalImageMacerel2
   TestImage.show()
   #FinalImageMacerel2.show()
   img333 = im.fromarray(FinalImageMacerel)
   #img333.show()
   img334 = img333.rotate(-90)
   #img334.show()
   img335 = img334.transpose(0)
   #img335.show()

   for i in range(0,a1):
      for j in range(0,b1):
         if((img333.getpixel((i,j)) != 0)):
            FinalImageMacerelb[i,j] = 2
            #get value inserted

   
   np.save(Imagefile4[z],FinalImageMacerelb)
