# leaf-disease-detection
The PlantVillage dataset consists of 54303 healthy and unhealthy leaf images divided into 38 categories by species and disease.

![Screenshot (49)](https://user-images.githubusercontent.com/72511465/181829805-da81d6af-b57f-49de-a123-61c93ef2bb5c.png)
![Screenshot (52)](https://user-images.githubusercontent.com/72511465/181829904-82f47cbc-0fa3-4a9b-908e-2d7f29b2d7da.png)
![Screenshot (77)](https://user-images.githubusercontent.com/72511465/181829917-52655d14-353e-483b-b2dd-462919c6932d.png)

The dataset is called 'plant_village' on Github.

We will build a CNN model to predict if a plant has a disease or not by taking the images of its leaves as input.

We will be using keras to build the model.

The repository contains a py notebook with the model and it's analysis, an .h5 file which is the final model and files to execute the same on a web application.

Below is a demo of the application:
![Screenshot (78)](https://user-images.githubusercontent.com/72511465/183300630-5ae9c40c-6488-4760-9e03-e1755ec4b073.png)
This is the home.html page ,which has an option to upload an image file

![Screenshot (79)](https://user-images.githubusercontent.com/72511465/183300675-ff360914-0871-4ddf-bea5-d46e1d30a878.png)
We have Selected an image called example3 from our device.

![Screenshot (80)](https://user-images.githubusercontent.com/72511465/183300706-20f2f014-2712-43ec-acca-aa90897cd46a.png)
This is the predict.html file which gives us the final predcition.
