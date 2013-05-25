from flask import Flask, send_file
from pywkher import generate_pdf

app = Flask(__name__)


@app.route("/")
def hello():
    pdf_file = generate_pdf(html="""
<html>
    <head>
        <title>Hello, world</title>
    </head>
    <body>
        <h1>Hello, cruel world!</h1>
    </body>
</html>
    """)
    return send_file(pdf_file)
