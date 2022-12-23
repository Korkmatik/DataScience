# Movie Recommendation System

The recommender system will recommend similar movies based on their title. After running the whole notebook, you will be prompted to input a movie title:

![image](https://user-images.githubusercontent.com/39222224/209410031-67a4ea02-6516-4ed6-ad78-f2570e932c37.png)

Type in a movie, that you want recommendations to:

![image](https://user-images.githubusercontent.com/39222224/209410056-7d15e15f-76be-4811-ab0c-b46f59d32220.png)

After that you should see the recommendation in the last output line of the last cell:

![image](https://user-images.githubusercontent.com/39222224/209410086-16d6d3f9-edfc-4eef-a94b-13479a5b61f1.png)


## Data
You can get the data from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset). Extract the archive and rename "filmtv_movies - ENG.csv" to "movies.csv"

## How the recommendation works

1. The movie titles inside the dataset are vectorized with the `TfidfVectorizer` from sklearn. 
2. Similarity between these vectors (movie titles) are calculated with cosine similarity
3. The recommendation system asks the user for a movie title
4. That movie title is compared to all titles inside the dataset, to find the best matching title to user's input
5. The index inside the similarity matrix of the user's specified movie title is determined
6. Based on that index, the similarity vector of that title is selected from the similarity matrix
7. The indices of the top 3 most similar titles are determined from the similarity vector for the user's input
8. Based on these indices the titles are determined from the original dataset and presented to the user
