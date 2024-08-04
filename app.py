from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load scaler and model
scaler = pickle.load(open('model/StandardScaler.pkl', 'rb'))
model = pickle.load(open('model/gbr_model_for_prediction.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_outputs():
    try:
        css = float(request.form['css'])
        
        # Scale the input data
        input_scaled = scaler.transform([[css]])
        
        # Predict outputs
        outputs = model.predict(input_scaled)
        
        # Format the outputs (assuming model.predict returns an array)
        outputs_rounded = np.round(outputs[0], 2)
        coal, bentonite, furnance_oil, im_speed, total_bed_height, lime_coal, t1, t2, t3, t4, t5, t6, t7, t8, prod_qty, tumble_index, abrasion_index, mean_dia, porosity_pellet, input_fe, output_fe = outputs_rounded
        
        # Divide furnance_oil by 1000 and round it to 2 decimal places
        # furnance_oil = round(furnance_oil / 1000, 2)

        result = {
            "css": css,
            "coal": coal,
            "bentonite": bentonite,
            "furnance_oil": furnance_oil,
            "im_speed": im_speed,
            "total_bed_height": total_bed_height,
            "lime_coal": lime_coal,
            "t1": t1,
            "t2": t2,
            "t3": t3,
            "t4": t4,
            "t5": t5,
            "t6": t6,
            "t7": t7,
            "t8": t8,
            "prod_qty": prod_qty,
            "tumble_index": tumble_index,
            "abrasion_index": abrasion_index,
            "mean_dia": mean_dia,
            "porosity_pellet": porosity_pellet,
            "input_fe": input_fe,
            "output_fe": output_fe
        }

        return render_template('result.html', **result)
    except Exception as e:
        print("Error:", e)
        return render_template('index.html', error=str(e))

if __name__ == "__main__":
    app.run(debug=True)