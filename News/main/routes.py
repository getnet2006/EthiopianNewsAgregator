from News.main import bp
from flask import render_template
from News.main import finder


@bp.route('/')
def index():
    et_news = finder.ethio_news()
    return render_template('main/index.html', et_news=et_news, title='Top')

@bp.route('/world')
def world():
    wo_news = finder.world_news()
    return render_template('main/world.html', wo_news=wo_news, title='World')

@bp.route('/africa')
def africa():
    af_news = finder.africa_news()
    return render_template('main/world.html', wo_news=af_news, title='Africa')

@bp.route('/europe')
def europe():
    eu_news = finder.europe_news()
    return render_template('main/world.html', wo_news=eu_news, title='Europe')