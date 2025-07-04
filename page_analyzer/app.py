import dotenv
import os
from page_analyzer import parser
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from page_analyzer import db
from .validate import validate_url, normalize_url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdflkasdfjasdlkfasd'

dotenv.load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')


@app.route('/')
def hello_hexlet():
    return render_template('index.html')


@app.get('/urls/<int:url_id>')
def url(url_id):
    conn = db.create_connection(DATABASE_URL)
    url = db.get_url(conn, url_id)
    url_checks = db.get_url_checks(conn, url_id)
    db.close_connection(conn)
    return render_template(
        'url.html', url=url, url_checks=url_checks)


@app.post('/urls')
def urls():
    url_name = normalize_url(request.form['url'])
    if not validate_url(url_name):
        flash('Некорректный URL', 'danger')
        return render_template('index.html'), 422
    conn = db.create_connection(DATABASE_URL)
    url = db.get_url_by_name(conn, url_name)
    if url:
        flash('Страница уже существует', 'info')
        db.close_connection(conn)
        return redirect(url_for('url', url_id=url.id))
    url_id = db.add_url(conn, url_name)
    db.close_connection(conn)
    flash('Страница успешно добавлена', 'success')
    return redirect(url_for('url', url_id=url_id))


@app.get('/urls')
def get_urls():
    conn = db.create_connection(DATABASE_URL)
    urls = db.get_urls(conn)
    db.close_connection(conn)
    return render_template('urls.html', urls=urls)


@app.post('/urls/<url_id>/checks')
def checks(url_id):
    conn = db.create_connection(DATABASE_URL)
    current_url = db.get_url(conn, url_id)
    try:
        resp = requests.get(current_url.name)
        resp.raise_for_status()
    except requests.RequestException:
        flash('Произошла ошибка при проверке', 'danger')
        db.close_connection(conn)
        return redirect(url_for('url', url_id=url_id))
    page_info = parser.parse_page(resp.text)
    db.add_url_check(conn, url_id, resp.status_code, page_info['h1'],
                     page_info['title'], page_info['description'])
    db.close_connection(conn)
    flash('Страница успешно проверена', 'success')
    return redirect(url_for('url', url_id=url_id))
