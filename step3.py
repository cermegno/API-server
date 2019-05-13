from flask import Flask, jsonify, request
import os

app = Flask(__name__)

prize = "4"

@app.route('/api/v1/guess',methods=['GET'])
def status():
    #myguess = request.args.get('myguess') #Read a single passed parameter
    req = request.args # Put all passed parameters in a dictionary
    myguess = req['myguess'] # then extract whatever key/value you need
    if myguess == prize:
        response = {'result' : 'You guessed the number'}
        code = 201
    else:
        response = {'result' : 'No luck. Keep trying'}
        code = 202
    return jsonify(response), code

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
    
