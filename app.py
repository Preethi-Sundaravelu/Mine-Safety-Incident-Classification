from src.all_imports import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates\index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    columns_file_obj = open('src\columns.txt', 'r')
    columns_list = columns_file_obj.read()
    data = {column: request.form.get(column) for column in columns_list}
    columns_file_obj.close()

    encoded_data_for_model_input = label_encoder.fit_transform(list(data.values()))

    prediction = gbnn_model.predict(encoded_data_for_model_input)
    prediction_text = label_encoder.inverse_transform(prediction)
    
    return render_template('templates\index.html', prediction_text = prediction_text)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
