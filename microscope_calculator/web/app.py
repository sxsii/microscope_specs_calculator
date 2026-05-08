from flask import Flask
from flask import render_template
from flask import request

import os

from werkzeug.utils import secure_filename

from core.calculator import calculate_real_size
from core.microscope_data import MICROSCOPES
from core.database import create_table
from core.database import save_record
from core.database import get_records


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

create_table()


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        username = request.form["username"]

        measured_size = float(
            request.form["measured_size"]
        )

        microscope_type = request.form["microscope_type"]

        output_unit = request.form["output_unit"]

        image = request.files["image"]

        filename = secure_filename(image.filename)

        image.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )

        magnification = MICROSCOPES[microscope_type]

        real_size_mm, converted = calculate_real_size(
            measured_size,
            magnification,
            output_unit
        )

        result = f"{converted:.6f} {output_unit}"

        save_record(
            username,
            measured_size,
            microscope_type,
            magnification,
            converted,
            output_unit
        )

    return render_template(
        "index.html",
        microscopes=MICROSCOPES.keys(),
        result=result
    )


@app.route("/history")
def history():

    records = get_records()

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)