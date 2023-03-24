from application import app
from flask import render_template, url_for
import pandas as pd
import numpy as np
import json
import plotly
import matplotlib.pyplot as plt
import plotly.express as px


#Uploading files 
File_data_u = np.loadtxt(r"application\static\u.txt")  
File_data_v = np.loadtxt(r"application\static\v.txt")

#Two empty lists 
u=v=[]

#we will loop through all the values to search for nan values and convert them to zeroes, so as to carry 
#on mathemetical operations 
for x in File_data_u:
    if np.isnan(x).any():         #Function to find any if not all nan values
        x = np.nan_to_num(x)
        u.append(x)

for y in File_data_v:
    if np.isnan(y).any():        #Function to find any if not all nan values
        y = np.nan_to_num(y)     #Function that converts nan values to Zeros
        v.append(y)
        
#Matrices for u and v vectors        
mat_u = np.array(u)
mat_v = np.array(v)

#calculating the intensity in knots using the library numpy 
intensity=np.sqrt(mat_u**2+mat_v**2)*1.94


@app.route("/")
def index():
   #Graph One
   fig1=px.bar(intensity,title="Schema of visualization of oceanic currents")
   graph1JSON = json.dumps(fig1,cls=plotly.utils.PlotlyJSONEncoder)  

   #GraphTwo
   fig2=px.histogram(intensity,title="Schema of visualization of oceanic currents")
   graph2JSON = json.dumps(fig2,cls=plotly.utils.PlotlyJSONEncoder)
    
   #GraphThree
   fig3=px.bar(intensity,title="Schema of visualization of oceanic currents")
   fig3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
   graph3JSON = json.dumps(fig3,cls=plotly.utils.PlotlyJSONEncoder) 
   return render_template("index.html", title ="Home", graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON = graph3JSON)