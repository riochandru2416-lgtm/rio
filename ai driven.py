from flask import Flask, jsonify, send_from_directory
import random
import datetime
import os

# ✅ Use __name__, not _name_
app = Flask(__name__, static_folder='.', static_url_path='')

def get_week_data():
    today = datetime.date.today()
    data = []
    for i in range(7):
        day = today - datetime.timedelta(days=i)
        hours = round(random.uniform(2, 10), 1)
        focus = round(random.uniform(3, 9), 1)
        tasks = random.randint(1, 6)
        score = 0.5 * hours + 0.4 * focus + 0.1 * tasks
        if score > 7:
            label = "productive"
        elif score > 5:
            label = "average"
        else:
            label = "low"
        data.append({
            "date": str(day),
            "hours": hours,
            "focus": focus,
            "tasks": tasks,
            "label": label
        })
    return list(reversed(data))

@app.route("/api/summary")
def summary():
    records = get_week_data()
    avg_focus = sum(r["focus"] for r in records) / 7
    trend = "improving" if records[-1]["focus"] > records[0]["focus"] else "declining"
    summary_text = f"Your learning curve looks {trend} with an average focus of {avg_focus:.1f}. Keep it up!"
    return jsonify({"records": records, "summary": summary_text})

# ✅ Serve HTML file at root
@app.route('/')
def home():
    return send_from_directory('.', 'driven progress.html')

# ✅ Use __main__, not _main_
if __name__ == "__main__":
    app.run(debug=True)
