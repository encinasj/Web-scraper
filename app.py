from flask import Flask, render_template, request
from scraper import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webindex():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/results')
def results():
    scraper.ProxyScraper()
    scraper.run()

    return render_template('results.html', proxies=scraper.results)

if __name__ == "__main__":
    app.run(port=5000, debug=True, thread=True)
