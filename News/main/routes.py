from News.main import bp
from flask import render_template
from News.main import finder

et_news = finder.top_news()

@bp.route('/')
def index():
    return render_template('main/index.html', et_news=et_news)