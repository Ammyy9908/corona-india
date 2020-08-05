from Covid import Covid
from flask import Flask,redirect,render_template,request

app = Flask(__name__)

# c = Covid()
# print(c.get_data_state())

# Home Route

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        pass
    else:
        country = Covid()
        india_data = country.get_data_country()
        state_data = country.get_data_state()
        return render_template('index.html',data=india_data,state_data=state_data)


if __name__ == "__main__":
    app.run(debug=True)
