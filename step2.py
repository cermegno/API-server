from flask import Flask, jsonify, request
import os

app = Flask(__name__)

prize = "4"

@app.route('/api/v1/guess',methods=['GET'])
def guess():
    #myguess = request.args.get('myguess') #Read a single passed parameter
    req = request.args # Put all passed parameters in a dictionary
    myguess = req['myguess'] # then extract whatever key/value you need
    if myguess == prize:
        response = {'result' : 'You guessed the number',
                    'guess' : myguess}
    else:
        response = {'result' : 'No luck. Keep trying',
                    'guess' : myguess}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
    
