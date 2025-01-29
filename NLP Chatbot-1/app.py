from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV data into a Pandas DataFrame
df = pd.read_csv("student_data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    student_details = None
    if request.method == "POST":
        student_id = request.form.get("student_id")
        if student_id and student_id.isdigit():
            # Find the student details by StudentID
            student_details = df[df["StudentID"] == int(student_id)].to_dict(orient="records")
            if not student_details:
                student_details = "Student ID not found."
    
    return render_template("index.html", student_details=student_details)

if __name__ == "__main__":
    app.run(debug=True)
