from flask import Flask, render_template
import random_quote_generator as QuoteGen

app = Flask(__name__)

@app.route('/')
def index():
    output = QuoteGen.generate_random_quote()
    return render_template('index.html',output=output)

if __name__ == "__main__":
    app.run(debug=True)