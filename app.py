from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        embarked = int(request.form['embarked'])

        # Convert to numpy array for prediction
        input_data = np.array([[age, sex, embarked]])
        prediction = model.predict(input_data)[0]

        result = "Survived 🚢" if prediction == 1 else "Did not survive 💀"
        return render_template('index.html', result=result)

    return render_template('index.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
