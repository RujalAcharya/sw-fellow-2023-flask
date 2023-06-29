from flask import Flask, redirect, render_template
from appform import TestForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '18b8f7e31f1b1ddaa65d61f80d30d24302edd0e9b33c31de'

peoplelist = [{'name': "Ram",
               'age' : 50,
               'gender' : "Male"}]

@app.route("/people")
def people():
    return render_template("people.html", people=peoplelist)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = TestForm()
    
    if form.validate_on_submit():
        peoplelist.append({'name' : form.name.data,
                           'age' : form.age.data,
                           'gender' : form.gender.data})
        print(peoplelist)
        return redirect('/people')
    else:
        print(form.errors)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()
