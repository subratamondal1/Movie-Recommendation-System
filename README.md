# Movie Recommendation System
An End to End ML Project, this is a Content Based Recommendation System using Natural Language Processing. This System has 4806 movies you can choose from, based on that you'll be recommended top 5 similar movies. Furthermore, you can click on the movie names that was recommended and then you'll be redirected to it's respective IMDB page. Thanks for visiting !!! 😇
1. [Movie Recommendation System Jupyter Notebook](https://github.com/subratamondal1/Movie-Recommendation-System/blob/main/Movie%20Recommendation%20System.ipynb)

2. [Movie Recommendation System App Hosted on Cloud](https://subratamondal1-movie-recommendation-system-app-jd8dve.streamlitapp.com/)

# `🎓` Tech Stack Used 
1. **Python**
2. **Streamlit**
3. **Numpy**
4. **Pandas**
5. **Scikit-Learn**
6. **NLTK**
7. **Git & Github**
8. **Jupyter Notebook**
9. **Vs-Code**
10. **Py-Charm**

# `🩴` Steps Involved
## 1. `Business Understanding`
**Objective :** `is to create an intelligent website where the user wil search a movie and based on that searched movie the user will be recommended top 5 similar movies they would like to watch.`

## 2. `Data Understanding`
After performing some statistical analysis we found that there are `4803 unique observations` & `20 unique features` in the movies dataset, whereas, in the credits dataset we have `4803 unique observations` & `4 unique features`

## 3. `Data Pre-Processing`
Merged both the dataset on `'title' column` into one dataframe called movies, due to their similarity. The merged dataframe contains `4803 unique observations` & `23 unique features`
### Column Filteration
**Since, we are making a Recommendation System, we will basically create tags for the Movies, therefore, we have to identify which columns are going to be useful for creating tags , make a list and discard the remaining columns.**
#### Ultimately, from those 23 columns we extracted the 7 required columns according to the requirements
* **genres**
* **id**
* **keywords**
* **title**
* **overview**
* **cast**
* **crew**
* 
### Dealing with Missing Values
Found 3 missing values in the overview column, and since, the number was very low compared to the no. of observations, therefore, we dropped those 3 observations.

### Duplicate Value Check
No duplicate value was found

### Column Data Reformatting
The data inside the columns were in weird format, for example :

We need to change the format from 

`[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]` to 

`['Action','Adventure','Fantasy','Science Fiction']`

We achieved those via creating multiple helper functions to cure the following columns `keywords	genres	overview	cast	crew`.

We also did `import ast` library # To convert them into list to avoid TypeError: string indices must be integers

### Important Step
**From the** `'keywords', 'genres', 'overview', 'cast', 'crew'` **columb we need to remove any spaces that are present inside the data of these columns to make them one individual entity i,e from this** `"Sam Worthington"` **to** `"SamWorthington"` **this because it is very important for our Recommendation System because if we don't do this the Recommendation System will get confused since due to space between "Sam Worthington" , "Sam" will be treated as one entity and "Worthington" will be treated as other entity instead of treating the whole "Sam Worthington" as one entity. So, now if there exists cast with multiple same first name but different last name then the Recommendation system might recommend the other person with the same name. For example you might want "Sam Worthington" but the system is recommending you "Sam Mendes"**. 

### Creating `tags` column
**Now these columns** `['keywords', 'genres', 'overview', 'cast', 'crew']` **are ready for concatenation to form** `tags column`

### Convert `tags column` from list to strings

### Stemming
**Stemming is a technique used to extract the base form of the words by removing affixes from them.**
Stemming converts multiple form of one word to only single form . For Example : 

From `["loving","love","loved"] to ["love","love","love"]`

### Converting `tags column` to lowercase
Its a recommended step

### Text Vectorization
Out of 5000 movies how will we know which 5 movies are similar? 

The recommendation is going to happen based on the tags.

### Important Step : `Ignore Stop Words`
**Stop Words** are those that are used for the formation of English Words but in reality they do not contribute in the meaning of the word, for example: are, and, they, to, etc. **We will discard them with the help of Scikit-learn library before doing vectorization**

### Text Vectorization
Here, the text or tags will be represented as Vectors in a 2-D space with coordinates, since all the tags or vectors will be in 2-D space, therefore, we are going to represent the closest neighbours around it.
**Techniques for Text Vectorization are :**
1. **Bag Of Words :** `Here, we will concatenate the text in a tag of a single movie into one large text, and from that large text I will count the frequency of the words (w) and extract say top 5000. And now theses each word(w) we are going to see how many times each word came in the first movie (m1) and second movie(m2) then we will create a Table (5000(m) x 5000(w)) with those information for all the movies.`
2. **TF-IDF**
3. **Word2Vector**

## 4. `Modelling`
## `Cosine Similarity` 
**Cosine similarity is a metric, helpful in determining, how similar the data objects are irrespective of their size, we need to calculate distance of all the movies from one another.**

**Since the Dimension is 5000, and at Higher Dimension : Euclidean Distance is not a reliable measurement.**

**Greater the distance Lesser the similarity, vice-versa, Lesser the Distance Greater the Similarity.**

### Recommend Model
**When passed a movie to the model, the model will return the top 5 most similar movies as an output.**

**After that, we can't do sorting directly because, it will shuffle the index, i.e the original index will be shuffled, which will result in wrong answers, therefore, we need to somehow hold the Index of each movie and that we will do with the help of** `enumerate`

**Sorted based on the index.**

**Sorted based on the cosine similarity value.**

**Extracting top 5 similar movies based on cosine similarity value.**

## 5. `Next Step : Convert this into an entire website with `streamlit``
## 6. `Deployment with Stremlit`
**With the help of Streamlit the model is hosted seamlessly in the Streamlit Cloud**

### What did it cost ?
Uhhmmn... few days, some sleepless night and few head scratches.
