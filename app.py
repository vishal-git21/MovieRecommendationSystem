from flask import Flask, request, jsonify, render_template
import pandas as pd
from surprise import Dataset, Reader, KNNBasic

app = Flask(__name__)


df = pd.read_csv('data/filtered_ratings.csv')
df= df.sample(frac=0.1, random_state=42) 
movies_df = pd.read_csv('data/movies.csv')
title_to_id = pd.Series(movies_df.movieId.values, index=movies_df.title).to_dict()


reader = Reader(rating_scale=(0, 5))
data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)
trainset = data.build_full_trainset()


algo_user = KNNBasic(sim_options={'user_based': True})
algo_user.fit(trainset)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    new_ratings = request.json['ratings']
    
    temp_user_id = max(df['userId']) + 1
    new_ratings_df = pd.DataFrame(new_ratings)
    new_ratings_df['userId'] = temp_user_id
    new_ratings_df['movieId'] = new_ratings_df['title'].map(title_to_id)
    new_ratings_df.drop(columns=['title'], inplace=True)
    
    new_df = pd.concat([df, new_ratings_df], ignore_index=True)
    new_data = Dataset.load_from_df(new_df[['userId', 'movieId', 'rating']], reader)
    new_trainset = new_data.build_full_trainset()
    
    algo_user.fit(new_trainset)
    
    all_movie_ids = df['movieId'].unique()
    rated_movies = new_ratings_df['movieId'].tolist()
    
    user_predictions = [algo_user.predict(temp_user_id, movie_id) for movie_id in all_movie_ids if movie_id not in rated_movies]
    user_predictions.sort(key=lambda x: x.est, reverse=True)
    
    n_recommendations = 10
    user_recommendations = user_predictions[:n_recommendations]
    
    id_to_title = {v: k for k, v in title_to_id.items()}
    user_recommendations = [{'title': id_to_title[pred.iid], 'estimated_rating': pred.est} for pred in user_recommendations]
    
    return jsonify({'user_recommendations': user_recommendations})

if __name__ == '__main__':
    app.run(debug=True)
