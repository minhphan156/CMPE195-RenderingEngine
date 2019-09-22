from flask import Flask, request
from nbToHTML import auto_convert

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the Rendering Engine!\n/pynb-to-html   --   Jupyter Notebook to HTML"


# Pass in raw Unicode text of Jupyter Notebook in POST request
# Returns HTML text of rendered notebook
@app.route("/pynb-to-html", methods=["POST"])
def nb_to_html():
    
    render_package = (auto_convert(request.get_data()))

    return render_package


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003, debug=True)