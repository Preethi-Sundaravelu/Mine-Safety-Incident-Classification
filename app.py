from src.all_imports import *

app = Flask(__name__)
data = dict()

# model = pickle.load(open('xgb_pkl.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('templates\index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    columns_file_obj = open('src\columns.txt', 'r')
    columns_list = columns_file_obj.read()
    data = {column: request.form.get(column) for column in columns_list}
    columns_file_obj.close()

#     prediction = model.predict(list(data.values()))

if __name__ == '__main__':
    app.run(debug=True, port=8001)
