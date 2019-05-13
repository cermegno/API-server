from flask import Flask, jsonify, request
import os

app = Flask(__name__)

prize = "4"
print "The initial prize is : " + str(prize)

@app.route('/api/v1/setprize',methods=['POST'])
def setprize():
    global prize
    data = request.form # Put POST request data in a dictionary
    prize = data['newprize']
    response = {'result' : 'New prize set successfully'}
    print "Variable prize changed to : " + prize
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
    
