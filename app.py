#env\Scripts\activate 

from flask import Flask,render_template, request, redirect
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from  sklearn.feature_extraction.text import TfidfVectorizer




def check_review(textData):
    file = open("pickle_model.pkl", 'rb')

    recreated_model = pickle.load(file)
    
    #load the vocab
    
    vocab = pickle.load((open('features.pkl', 'rb')))
    
    from sklearn.feature_extraction.text import CountVectorizer
    recreated_vec = CountVectorizer(decode_error ='replace' ,vocabulary = vocab)

    from sklearn.feature_extraction.text  import TfidfTransformer
    
    transformer = TfidfTransformer()
    
    return recreated_model.predict(transformer.fit_transform(recreated_vec.fit_transform([textData])))
    

    
app=Flask(__name__)


path1 = os.path.join("static","pics")

path1_css = os.path.join("static","css")

path2_css = os.path.join("static","css")


app.config['uplaod_img1']=path1
class Todo():
    def __repr__(self) -> str:
        return "okay"


@app.route('/',methods=['GET', 'POST'])
def hello_world():
    pics1=os.path.join(app.config['uplaod_img1'],"img1.jpg")
    return render_template('./k1.html',exta=os.path.join(path1_css,"f2.css"),our_ques='projectpath',img1=os.path.join(path1,"down2.png"),img2=os.path.join(path1,"down1.png"),img3=os.path.join(path1,"download.png"),our_ans='strr')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    print("\n\n\n\n "+projectpath)

    result=list(check_review(str(projectpath)))[0]
    if(result==0):
        strr="you are Negative"
    else:
        strr="you are positive"
    
    
    pics1=os.path.join(app.config['uplaod_img1'],"img1.jpg")
    
    return render_template('./k1.html',exta=os.path.join(path1_css,"f.css"),our_ques=projectpath,img1=pics1,our_ans=strr)

if __name__=="__main__":
    app.run(debug=True,port=8000)
'''
def index(name):
    return '<h1 background="yellow">hello {}!</h1>'.format(name)
'''

  
#print(list(check_review("I love you"))[0])