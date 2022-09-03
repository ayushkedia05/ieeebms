from crypt import methods
import json 
import time
from unicodedata import category
from flask import Flask ,render_template, request,jsonify
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
import pyrebase
import time
import os
app= Flask(__name__)
# run_with_ngrok(app)
CORS(app)







# @app.route('/metadata',methods=['POST'])

# def generatedata():
#     import ffmpeg
#     import sys
#     from pprint import pprint # for printing Python dictionaries in a human-readable way
#     data=[]
#     # read the audio/video file from the command line arguments
#     media_file = 'Launch1.mp4'
#     # uses ffprobe command to extract all possible metadata from the media file
#     data=ffmpeg.probe(media_file)["streams"]
    
#     return data


@app.route('/', methods=['POST'])




def hello_word():
    print(request.data)
    getdata=request.get_json()  
    # getdata=jsonify(getdata)
    print((getdata))
  
        
    import pyrebase
    import os
    config={
    "apiKey": "AIzaSyBR1rLney0FtBpDbe0OpHZKrqXzF9FXM-Y",
    "authDomain": "upload-files-97fdd.firebaseapp.com",
    "projectId": "upload-files-97fdd",
    "storageBucket": "upload-files-97fdd.appspot.com",
    "messagingSenderId": "1056716980772",
    "appId": "1:1056716980772:web:cdd9cf363c8b0ea6f58eb1",
    "databaseURL":"https://upload-files-97fdd.firebaseio.com"
    
    }



    firebase=pyrebase.initialize_app(config)
    storage=firebase.storage()

    print(storage)
    path_on_cloud="/images/"+str(getdata)




    print(type(path_on_cloud))
    # storage.child(path_on_cloud).put(path_local)


    storage.child(path_on_cloud).download(filename="ieeeimage.jpg",path=os.path.basename('test'))
    time.sleep(8)
    
    from PIL import Image
    import tensorflow 
    from tensorflow.keras.preprocessing.image import load_img,img_to_array
    import numpy as np
    from keras.models import load_model
    import requests
    from bs4 import BeautifulSoup

    model = load_model('FV.h5')
    labels = {0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot', 7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger', 14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
            19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple', 26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn', 32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'}

    fruits = ['Apple','Banana','Bello Pepper','Chilli Pepper','Grapes','Jalepeno','Kiwi','Lemon','Mango','Orange','Paprika','Pear','Pineapple','Pomegranate','Watermelon']
    vegetables = ['Beetroot','Cabbage','Capsicum','Carrot','Cauliflower','Corn','Cucumber','Eggplant','Ginger','Lettuce','Onion','Peas','Potato','Raddish','Soy Beans','Spinach','Sweetcorn','Sweetpotato','Tomato','Turnip']

    def fetch_calories(prediction):
        try:
            url = 'https://www.google.com/search?&q=calories in ' + prediction
            req = requests.get(url).text
            scrap = BeautifulSoup(req, 'html.parser')
            calories = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
            return calories
        except Exception as e:
            # st.error("Can't able to fetch the Calories")
            print(e)

    def processed_img(img_path):
        img=load_img(img_path,target_size=(224,224,3))
        img=img_to_array(img)
        img=img/255
        img=np.expand_dims(img,[0])
        answer=model.predict(img)
        y_class = answer.argmax(axis=-1)
        print(y_class)
        y = " ".join(str(x) for x in y_class)
        y = int(y)
        res = labels[y]
        print(res)
        return res.capitalize()

    def run():
        # st.title("Fruits🍍-Vegetable🍅 Classification")
        # img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
        # if img_file is not None:
        #     img = Image.open(img_file).resize((250,250))
        #     st.image(img,use_column_width=False)
        #     save_image_path = './upload_images/'+img_file.name
        #     with open(save_image_path, "wb") as f:
        #         f.write(img_file.getbuffer())

        #     # if st.button("Predict"):
        #     if img_file is not None:
        save_image_path='ieeeimage.jpg'
        result= processed_img(save_image_path)
        # aaa=result
        print(result)
        # if result in vegetables:
        #     st.info('**Category : Vegetables**')
        # else:
        #     st.info('**Category : Fruit**')
        # st.success("**Predicted : "+result+'**')
        cal = fetch_calories(result)
        if cal:
            # aa=cal
            print(cal)
        data={
        "category":result,
        "cal":cal
        }    
        return data
    answer=run()

    
    
    return jsonify(answer)


if __name__ =='__main__':
    app.run(  port=3002,debug=True  )



    
    
