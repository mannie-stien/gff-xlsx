from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from gff_to_xlsx_converter import gff_to_xlsx  # Assuming this contains your conversion logic
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Ensure the 'uploads' directory exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")


@app.route("/", methods=["GET", "POST"])
def index():
    logger.info("Received a request.")
    
    if request.method == "POST":
        file = request.files.get("file")
        
        if not file or file.filename == "":
            logger.warning("No file selected.")
            return redirect(url_for("index"))

        gff_file_path = os.path.abspath(os.path.join("uploads", file.filename))
        
        # Define a generator to handle file streaming in chunks
        def save_in_chunks(input_file, output_path, chunk_size=8192):
            with open(output_path, "wb") as f:
                while True:
                    chunk = input_file.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
        
        # Save the file in chunks to reduce memory load
        save_in_chunks(file, gff_file_path)
        logger.info(f"File saved at {gff_file_path}")

        # Run the conversion process
        output_xlsx_path = os.path.abspath(os.path.join("uploads", "output.xlsx"))
        gff_to_xlsx(gff_file_path, output_xlsx_path)

        if not os.path.exists(output_xlsx_path):
            logger.error("Output file was not created.")
            return "Error in processing the file", 500

        return send_file(output_xlsx_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
