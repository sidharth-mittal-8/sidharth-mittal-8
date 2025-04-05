from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "sample_name"  # Replace this with your actual full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist)

    # Get top output (first 20 lines)
    try:
        top_output = subprocess.getoutput("top -b -n1 | head -n 20")
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    top_html = top_output.replace("\n", "<br>")

    return f"""
    <pre>
    Name: {name}
    user: {username}
    Server Time (IST): {server_time}
    TOP output:
    {top_html}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
