from email import message
from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{
    'id' : 1,
    'name' : 'Mom',
    'contact' : '8763863965',
    'done' : False
},

{
    'id' : 2,
    'name' : 'Dad',
    'contact' : '569363563',
    'done' : False
}]

@app.route('/add-data', methods = ['POST'])

def add_contact():
    if not request.json:
        return(jsonify({'status' : 'error', 'message' : 'Please give the number'}, 400))
    
    contact = {'id' : contacts[-1]['id'] + 1, 'name' : request.json['name'], 'contact' : request.json.get('contact', ''), 'done' : False}

    contacts.append(contact)
    return(jsonify({'status' : 'success', 'message' : 'contact added'}))

if __name__ == '__main__':
    app.run()