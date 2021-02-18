from flask import Flask, render_template, request, send_file
from LocProcessing import add_latlon

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    global filename
    file = request.files["CSV_File"]
    filename = "uploaded" + file.filename
    file.save(filename)
    nested_list = add_latlon(filename)
    print(nested_list)
    return render_template("index.html", table="table.html", nested_list=nested_list)

@app.route("/download")
def download():
    return send_file(f"Processed_{filename}", as_attachment=True, attachment_filename=f"Processed_{filename}")

if __name__ == "__main__":
    app.run(debug=True)