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
               
    pred_input = [0.0]*34

    # Retrieve form values and update pred_input list accordingly
    pred_input[0] = float(request.form.get('document_no'))
    pred_input[1] = float(request.form.get('subunit_cd'))
    pred_input[2] = request.form.get('accident_dt')
    pred_input[3] = float(request.form.get('cal_yr'))
    pred_input[4] = float(request.form.get('cal_qtr'))
    pred_input[5] = float(request.form.get('fiscal_yr'))
    pred_input[6] = float(request.form.get('fiscal_qtr'))
    pred_input[7] = request.form.get('accident_time')
    pred_input[8] = float(request.form.get('degree_injury_cd'))
    pred_input[9] = float(request.form.get('fips_state_cd'))
    pred_input[10] = float(request.form.get('ug_location_cd'))
    pred_input[11] = float(request.form.get('ug_mining_method_cd'))
    pred_input[12] = request.form.get('mining_equip_cd')
    pred_input[13] = request.form.get('equip_mfr_cd')
    pred_input[14] = request.form.get('equip_mfr_name')
    pred_input[15] = request.form.get('shift_begin_time')
    pred_input[16] = request.form.get('accident_type')
    pred_input[17] = float(request.form.get('no_injuries'))
    pred_input[18] = float(request.form.get('tot_exper'))
    pred_input[19] = float(request.form.get('mine_exper'))
    pred_input[20] = float(request.form.get('job_exper'))
    pred_input[21] = request.form.get('occupation_cd')
    pred_input[22] = request.form.get('activity_cd')
    pred_input[23] = request.form.get('injury_source_cd')
    pred_input[24] = request.form.get('nature_injury_cd')
    pred_input[25] = request.form.get('inj_body_part_cd')
    pred_input[26] = float(request.form.get('schedule_charge'))
    pred_input[27] = float(request.form.get('days_restrict'))
    pred_input[28] = float(request.form.get('days_lost'))
    pred_input[29] = request.form.get('trans_term')
    pred_input[30] = request.form.get('return_to_work_dt')
    pred_input[31] = request.form.get('immed_notify_cd')
    pred_input[32] = request.form.get('coal_metal_ind')

    data = np.array([pred_input])

    prediction = model.predict(data)

    if prediction[0] == 1:
        output = "Prediction: Accident/Injury Classified as 'Yes'"
    else:
        output = "Prediction: Accident/Injury Classified as 'No'"

    return render_template('index.html', prediction_text=output)


#     prediction = model.predict(list(data.values()))

if __name__ == '__main__':
    app.run(debug=True, port=8001)
