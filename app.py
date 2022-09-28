import streamlit as st
import pickle
import requests

movies_final = pickle.load(open("movies.pkl", "rb"))
movies_name_list = movies_final["title"].values

similarity_matrix = pickle.load(open("similarity_matrix.pkl", "rb"))


# Fetch Posters
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1a58380d51ac1b466f75ec680d63a591&language=en-US")
    # Convert the response to json
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


# Movie Recommendations
def recommend(movie):
    recommended_movies = []
    recommended_movies_poster = []

    # Get the index from movies DataFrame
    movie_index = movies_final[movies_final["title"] == movie].index[0]

    # Get the distance vector from similarity_matrix
    distances = similarity_matrix[movie_index]

    # Create Movie List in Decreasing Order
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6]  # Slice top 5 similar movies

    for i in movie_list:
        movies_id = movies_final.iloc[i[0]].id
        recommended_movies.append(movies_final.iloc[i[0]].title)

        # Fetch Poster from API using movie_id
        recommended_movies_poster.append(fetch_poster(movies_id))

    return recommended_movies, recommended_movies_poster


st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    'Select a movie from the dropdown menu or simply just search it 😇',
    movies_name_list)

if st.button("Recommend"):
    names, posters_link = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters_link[0])

    with col2:
        st.text(names[1])
        st.image(posters_link[1])

    with col3:
        st.text(names[2])
        st.image(posters_link[2])

    with col4:
        st.text(names[3])
        st.image(posters_link[3])

    with col5:
        st.text(names[4])
        st.image(posters_link[4])