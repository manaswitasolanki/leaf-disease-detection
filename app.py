#importing the libaries we will need 
from flask import Flask, render_template, request
import pandas as pd 
import numpy as np 
import tensorflow as tf 
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os


app = Flask(__name__)
app.static_folder = 'static'
#FILES ABOVE 10MB WONT BE TAKEN 
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

ALLOWED_EXTENSIONS=['png','jpg','jpeg']
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def init():
    global graph
    #graph=tf.get_default_graph()
    graph=tf.compat.v1.get_default_graph()

def read_image(filename):
    img=load_img(filename,grayscale=False,target_size=(128,128))
    img=img_to_array(img)
    img=img.reshape(1,128,128,3)
    img=img.astype('float32')
    img=img/255
    return img 


@app.route("/",methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file=request.files['file']
        try:
            if file and allowed_file(file.filename):
                filename=file.filename
                file_path=os.path.join('static/images',filename)
                file.save(file_path)
                img=read_image(file_path)

                with graph.as_default():
                    model1=load_model('plant_detection_model.h5')
                    pred = model1.predict(img)
                    class_pred = [np.argmax(element) for element in pred]
                
                
                if class_pred[0]==0:
                    cat="Apple-Scab"
                elif class_pred[0]==1:
                    cat="Apple-Black Rot"
                elif class_pred[0]==2:
                    cat="Apple-Cedar Rust"
                elif class_pred[0]==3:
                    cat="Apple-Healthy"
                elif class_pred[0]==4:
                    cat="Blueberry-Healthy"
                elif class_pred[0]==5:
                    cat="Cherry-Powdery Mildew"
                elif class_pred[0]==6:
                    cat="Cherry-Healthy"
                elif class_pred[0]==7:
                    cat="Corn-Cercospora Leaf Spot, Gray Leaf Spot"
                elif class_pred[0]==8:
                    cat="Corn-Common Rust"
                elif class_pred[0]==9:
                    cat="Corn-Northern Leaf Blight"
                elif class_pred[0]==10:
                    cat="Corn-Healthy"
                elif class_pred[0]==11:
                    cat="Grape-Black Rot"
                elif class_pred[0]==12:
                    cat="Grape-Esca Black Measles"
                elif class_pred[0]==13:
                    cat="Grape-Leaf Blight (Isariopsis Leaf Spot)"
                elif class_pred[0]==14:
                    cat="Grape-Healthy"
                elif class_pred[0]==15:
                    cat="Orange-Haunglongbing Citrus Greening"
                elif class_pred[0]==16:
                    cat="Peach-Bacterial Spot"
                elif class_pred[0]==17:
                    cat="Peach-Healthy"
                elif class_pred[0]==18:
                    cat="Pepper Bell-Bacterial Spot"
                elif class_pred[0]==19:
                    cat="Pepper Bell- Healthy"
                elif class_pred[0]==20:
                    cat="Potato-Early Blight"
                elif class_pred[0]==21:
                    cat="Potato-Late Blight"
                elif class_pred[0]==22:
                    cat="Potato-Healthy"
                elif class_pred[0]==23:
                    cat="Raspberry-Healthy"
                elif class_pred[0]==24:
                    cat="Soybean-Healthy"
                elif class_pred[0]==25:
                    cat="Squash-Powdery Mildew"
                elif class_pred[0]==26:
                    cat="Strawberry-Leaf Scorch"
                elif class_pred[0]==27:
                    cat="Strawberry-Healthy"
                elif class_pred[0]==28:
                    cat="Tomato-Bacterial Spot"
                elif class_pred[0]==29:
                    cat="Tomato-Early Blight"
                elif class_pred[0]==30:
                    cat="Tomato-Late Blight"
                elif class_pred[0]==31:
                    cat="Tomato-Leaf Mold"
                elif class_pred[0]==32:
                    cat="Tomato-Septoria Leaf Spot"
                elif class_pred[0]==33:
                    cat="Tomato-Spider Mites Two Spotted Spider Mite"
                elif class_pred[0]==34:
                    cat="Tomato-Target Spot"
                elif class_pred[0]==35:
                    cat="Tomato-Tomato Yellow Leaf Curl Virus"
                elif class_pred[0]==36:
                    cat="Tomato Tomato Mosaic Virus"
                elif class_pred[0]==37:
                    cat="Tomato Healthy"
                return render_template('predict.html',cat=cat,user_image=file_path) 
        except Exception as e:
            return "Unable to read file.Please check if the file extension is correct."

    return render_template('predict.html')

if __name__ == "__main__":
    init()
    app.run()
             
             
           



