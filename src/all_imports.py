from urllib import response
from flask import Flask, render_template, request
import pickle
import json
from datetime import date, datetime

data = dict()

label_encoder = pickle.load(open('/src/label_encoder.pickle', 'rb'))

gbnn_model = pickle.load(open('/src/gbnn_model.pickle', 'rb'))

output_map_object = open('classification_outputs.txt')