import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from difflib import get_close_matches
import random

columns_data = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=columns_data)

columns_item = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL'] + [f'genre_{i}' for i in range(19)]
movies = pd.read_csv('u.item', sep='|', encoding='latin-1', names=columns_item, usecols=[0,1] + list(range(5, 24)))

data = pd.merge(ratings, movies, on='movie_id')

genre_features = movies.drop(columns = ['movie_id', 'title'])

cosine_sim = cosine_similarity(genre_features)

movie_titles = movies['title'].reset_index(drop=True)

def get_recommendations(movie_title, cosine_sim=cosine_sim):
    close_matches = get_close_matches(movie_title, movie_titles, n=1, cutoff=0.5)
    if not close_matches:
        return "", f"No close match found for {movie_title}. Please try a different movie name."
    best_match = close_matches[0]
    idx = movie_titles[movie_titles == best_match].index[0]
    sim_scores=  list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return f"Showing results for: **{best_match}**",movie_titles.iloc[movie_indices]
genre_map = {
    'Action': 1, 'Adventure': 2, 'Animation': 3, "Children's": 4,
    'Comedy': 5, 'Crime': 6, 'Documentary': 7, 'Drama': 8,
    'Fantasy': 9, 'Film-Noir': 10, 'Horror': 11, 'Musical': 12,
    'Mystery': 13, 'Romance': 14, 'Sci-Fi': 15, 'Thriller': 16,
    'War': 17, 'Western': 18
}
st.title("🎬 Smart Movie Recommender")
st.markdown("Type a movie name or pick one from the dropdown to get 5 similar movies based on genres.")
st.markdown("---") 

if st.button("🔁 Reset All"):
    st.session_state["selected_input"] = "-- Select a movie --"
    st.session_state["genre_choice"] = "-- Select a genre --"
    st.session_state["user_input"] = ""
    st.rerun()

user_input = st.text_input("Enter a movie title:","",key="user_input")

selected_input = st.selectbox("Or pick a movie from the list:", ["-- Select a movie --"] + list(movie_titles),key = "selected_input")
genre_choice = st.selectbox("🍿 Explore Movies by Genre",  ["-- Select a genre --"] + list(genre_map),key="genre_choice")


if user_input:
    
    st.subheader("Recommended Movies:")
    _, recommended = get_recommendations(user_input)
    if isinstance(recommended, str):
        st.error(recommended)
    else:
        st.success(f"**{_}**")
        for i, movie in enumerate(recommended, 1):
            st.markdown(f"{i}. {movie}")

if selected_input != "-- Select a movie --":
    st.subheader("Recommeneded Movies:")
    _, recommended = get_recommendations(selected_input)
    if isinstance(recommended, str):
        st.error(recommended)
    else:
        st.success(f"Showing results for: **{_}**")
        for i, movie in enumerate(recommended, 1):
            st.markdown(f"{i}. {movie}")
    

if genre_choice != "-- Select a genre --":
    genre_col = f'genre_{genre_map[genre_choice]}'
    genre_movies = movies[movies[genre_col] == 1]['title'].tolist()
    sampled_movies = random.sample(genre_movies, min(10, len(genre_movies)))

    st.success(f"🎬 Movies in **{genre_choice}** genre:")
    for i, title in enumerate(sampled_movies, 1):
        st.write(f"{i}. {title}")