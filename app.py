import sys
import logging
import os
import numpy as np
import pandas as pd
import streamlit as st
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
 
@app.route('/')
def index():

  url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
  df = pd.read_csv(url, dtype={'PMID':str,'Year':int})
  df1 = df['Disease'].dropna()
  string = df1.str.cat(sep=',')
  splits = string.split(",")
  S = set(splits)
  T = np.array(list(S)).astype(object)
  U = np.sort(T)
  disease = st.multiselect('Step 1) Choose a disease, sign or symptom:', options=list(U),)

  return render_template('02_index.html', title='main', my_table=disease)

#@app.route('/send_email', methods=['POST'])
#def send_email():
#  params = request.get_json()
#  print("params: ")
#  print(params)
#  hostinfo = {
#    'sysname': os.uname()[0],
#    'nodename': os.uname()[1],
#    'release': os.uname()[2],
#    'version': os.uname()[3],
#    'machine': os.uname()[4]
#  }
#  params['server'] = hostinfo
#  params['remote_addr'] = request.remote_addr
#  return jsonify(params)


if __name__ == "__main__":
  app.run()
