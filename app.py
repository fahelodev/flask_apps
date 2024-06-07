# import the necessary packages
import flask
import json
import mariadb

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# configuration used to connect to MariaDB
config = {
    'host': 'mariadb_container',
    'port': 3306,
    'user': 'root',
    'password': 'tsoftDevops123',
    'database': 'tsoftDevops'
}

# route to return all people
@app.route('/', methods=['GET'])
def index():
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    # execute a SQL statement
    cur.execute("select * from ejercicio")

    # serialize results into JSON
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    # generate HTML content
    html_content = "<h1>Hola Mundo - Ansible Check - From Github</h1>"
    html_content += "<table border='1'><tr>{}</tr>".format("".join(["<th>{}</th>".format(header) for header in row_headers]))
    for row in json_data:
        html_content += "<tr>{}</tr>".format("".join(["<td>{}</td>".format(value) for value in row.values()]))
    html_content += "</table>"

    # return the HTML content
    return html_content

app.run(host='0.0.0.0', port=8080)
