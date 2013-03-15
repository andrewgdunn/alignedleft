from flask import Flask, render_template, redirect, url_for

# Configuring the Application
app = Flask(__name__, template_folder='static')
#app.host ='0.0.0.0'
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


# Route the resource request to the proper js file
@app.route('/d3.v3/d3.v3.js')
def sencha_app():
    return redirect(url_for('static', filename='d3.v3/d3.v3.js'))

# Generalized resource request
# @app.route('/app/view/<control>')
# def sencha_app_view(control):
#     redirect_url = os.path.join('app', 'view', control)
#     return redirect(url_for('static', filename=redirect_url))

if __name__ == '__main__':
    app.run()
