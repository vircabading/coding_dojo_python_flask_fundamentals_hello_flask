# /////////////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python > Flask > Fundamentals: Hello Flask
# By: Virgilio D. Cabading Jr.  Created: October 27, 2021
# /////////////////////////////////////////////////////////////////////

from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# add an app route success
@app.route('/success')
def success():
    return "success"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



