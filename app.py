import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    X = pd.DataFrame(columns=['bath', 'balcony', 'bhk', 'new_total_sqft', 'Alandi Road',
                              'Ambegaon Budruk', 'Anandnagar', 'Aundh', 'Aundh Road', 'Balaji Nagar',
                              'Baner', 'Baner road', 'Bhandarkar Road', 'Bhavani Peth', 'Bibvewadi',
                              'Bopodi', 'Budhwar Peth', 'Bund Garden Road', 'Camp', 'Chandan Nagar',
                              'Dapodi', 'Deccan Gymkhana', 'Dehu Road', 'Dhankawadi', 'Dhayari Phata',
                              'Dhole Patil Road', 'Erandwane', 'Fatima Nagar',
                              'Fergusson College Road', 'Ganesh Peth', 'Ganeshkhind', 'Ghorpade Peth',
                              'Ghorpadi', 'Gokhale Nagar', 'Gultekdi', 'Guruwar peth', 'Hadapsar',
                              'Hadapsar Industrial Estate', 'Hingne Khurd', 'Jangali Maharaj Road',
                              'Kalyani Nagar', 'Karve Nagar', 'Karve Road', 'Kasba Peth', 'Katraj',
                              'Khadaki', 'Khadki', 'Kharadi', 'Kondhwa', 'Kondhwa Budruk',
                              'Kondhwa Khurd', 'Koregaon Park', 'Kothrud', 'Law College Road',
                              'Laxmi Road', 'Lulla Nagar', 'Mahatma Gandhi Road', 'Mangalwar peth',
                              'Manik Bagh', 'Market yard', 'Model colony', 'Mukund Nagar', 'Mundhawa',
                              'Nagar Road', 'Nana Peth', 'Narayan Peth', 'Narayangaon', 'Navi Peth',
                              'Padmavati', 'Parvati Darshan', 'Pashan', 'Paud Road', 'Pirangut',
                              'Prabhat Road', 'Pune Railway Station', 'Rasta Peth', 'Raviwar Peth',
                              'Sadashiv Peth', 'Sahakar Nagar', 'Salunke Vihar', 'Sasson Road',
                              'Satara Road', 'Senapati Bapat Road', 'Shaniwar Peth', 'Shivaji Nagar',
                              'Shukrawar Peth', 'Sinhagad Road', 'Somwar Peth', 'Swargate',
                              'Tilak Road', 'Uruli Devachi', 'Vadgaon Budruk', 'Viman Nagar',
                              'Vishrant Wadi', 'Wadgaon Sheri', 'Wagholi', 'Wakadewadi', 'Wanowrie',
                              'Warje', 'Yerawada', 'Ready To Move', 'Built-up  Area', 'Carpet  Area', 'Plot  Area'])

    data=request.form.values()

    data=list(data)

    bhk=data[0]
    bath=data[1]
    balcony=data[2]
    sqft=data[3]
    location=data[4]
    area_type=data[5]
    availability=data[6]

    loc_index, area_index, avail_index = -1, -1, -1

    if location != 'other':
        loc_index = int(np.where(X.columns == location)[0][0])

    if area_type != 'Super built-up  Area':
        area_index = np.where(X.columns == area_type)[0][0]

    if availability != 'Not Ready':
        avail_index = np.where(X.columns == availability)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = bath
    x[1] = balcony
    x[2] = bhk
    x[3] = sqft

    if loc_index >= 0:
        x[loc_index] = 1
    if area_index >= 0:
        x[area_index] = 1
    if avail_index >= 0:
        x[avail_index] = 1

    output = model.predict([x])
    output = round(output[0], 2)
    return render_template('index.html', prediction_text='House Price will be RS. {} Lacs'.format(output))



if __name__ == "__main__":
    app.run(debug=True)
