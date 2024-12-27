from datetime import datetime
import time
from flask import Flask, render_template_string

app = Flask(__name__)

# HTML шаблон с автообновлением страницы
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>New Year Countdown</title>
    <meta http-equiv="refresh" content="1">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .countdown {
            font-size: 24px;
            text-align: center;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="countdown">
        <h1>New Year Countdown</h1>
        <p>{{ countdown_text }}</p>
    </div>
</body>
</html>
'''

def get_countdown():
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    diff = new_year - now
    
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60
    
    return f"Time until New Year: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, countdown_text=get_countdown())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)