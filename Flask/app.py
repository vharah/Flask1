from flask import Flask

# WSGF Application
app = Flask(__name__)

# Decorator binding in function
@app.route('/') 
def welcome():
    return 'Welcome to Flask '

@app.route('/JSON') 
def JSON():
    return 'Welcome to JSON '

if __name__ == '__main__':
    app.run()