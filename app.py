from flask import Flask, render_template, request
import DFA_Recognizer

# Initialize flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Accept uploaded text file
        uploaded_file = request.files['text_file']
        if uploaded_file:
            text = uploaded_file.read().decode('utf-8')

            # Split patterns to search by comma, if no pattern input used default list
            if request.form['patterns'] == "":
                patterns = ["David", "Sarah", "Ethan", "Vanessa", "Carl", "Mia", "Josh", "Emily", "Leo", "Isabella", "Benjamin", "Grace", "Jacob", "Sophia", "Liam"]
            else:
                patterns = request.form['patterns'].split(',')

            # Process the text and patterns using the DFA_Recognizer functions
            results = DFA_Recognizer.process_text(text, patterns)

            # Display output to results.html
            return render_template('results.html', results=results)
        else:
            return "No file uploaded"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
