from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load models and data
with open('content_based_model.pkl', 'rb') as f:
    content_similarity = pickle.load(f)

with open('user_based_model.pkl', 'rb') as f:
    user_based_model = pickle.load(f)

with open('als_model.pkl', 'rb') as f:
    als_model = pickle.load(f)

movies = pd.read_pickle('movies.pkl')
ratings = pd.read_pickle('ratings.pkl')

# Initialize Flask app
app = Flask(__name__)

# Placeholder for hybrid recommendation logic
# In app.py, replace this:
def hybrid_recommendations(user_id, movie_name, top_n=10):
    # Dummy logic that returns the top N most popular movie titles
    top_movies = movies['title'].head(top_n).tolist()
    return top_movies
    recommended_titles = movies[movies['movieId'].isin(recommended_movie_ids)]['title'].tolist()
    return recommended_titles


@app.route('/')
def home():
    return render_template('index.html', recommendations=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form.get('movie_name')
    user_id = int(request.form.get('user_id'))
    top_n = int(request.form.get('top_n',10))

    # Get the recommendations
    recommendations = hybrid_recommendations(user_id, movie_name, top_n)

    # Render the recommendations on the HTML page
    return render_template('index.html', recommendations=recommendations, movie_name=movie_name, user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)
