# Rechek
This is a ml based review checker model. With the help of this we can easy check out text positivity, means this can show that our text is positive or negative.
# Useful and required commands:

py -m venv env
env\Scripts\activate
# module used
python sklearn
python pandas
python numpy
python flask
python pickle

# Database:
You can choose any dataset of reviews and rating.
Column for datasets  should be {"review","rating","positivity"}
review :- This a string contain meaningful text.
rating :- Corresponing to review we assign a number bitween 1 and 5.
positivity :- for rating > 3 = 1 and for rating<3 =0
# Database file:
In my main_model file, I used database file name final_250k_reviews.csv.
