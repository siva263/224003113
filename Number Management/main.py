# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import requests
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():

    urls = request.args.getlist('url')
    numbers = [1,3,5,7,9,11,13,15,17,19,21,23]
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            numbers += response.json()['numbers']
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)}), 400
        except KeyError:
            return jsonify({'error': 'Invalid response format'}), 500
    return jsonify({'numbers': numbers})

if __name__ == '__main__':
    app.run(debug=True)
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
