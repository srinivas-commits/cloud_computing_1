from flask import Flask, jsonify, request, Response
import sqlite3
import xml.etree.ElementTree as ET

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('19mcme26.db')
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    conn.close()
    
    root = ET.Element('data')
    for row in rv:
        elem = ET.SubElement(root, 'row')
        for i, col in enumerate(row):
            col_name = cur.description[i][0]
            col_elem = ET.SubElement(elem, col_name)
            col_elem.text = str(col)

    return ET.tostring(root, encoding='unicode')

@app.route('/data', methods=['GET'])
def get_data():
    query = 'SELECT * FROM students'
    data = query_db(query)
    if not data:
        print("The data in the database is: ")
        print(data)
        return Response('No data found', status=404)
    else:
        return Response(data, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
