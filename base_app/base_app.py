from flask import Flask, flask.views
import os

app = flask.Flask(__name__)

app.secret_key = "bacon"

class Main(flask.views.MethodView):
    def get(self):
        '''Defines the template 
        for the landing page '''
        return flask.render_template('index.html') 

    def post(self): 
        ''' '''
        required = ['username','password']
        for r in required:
            if r not flask.request.form: 
                flask.flash("Error: {0} is required.".format(r))
                return flask.redirect(flask.url_for('index'))


class Remote(flask.views.MethodView):
    def get(self):
        return flask.render_template('remote.html')

    def post(self):
        result = eval (flask.request.form['expression'])
        flask.flash(result)
        return self.get()

        # alternate method
        # return flask.redirect(flask.url_for('index'))

         
app.add_url_rule('/',view_func=Main.as_view('index'), methods=['GET','POST'])
app.add_url_rule('/remote/',view_func=Remote.as_view('remote'), methods=['GET', 'POST'])

app.debug = True
app.run()