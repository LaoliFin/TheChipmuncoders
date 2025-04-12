from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

if __name__ == '__main__':
    # Note: Debug mode should be False in production
    app.run(debug=True)