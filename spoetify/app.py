import os
from flask import Flask, render_template, send_from_directory, request
import converter

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        hits = converter.SimpleTrackConverter().poem_to_song(request.form["poem"])
        return render_template('index.html', hits=hits, poem=request.form["poem"])
    else:
        return render_template('index.html', poem="I love food\nyou know me\nThat's why I love you\navocado")

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
