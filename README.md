 🎬 CineMatch --- Movie Recommendation System

> An unsupervised machine learning movie recommendation system built
> with DBSCAN, feature engineering, TF-IDF, and Streamlit.

## 📌 Project Overview

CineMatch is a practical machine learning project that uses **DBSCAN
clustering** to group movies according to their available features and
then recommend other movies from the same cluster.

The project combines categorical movie information, text information
from movie overviews, and numerical features. The processed features are
combined into a sparse feature matrix and passed to DBSCAN.

A Streamlit application provides a simple interface where a user can
search for a movie and receive recommendations.

## ✨ Features

-   🎬 Movie search
-   🤖 DBSCAN-based clustering
-   🎭 Genre encoding
-   🌍 Original-language encoding
-   📝 Movie overview processing with TF-IDF
-   📊 Numerical feature scaling
-   ⭐ Rating information
-   🔎 Cluster-based recommendations
-   🖥️ Streamlit web interface
-   🌑 Dark cinema-style UI

## 🧠 Machine Learning Approach

This is an **Unsupervised Machine Learning** project because there is no
target label being predicted during training.

### DBSCAN

The project uses:

``` python
dbscan = DBSCAN(eps=1.5, min_samples=5)
clusters = dbscan.fit_predict(X)
```

DBSCAN groups observations according to density and can identify
observations that do not belong to a dense group. These observations
receive the label:

``` text
-1
```

which represents DBSCAN noise/outliers.

## 🔄 Project Workflow

``` text
Movie Dataset
     ↓
Data Cleaning
     ↓
Genre Encoding
     ↓
Language Encoding
     ↓
Overview → TF-IDF
     ↓
Numerical Features → StandardScaler
     ↓
Sparse Feature Combination
     ↓
DBSCAN Clustering
     ↓
Cluster Assignment
     ↓
Movie Search
     ↓
Find Movie Cluster
     ↓
Find Movies in Same Cluster
     ↓
Recommendations
     ↓
Streamlit UI
```

## 🛠️ Technologies Used

  Technology         Purpose
  ------------------ ----------------------------------
  Python             Main programming language
  Pandas             Data manipulation
  NumPy              Numerical operations
  Scikit-learn       Preprocessing, TF-IDF and DBSCAN
  SciPy              Sparse matrix operations
  Streamlit          Web application
  Jupyter Notebook   Model development

## 📊 Features Used

### Genre

Genre values are converted into multiple binary features:

``` python
genre = df_new["Genre"].str.get_dummies(sep=" ")
```

### Original Language

The language column is converted into dummy variables:

``` python
language = pd.get_dummies(
    df_new["Original_Language"],
    prefix="Language",
    dtype=int
)
```

### Overview

Movie descriptions are converted into numerical text features using
TF-IDF:

``` python
tfidf = TfidfVectorizer(stop_words="english")
overview = tfidf.fit_transform(df_new["Overview"])
```

### Numerical Features

The project scales:

``` text
Popularity
Vote_Count
Vote_Average
```

using:

``` python
scaler = StandardScaler()

numeric = scaler.fit_transform(
    df_new[["Popularity", "Vote_Count", "Vote_Average"]]
)
```

## 🧩 Combining the Features

Because the feature space can become large, sparse matrices are used.

``` python
from scipy.sparse import csr_matrix, hstack

genre = csr_matrix(genre.values)
language = csr_matrix(language.values)
numeric = csr_matrix(numeric)

X = hstack([
    genre,
    language,
    overview,
    numeric
])
```

Using sparse matrices is particularly useful for TF-IDF and
dummy-encoded features because many values are zero.

## 🎯 Recommendation Logic

When the user enters a movie name:

1.  The system searches the movie dataset.
2.  The selected movie is identified.
3.  Its DBSCAN cluster is retrieved.
4.  Other movies with the same cluster label are selected.
5.  The recommendations are displayed in Streamlit.

The cluster is retrieved using:

``` python
cluster = movie["Cluster"].values[0]
```

## 🖥️ Streamlit Application

The Streamlit interface provides:

-   Movie search
-   Selected movie information
-   Cluster information
-   Movie rating information
-   Genre information
-   Original language information
-   Recommended movie cards

Run the application with:

``` bash
streamlit run app.py
```

## 📁 Project Structure

``` text
movie_recommendation/
│
├── app.py
├── m.ipynb
├── movies_clusters.csv
├── movie_Dr.csv
├── requirements.txt
├── README.md
└── .gitignore
```

### Main Files

  File                    Description
  ----------------------- -------------------------------------------
  `UI_code.py`                Streamlit application
  `train_code.ipynb`               Model development and experimentation
  `movies_clusters.csv`   Movie data containing cluster assignments
  `movie_Dr.csv`          Movie dataset used during development
  `requirements.txt`      Python dependencies
  `README.md`             Project documentation

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd movie_recommendation
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

Activate it on Windows:

``` bash
.venv\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install pandas numpy scikit-learn scipy streamlit
```

Or:

``` bash
pip install -r requirements.txt
```

## ▶️ Run the Project

``` bash
streamlit run app.py
```

Streamlit will provide a local address that can be opened in a browser.

## 📈 Why DBSCAN?

DBSCAN was selected because it:

-   Groups data according to density
-   Can detect noise/outliers
-   Does not require the number of clusters to be specified in advance
-   Provides an interesting unsupervised-learning approach for
    experimenting with movie similarity

## ⚠️ Limitations

The current project has some limitations:

-   Recommendations depend on the resulting DBSCAN clusters.
-   `eps` and `min_samples` can strongly affect the clustering result.
-   Movies classified as `-1` are treated as DBSCAN noise.
-   TF-IDF can create a high-dimensional feature space.
-   The current system does not use individual user watch history or
    personalized preferences.
-   Recommendation quality depends on the selected features and
    preprocessing.

## 🚀 Future Improvements

Possible future improvements include:

-   🎞️ Add movie posters
-   ⭐ Rank recommendations by similarity
-   🔍 Add fuzzy movie-name search
-   👤 Add personalized user preferences
-   ❤️ Add favorites/watchlist
-   📊 Visualize DBSCAN clusters
-   🧠 Compare DBSCAN with K-Means
-   📈 Tune DBSCAN parameters
-   🌐 Deploy the Streamlit application online
-   🎬 Add trailers and additional movie metadata

## 🎓 Learning Outcomes

This project provided practical experience with:

-   Data cleaning
-   Feature engineering
-   Categorical encoding
-   TF-IDF
-   Feature scaling
-   Sparse matrices
-   Feature combination
-   Unsupervised machine learning
-   DBSCAN
-   Cluster-based recommendation logic
-   Streamlit
-   Organizing a machine learning project for GitHub

## 👨‍💻 Author

**Hamid**

ML / AI DEVELOPER

This project was developed as a practical project for learning
**unsupervised machine learning, DBSCAN clustering, feature engineering,
and recommendation systems**.

## ⭐ Support

If you find the project useful, consider giving the GitHub repository a
⭐.

## 📜 License

This project is intended for educational and learning purposes.
