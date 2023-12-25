import matplotlib

from flask import *
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('agg')
app = Flask(__name__)


@app.route("/sin/<int:start>/<int:stop>")
def sin_function(start, stop):
    x = np.arange(start, stop, 0.1)
    y = np.sin(x)
    plt.plot(x, y, color='blue')
    plt.savefig("./static/fig.png")
    plt.close()
    return render_template("./function.html")


@app.route("/cos/<int:start>/<int:stop>")
def cos_funtions(start: int, stop: int):
    x = np.arange(start, stop * np.pi, 0.1)
    y = np.cos(x)

    plt.plot(x, y, color='green')
    plt.savefig("./static/fig.png")
    plt.close()
    return render_template("./function.html")


@app.route("/")
def something():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
