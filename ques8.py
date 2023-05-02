from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wordlist', methods=['POST'])
def get_word_list():
    input_string = request.json.get('input_string', '')

    if not input_string:
        return jsonify({'error': 'Input string is empty or null'}), 400

    word_list = input_string.split()

    return jsonify({'word_list': word_list})

if __name__ == '__main__':
    app.run(debug=True)