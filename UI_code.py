import streamlit as st
import pandas as pd
import random

# ---------------- Page ---------------- #

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:#0b0b0d;
    color:white;
}

/* Hide Streamlit Menu */
#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Title */

.title{
text-align:center;
font-size:65px;
font-weight:bold;
color:#d8b45c;
letter-spacing:5px;
margin-top:20px;
}

.sub{
text-align:center;
color:#bbbbbb;
font-size:18px;
margin-bottom:40px;
}

/* Search Box */

div[data-baseweb="input"] input{
background:#17171b;
color:white;
border:2px solid #d8b45c;
border-radius:10px;
padding:12px;
font-size:18px;
}

/* Button */

.stButton>button{
background:#d8b45c;
color:black;
font-size:20px;
font-weight:bold;
border:none;
border-radius:10px;
padding:12px 30px;
width:100%;
}

.stButton>button:hover{
background:#f0c96d;
}

/* Cards */

.card{
background:#17171b;
padding:20px;
border-radius:15px;
border:1px solid #444;
margin-bottom:15px;
box-shadow:0px 0px 10px rgba(216,180,92,.25);
}

.card h3{
color:#d8b45c;
}

.badge{
display:inline-block;
padding:5px 12px;
background:#333;
border-radius:20px;
margin-right:8px;
margin-top:5px;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Load Data ---------------- #

df = pd.read_csv("movies_clusters.csv")

# ---------------- Recommendation Function ---------------- #

def recommend_movie(movie_name):

    movie = df[df["Title"].str.lower().str.contains(movie_name.lower(), na=False)]

    if movie.empty:
        return None

    cluster = movie["Cluster"].values[0]

    recommendations = df[df["Cluster"]==cluster]

    recommendations = recommendations[recommendations["Title"]!=movie["Title"].values[0]]

    if len(recommendations)>5:
        recommendations = recommendations.sample(5)

    return movie.iloc[0], recommendations

# ---------------- Header ---------------- #

st.markdown("<div class='title'>🎬 CINE MATCH</div>",unsafe_allow_html=True)

st.markdown("<div class='sub'>DBSCAN Movie Recommendation System</div>",unsafe_allow_html=True)

movie_name = st.text_input("",placeholder="Search Movie...")

if st.button("🎥 Recommend Movie"):

    result = recommend_movie(movie_name)

    if result is None:

        st.error("Movie Not Found")

    else:

        movie,recommendations = result

        left,right = st.columns([1,2])

        with left:

            st.markdown(f"""
            <div class='card'>

            <h3>{movie['Title']}</h3>

            <b>Cluster :</b> {movie['Cluster']}<br><br>

            <b>Language :</b> {movie['Original_Language']}<br><br>

            <b>Popularity :</b> {movie['Popularity']}<br><br>

            <b>Vote Average :</b> {movie['Vote_Average']}

            </div>
            """,unsafe_allow_html=True)

        with right:

            st.subheader("⭐ Recommended Movies")

            for _,row in recommendations.iterrows():

                st.markdown(f"""
                <div class='card'>

                <h3>🎬 {row['Title']}</h3>

                <span class='badge'>{row['Genre']}</span>

                <span class='badge'>⭐ {row['Vote_Average']}</span>

                <span class='badge'>🌍 {row['Original_Language']}</span>

                </div>
                """,unsafe_allow_html=True)