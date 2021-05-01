import sys
import logging
import os
import pandas as pd
import streamlit as st
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
 
@app.route('/')
def index():
  url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalEps_01/main/Eponyms4python_Lite.csv'
  df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
  #df2 = df1.sort_values(by=['Eponym'],ascending=True)
  return render_template('02_index.html', title='Main')

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
