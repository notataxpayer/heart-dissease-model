# from flask import Flask, request, jsonify
# import pickle
# import pandas as pd

# app = Flask(__name__)

# # Load model once at the beginning
# with open("generate_heart_disease.pkl", 'rb') as file:
#     model = pickle.load(file)

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # JSON data dari client
#         data = request.get_json()

#         # Fitur yang diperlukan
#         expected_features = ['cp', 'thalach', 'slope', 'oldpeak', 'exang', 'ca', 'thal', 'sex', 'age']

#         # Cek apakah semua fitur ada
#         if not all(feature in data for feature in expected_features):
#             return jsonify({"error": "Missing required features"}), 400

#         # Ubah ke DataFrame
#         input_df = pd.DataFrame([data])

#         # Lakukan prediksi
#         prediction = model.predict(input_df)
#         result = 'Have Heart Disease' if prediction[0] == 1 else 'Did Not Have Heart Disease'

#         return jsonify({"prediction": result})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400

    image_file = request.files['image']
    
    try:
        image = Image.open(image_file.stream)
        # lakukan prediksi di sini...
        print("Image received:", image.size)

        return jsonify({'prediction': 'Prediksi Berhasil'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
