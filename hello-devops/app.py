from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the homepage!"

# Add the new route for /status
@app.route('/status')
def status():
    return {"status": "ok", "message": "Service is running smoothly!"}

if __name__ == '__main__':
    app.run(debug=True)
