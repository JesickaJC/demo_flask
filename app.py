from flask import Flask


app=Flask(__name__)

@app.route('/api/home')
def home():
    return "this is home page"

@app.route('/api/about')
def about():
    return "this is about page"

if __name__ =="__main__":
      app.run(debug=True)