from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = ['GET'])
def apiget(action):

   if action == "user":
      return render_template("boy.html",user=boy)

   elif action == "car":
      return render_template("girl.html", car=girl)

   elif action == "all":
      return render_template("sex.html", user=boy, car=girl)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():

   # <button type="submit" form="form_user" name="action" value="user_update">Submit</button>
   # send name="action" and value="user_update" to POST

   if request.form["action"] == "user_update":

      boy["name"] = request.form["first_name"]
      girl["lastname"] = request.form["age"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':

   boy = {
            "name":"Vlad",
            "lastname": "Kanievskyi"
          }

   girl = {
           "name": "Ford",
           "lastname": "Mustang",
           "specifications": "fake bitch"
         }

   app.run(debug = True)