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

    encoded_data_for_model_input = label_encoder.fit_transform(list(data.values()))

    prediction = gbnn_model.predict(encoded_data_for_model_input)
    prediction_text = label_encoder.inverse_transform(prediction)





        # try:
        # # Extract form data
        # document_no = request.form['document_no']
        # subunit_cd = request.form['subunit_cd']
        # accident_dt = request.form['accident_dt']
        # coal_metal_ind = request.form['coal_metal_ind']
        # cal_yr = request.form['cal_yr']
        # cal_qtr = request.form['cal_qtr']
        # fiscal_yr = request.form['fiscal_yr']
        # fiscal_qtr = request.form['fiscal_qtr']
        # accident_time = request.form['accident_time']
        # degree_injury_cd = request.form['degree_injury_cd']
        # fips_state_cd = request.form['fips_state_cd']
        # ug_location_cd = request.form['ug_location_cd']
        # ug_mining_method_cd = request.form['ug_mining_method_cd']
        # mining_equip_cd = request.form['mining_equip_cd']
        # equip_mfr_cd = request.form['equip_mfr_cd']
        # equip_mfr_name = request.form['equip_mfr_name']
        # shift_begin_time = request.form['shift_begin_time']
        # accident_type = request.form['accident_type']
        # no_injuries = request.form['no_injuries']
        # tot_exper = request.form['tot_exper']
        # mine_exper = request.form['mine_exper']
        # job_exper = request.form['job_exper']
        # occupation_cd = request.form['occupation_cd']
        # activity_cd = request.form['activity_cd']
        # injury_source_cd = request.form['injury_source_cd']
        # nature_injury_cd = request.form['nature_injury_cd']
        # inj_body_part_cd = request.form['inj_body_part_cd']
        # schedule_charge = request.form['schedule_charge']
        # days_restrict = request.form['days_restrict']
        # days_lost = request.form['days_lost']
        # trans_term = request.form['trans_term']
        # return_to_work_dt = request.form['return_to_work_dt']
        # immed_notify_cd = request.form['immed_notify_cd']

        # # Create an input dictionary for the model
        # input_data = {
        #     'document_no': document_no,
        #     'subunit_cd': subunit_cd,
        #     'accident_dt': accident_dt,
        #     'coal_metal_ind': coal_metal_ind,
        #     'cal_yr': cal_yr,
        #     'cal_qtr': cal_qtr,
        #     'fiscal_yr': fiscal_yr,
        #     'fiscal_qtr': fiscal_qtr,
        #     'accident_time': accident_time,
        #     'degree_injury_cd': degree_injury_cd,
        #     'fips_state_cd': fips_state_cd,
        #     'ug_location_cd': ug_location_cd,
        #     'ug_mining_method_cd': ug_mining_method_cd,
        #     'mining_equip_cd': mining_equip_cd,
        #     'equip_mfr_cd': equip_mfr_cd,
        #     'equip_mfr_name': equip_mfr_name,
        #     'shift_begin_time': shift_begin_time,
        #     'accident_type': accident_type,
        #     'no_injuries': no_injuries,
        #     'tot_exper': tot_exper,
        #     'mine_exper': mine_exper,
        #     'job_exper': job_exper,
        #     'occupation_cd': occupation_cd,
        #     'activity_cd': activity_cd,
        #     'injury_source_cd': injury_source_cd,
        #     'nature_injury_cd': nature_injury_cd,
        #     'inj_body_part_cd': inj_body_part_cd,
        #     'schedule_charge': schedule_charge,
        #     'days_restrict': days_restrict,
        #     'days_lost': days_lost,
        #     'trans_term': trans_term,
        #     'return_to_work_dt': return_to_work_dt,
        #     'immed_notify_cd': immed_notify_cd
        # }


    return render_template('templates\index.html', prediction_text = prediction_text)


    # except Exception as e:
    #     # Handle any errors that may occur during prediction or data processing
    #     # You can customize the error message as per your needs
    #     error_message = "Error occurred: {}".format(str(e))
    #     return render_template('index.html', prediction_text=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=8001)