import streamlit as st
import pickle
import requests

# Load movies_final dataframe
movies_final = pickle.load(open("movies.pkl", "rb"))

# Load movies_name_list
movies_name_list = movies_final["title"].values

# Similarity Matrix
similarity_matrix = pickle.load(open("similarity_matrix.pkl", "rb"))

# Fetch Posters


def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1a58380d51ac1b466f75ec680d63a591&language=en-US")
    # Convert the response to json
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def fetch_imdb_movie_page(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=1a58380d51ac1b466f75ec680d63a591&language=en-US")
    data = response.json()
    return "https://www.imdb.com/title/" + data["imdb_id"] + "/"


# Movie Recommendations
def recommend(movie):
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_imdb_homepage = []

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

        recommended_movies_imdb_homepage.append(
            fetch_imdb_movie_page(movies_id))

    return recommended_movies, recommended_movies_poster, recommended_movies_imdb_homepage


st.title("Movie Recommendation System")
st.caption("This is a Content Based Recommendation System using Natural Language Processing. This System has 4806 movies you can choose from, based on that you'll be recommended top 5 similar movies. Further you can click on the movie names that was recommended and then you'll be redirected to it's respective IMDB page. Thanks for visiting !!! 😇 ")
selected_movie = st.selectbox(
    'Select a movie from the dropdown menu or simply just search it 😇',
    movies_name_list)

if st.button("Recommend"):
    names, posters_link, homepage = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(f"[`{names[0]}`]({homepage[0]})")
        st.image(posters_link[0])

    with col2:
        st.write(f"[`{names[1]}`]({homepage[1]})")
        st.image(posters_link[1])

    with col3:
        st.write(f"[`{names[2]}`]({homepage[2]})")
        st.image(posters_link[2])

    with col4:
        st.write(f"[`{names[3]}`]({homepage[3]})")
        st.image(posters_link[3])

    with col5:
        st.write(f"[`{names[4]}`]({homepage[4]})")
        st.image(posters_link[4])
