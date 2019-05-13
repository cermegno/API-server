from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1/status',methods=['GET'])
def status():
    response = {'status' : 'Up and running'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
    
