from flask import Flask,request
import webbrowser
import sys


app = Flask(__name__)

@app.route('/create-path', methods=['POST'])
def index():
    return "This route is not used for this example."

@app.route('/get-path',  methods=['GET'])
def path():
    youtube_link = request.args.get('youtube_link')

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(youtube_link)

    return f"Opening {youtube_link} in Chrome"

if __name__ == '__main__':
    
    app.run( debug=True)
