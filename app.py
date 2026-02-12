from flask import Flask, render_template, request, redirect, session, url_for
from models import db, User, Review
from werkzeug.security import generate_password_hash, check_password_hash
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# -------------------------
# HOME
# -------------------------
@app.route('/')
def home():
    return render_template('home.html')


# -------------------------
# SIGNUP
# -------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists"

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')


# -------------------------
# LOGIN
# -------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password"

    return render_template('login.html')


# -------------------------
# LOGOUT
# -------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


# -------------------------
# DASHBOARD
# -------------------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    reviews = Review.query.all()
    random_review = random.choice(reviews) if reviews else None

    return render_template(
        'dashboard.html',
        random_review=random_review,
        user=user
    )


# -------------------------
# CREATE REVIEW
# -------------------------
@app.route('/makeareview', methods=['GET', 'POST'])
def makeareview():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        rating = int(request.form['rating'])

        new_review = Review(
            username=user.nickname or user.username,
            title=title,
            content=content,
            rating=rating
        )

        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('makeareview.html')


# -------------------------
# SET NICKNAME (POPUP)
# -------------------------
@app.route('/set_nickname', methods=['POST'])
def set_nickname():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    nickname = request.form['nickname']
    user = User.query.get(session['user_id'])

    user.nickname = nickname.strip() if nickname.strip() else user.username

    db.session.commit()

    return redirect(url_for('dashboard'))


@app.route('/user_count')
def user_count():
    count = User.query.count()
    return {"count": count}

@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

@app.route('/lists')
def lists():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    # Use nickname if set, otherwise username
    display_name = user.nickname or user.username

    # Get all reviews written by this user
    user_reviews = Review.query.filter_by(username=display_name).all()

    return render_template('lists.html', user=user, reviews=user_reviews)

@app.route('/reviews')
def reviews():
    search = request.args.get('search', '')
    rating_filter = request.args.get('rating', '')
    user_filter = request.args.get('user', '')

    query = Review.query

    if search:
        query = query.filter(
            (Review.title.ilike(f"%{search}%")) |
            (Review.content.ilike(f"%{search}%"))
        )

    if rating_filter:
        query = query.filter_by(rating=int(rating_filter))

    if user_filter:
        query = query.filter(Review.username.ilike(f"%{user_filter}%"))

    all_reviews = query.all()

    return render_template(
        'reviews.html',
        reviews=all_reviews,
        search=search,
        rating_filter=rating_filter,
        user_filter=user_filter
    )


# -------------------------
# RUN APP
# -------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)