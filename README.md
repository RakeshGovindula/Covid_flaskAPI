# Covid_flaskAPI
# Flask API to retrieve Covid-19 Details country wise and by Month and Year
### Install Pycharm or any Relevant Python IDE
 Create and activate Virtual Environment.
 In Pycharm you can use ```venv\Scripts\activate.bat``` command in windows to activate the Virtual Environment.
 
### Install the required packgages:
-> To Install the Packages follow the requirements.txt file.<br>
-> Go to the Folder where requirements.txt is present and type the following command.
```pip install -r requirements.txt```<br>
### Download the Dataset from Kaggle.
-> The Dataset link is : https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset/version/151<br>
### Clean the dataset and Create a SQlite Database for the data
-> Pandas will be helpful here.<br>
-> After Cleaning the data store the whole data into a database.<br>
-> After creating Database, Make sure that the database is present in the folder where our code is there.<br>
### Use the Database in our app.py 
-> Store the data from the database to a class.<br>
-> Query the data for Country name and Year and Month. from the URL 
```http://127.0.0.1:5000/covid/countryname/MMYYYY```<br>
### Return by Passing this data to HTML Page
-> Print the data in the tabular Format in the HTML Page.<br>
-> Run it by ```flask run``` Command after entering in to the folder app.<br>
-> In the URL enter like this format ```http://127.0.0.1:5000/covid/countryname/MMYYYY```. For Example- ```http://127.0.0.1:5000/covid/india/042020```<br>
-> We can retrieve the Details of Covid Cases across various Countries.<br>
-> You can see the some of them in the outputs folder.


