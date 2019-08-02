from app import app, errors
from app.models import About, Director, Movie, Top10, MySeenList, Serie
from flask import render_template
from flask import request, url_for
from datetime import datetime
from datetime import timedelta


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", last_update=MySeenList.query.order_by('date desc').first(), this_month=True, title='Home', seen=MySeenList.query.order_by('date desc').first(), seenlist=MySeenList.query.order_by('date desc').all(), year=0, month=0)

@app.route('/about')
def about():
    return render_template("about.html",about=About.query.all())

@app.route('/directors', methods=['GET'])
def directors():
    page = request.args.get('page', default=1, type=int)
    directors = Director.query.paginate(page, app.config['DIRECTORS_PER_PAGE'], False)
    last_page = int(Director.query.count() % app.config['DIRECTORS_PER_PAGE'])
    if last_page == 0:
        last_page_num = int(Director.query.count() / app.config['DIRECTORS_PER_PAGE'])
    else:
        last_page_num = int(Director.query.count() / app.config['DIRECTORS_PER_PAGE']) + 1
    last_page_url = url_for('directors', page=last_page_num) 
    first_page_url = url_for('directors', page=1) 
    next_url = url_for('directors', page=directors.next_num) if directors.has_next else last_page_url
    prev_url = url_for('directors', page=directors.prev_num) if directors.has_prev else first_page_url
    return render_template("directors.html", directors=directors.items, next_url=next_url, prev_url=prev_url, page=page, first_page_url=first_page_url, last_page_url=last_page_url)

@app.route('/movies', methods=['GET'])
def movies():
    page = request.args.get('page', default=1, type=int)
    order = request.args.get('order', default='director', type=str)
    by = request.args.get('by', default='desc', type=str)
    first = request.args.get('first', default='False', type=str)
    orders = 'director.name' if order == 'director' else 'imdb_rank'
    if page == 1 and by == 'asc' and first == 'False':
        by = 'desc'
    elif page == 1 and by == 'desc' and first == 'False':
        by = 'asc'
    if page == 'first':
        page = 1
    last_page = int(Movie.query.count() % app.config['MOVIES_PER_PAGE'])
    if last_page == 0:
        last_page_num = int(Movie.query.count() / app.config['MOVIES_PER_PAGE'])
    else:
        last_page_num = int(Movie.query.count() / app.config['MOVIES_PER_PAGE']) + 1
        
    movies = Movie.query.join(Director).order_by(orders+' '+by, 'year asc').paginate(page, app.config['MOVIES_PER_PAGE'], False) 
    last_page_url = url_for('movies', page=last_page_num, order=order, by=by) 
    first_page_url = url_for('movies',first='True', page=1, order=order, by=by) 
    next_url = url_for('movies', page=movies.next_num, order=order, by=by) if movies.has_next else last_page_url
    prev_url = url_for('movies', page=movies.prev_num, order=order, by=by) if movies.has_prev else first_page_url
    return render_template("movies.html", movies=movies.items, next_url=next_url, prev_url=prev_url, page=page, order=order, by=by, first_page_url=first_page_url, last_page_url=last_page_url)

@app.route('/tv', methods=['GET'])
def tv():
    page = request.args.get('page', default=1, type=int)
    series = Serie.query.order_by('title').paginate(page, app.config['SERIES_PER_PAGE'], False)
    last_page = int(Serie.query.count() % app.config['SERIES_PER_PAGE'])
    if last_page == 0:
        last_page_num = int(Serie.query.count() / app.config['SERIES_PER_PAGE'])
    else:
        last_page_num = int(Serie.query.count() / app.config['SERIES_PER_PAGE']) + 1
    last_page_url = url_for('tv', page=last_page_num) 
    first_page_url = url_for('tv', page=1) 
    next_url = url_for('tv', page=series.next_num) if series.has_next else last_page_url
    prev_url = url_for('tv', page=series.prev_num) if series.has_prev else first_page_url
    return render_template("series.html", series=series.items, next_url=next_url, prev_url=prev_url, page=page, first_page_url=first_page_url, last_page_url=last_page_url)


@app.route('/top10')
def top10():
    return render_template("top10.html", top10=Top10.query.all())

@app.route('/movie/<movie_id>')
def movie(movie_id):
    movie=Movie.query.get_or_404(movie_id)
    return render_template("movie.html", movie=movie)
    

@app.route('/director/<director_id>')
def director(director_id):
    return render_template("director.html", director=Director.query.get_or_404(director_id))


@app.route('/tv/<serie_id>')
def serie(serie_id):
    return render_template("tv.html", serie=Serie.query.get_or_404(serie_id))


@app.route('/search', methods=['GET'])
def search():
    search = request.args.get('q')
    movies = Movie.query.filter(Movie.title.like('%'+search+'%'))
    directors = Director.query.filter(Director.name.like('%'+search+'%'))
    return render_template("search.html", search=search, movies=movies, directors=directors)

@app.route('/seen/<year>/<month>', methods=['GET'])
def seen(year, month):
    try:
        date = datetime(int(year), int(month), 1)
        seen = MySeenList.query.filter_by(date=date).first()
        return render_template("index.html", last_update=MySeenList.query.order_by('date desc').first(), this_month=False, title='Previous', seen=seen, seenlist=MySeenList.query.order_by('date desc').all(), year=year, month=month)
    except Exception:
        return render_template("404.html")
    
