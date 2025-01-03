from flask import Flask, render_template, request

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions
@app.route('/thank_you', methods=['POST'])
def thank_you():
    # Retrieve the message from the form
    message = request.form.get('message')
    return f"Thank you for your feedback, dear PROFESSOR: {message}"

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
