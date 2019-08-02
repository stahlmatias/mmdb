from flask import Flask, request, render_template, Response
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from datetime import timedelta

application = app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0 and (str(rule.rule) != '/search') and (str(rule.rule) != '/index') and (str(rule.rule) != '/sitemap.xml') and (str(rule.rule) != '/'):
              pages.append(
                           ["https://mmdb.com.ar"+str(rule.rule),ten_days_ago]
                           )

      return render_template('sitemap_template.xml', pages=pages)
     
    except Exception as e:
        return(str(e))	
