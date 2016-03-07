from flask import Flask, render_template

app = Flask(__name__)

'''
@app.route("/profile.html")


def profile():
   # return 'This is a homepage from pycharm!'
    return render_template('profile.html')
'''

@app.route("/samplegmap.html")


def samplegmap():
   # return 'This is a homepage from pycharm!'
    return render_template('samplegmap.html')



if __name__ == '__main__':
    app.run()

# google API key AIzaSyDvf5_MyrOYKgKXmpmH6L2qWvSwkPEvAZg
