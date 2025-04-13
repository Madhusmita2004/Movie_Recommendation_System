**Movie** **Recommendation** **System**

This is a hybrid movie recommendation system built using a combination
of content-based filtering, collaborative filtering (user-based), and
Alternating Least Squares (ALS) algorithms. The system is designed to
recommend movies based on user preferences and historical interactions
with movies. The projectusestheMovieLensdatasetfor trainingand
evaluation.

**Dataset** **used**

For MovieRecommendationSystem
ProjectiuseMovieLensdataset.Hereisthelink:-

Gothroughthislink[<u>https://grouplens.org/datasets/movielens/</u>](https://grouplens.org/datasets/movielens/)
and
thendownloadthezipfil[e<u>ml-32m.zip</u>](https://files.grouplens.org/datasets/movielens/ml-32m.zip).Thenextractthezipfilefor
project,take**movies.csv**and **ratings.csv**file.

**Features**

> • **Hybrid** **Recommendation:**Combinescontent-based
> filtering,collaborativefiltering,and ALS
>
> techniquestoprovideaccuratemovierecommendations.
>
> • **CustomizableOutput:**Userscanspecifythenumber
> ofmovierecommendationstheywant,up toacustomizable"Top N".
>
> • **Web** **Interface:**Thesystem hasbeendeployed
> usingFlask,allowinguserstointeractwiththe
> recommendationenginethroughanintuitiveweb form.

**Technologies** **Used**

> • **Python**:Corelanguageused tobuild therecommendationengine. •
> **Pandas**:For datamanipulationand analysis.
>
> • **Scikit-learn**:Used for content-based
> filtering,buildingKNNmodelsfor collaborativefiltering,and evaluation.
>
> • **Seaborn**:used forvisualization
>
> • **KNN(fromScikit-learn)**:Used for user-based
> collaborativefilteringinstead oftheSurprise library.
>
> • **Flask**:Web frameworkfordeployingthesystem withafront-end
> HTMLinterface.
>
> • **Pickle(.pkl)**:Serialized modelfilesused forefficientstorageand
> retrievaloftherecommendation models.
>
> **Features**
>
> • Combinesmultiplerecommendationalgorithms • Flask-based backend API
>
> • HTML frontend interface
>
> • Modelserialized with picklefor easydeployment

**Usage**

> 1\. Enter aMovie:Typethenameofamovieinthesearchbar.
>
> 2\. SelectTop NRecommendations:Choosehowmanymovierecommendationsyou'd
> like(e.g.,10, 50,etc.).
>
> 3\. GetRecommendations:Thesystem
> willdisplayalistofmoviesuggestionsbased ontheinput.

**ProjectStructure:** Movie_Recommendation_System/

├── app.py

├── templates/

│ └── index.html

├── static/

├── models/

│ ├── content_based_model.pkl

│ ├── user_based_model.pkl

│ └── als_model.pkl

├── data/

│ ├── movies.pkl

│ └── ratings.pkl

└── movie_recommendation.ipynb

**How** **to** **Run** **theProject:**

**1.ClonetheRepository**

git clone
https://github.com/Madhusmita2004/Movie_Recommendation_System.git cd
Movie_Recommendation_System

**2.** **Install** **Dependencies**

pip install -r requirements.txt

**3.** **Run** **the** **Flask** **App**

python app.py

**4.** **View** **in** **Browser**

Then open your browser and go to:
[<u>http://127.0.0.1:5000</u>](http://127.0.0.1:5000/)

**5.** **Frontend** **(Optional)**

Open index.html and use it to submit your movie name, user ID, and get
recommendations.

> Files

\-**movierecommendation.ipynb** -Inthisfiletheprojectcodeand
.pklfilecodeareAvailable

\-**app.py**-Flaskbackend API

\-**index.html**-FrontendUI

\-**\*.pkl**-Picklefilesfor modelsand data

\-**README.md**-Projectdetails
