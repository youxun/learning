from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index
	user = {'nickname':'Miguel'}
	posts = [
	{'author':{'nickname':'John'},
	 'body':'Beautiful day in Portland!'
	},
	{'author':{'nickname':'Susan'},
	 'body':'Think in java'
	}
	]
	return render_template(
	'index.html',
	title = 'Home',
	user = user,
	posts = posts
	)
