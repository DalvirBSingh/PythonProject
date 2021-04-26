# PythonProject

CIS1051 Project Sections

- Demo
- Preposal
- Proposal
- Building Project Locally Instructions



# Demo

##### Note : The video is 10 minutes long but in the description, the video has timestamps that can help navigate you to the parts you are intered in. The system design chapter is not required but I just did it since it seemed appropriate.  

###### Link: https://youtu.be/CtjjvP5DAys


# Preproposal
## What idea(s) do you have for your final project?

- Facial Image Emotion Detecter
- Detect Whether person is wearing a mask or not
- Text Sentiment analysis(Tweets,User entered, etc)
- Detect whether person is focused or not
- Movie Recommendation system

## If you plan to collaborate with one or two classmates, what are their names?

No,individual project

## Do you have any questions of your own?
- Do we need to deploy the application to the web after completion?


# Proposal

## What will (likely) be the title of your project?

Emotion Detection System

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A website that allows you to upload an face image and the system will predict what emotion the user is experiencing. 

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

A emotion detection system has many applications such as recognizing how users react to ads, user interfaces, movie reviews, and many other. Therefore to create a lighter version of this emotion detection system. My project will consist of creating a django web application that is integrated with a trained machine learning model to create an intelligent system that can emulate and guage rections from faces. Basically it will be a simple web application interface that will allow users to upload images and the software will predict the emotion that is expressed. The machine learning aspect of this project will be created from scratch based on inspirations from other facial detection systems. Planning to use a kaggle dataset to train the machine learning models and trying different machine learning algorithms and ultimately choosing the one that has the highest accuracy. Then, I will integrate the trained machine learning model with the django tech stack for web application development. There is a facial-emotion-recognition python library that could simplify this project but since Iwant to learn more about machine learning and processing images for intelligent systems, I will be creating the emotion detector from scratch.

Main Web Features: 
- Home Screen with upload image button
- Results page that displays the emotion expressed in the given image 

Machine Learning Features: 
- Trained & Tested Machine learning model for predicting user emotion



## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

Solo Project

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

A good outcome is a trained machine learning model to detect emotion without a user interface to facilitate the user interaction of uploading a image and displaying results

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A better outcome is relatively accurrate trained machine learning model integrated with a web interface to facilate uploading and displaying results

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The best outcome is extremely accurrate trained machine learning model integrated with a web interface to facilate uploading and displaying results

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

Steps to Accomplish this project: 

Machine Learning Aspect: 
1) Find meaninful dataset to use to train the machine learning models
2) Learn techniques to accomplish this task by learning how to perform feature extraction from images
3) Read relevant papers on this topic https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1643&context=etd_projects
4) Learn how to use keras and convolutional neural networks as that seems to popular combination for image processing in machine learning 
5) Train the Machine learning Model on the dataset with multiple machine learning algorithms
6) Test the ML models on test data and choose the algorithm with the best accuracy

Web Application Aspect: 
1) Bootstrap a django web application
2) Create a home screen with a button to allow the user to select image
3) Create a result page that will display the prediction
4) Integrate the trained ML model into the web application and linking the home screen -> ML processing -> Result Page


Topics to Research: 
1) Keras library 
2) Feature extraction from images 
3) How convolutional neural networks works
4) Learning(Refreshing) differennt machine learning algorithms 
5) Learning Django Web App Architecture 

Potential New Skills Gained From Project: 
1) Keras Tool
2) CNN understanding 
3) Feature extraction and implication with different uses



# Progress Report

#### Your name

Dalvir Singh

#### Your section leader's name
Sai Shi

#### Project title

Emotion Detection System

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

- Learned how CNN works & feature extraction from images
- Trained a machine learning model using kaggle data set to detect a user's emotion provided a facial image
- Learning Django Web Architecture Pattern
- Created a Django Web application to serve the trained machine learnig model. Created simple UI pages to allow user to upload an image and display the results on the next page. 

#### What have you not done for your project yet?
- Refine/tune the machine learning models to get better accuracy on 
- Integrate the web app & trained machine learning model

#### What problems, if any, have you encountered?
- No big problems, just minor bugs & issues. Most time consuming part is training the machine learning model on the large dataset. I still need to optimize the parameters to reach better accuracy and each time it just takes so long. 


#### Challeges 
- Traininng the machine learning model takes forever, just 20 epoch took hours & 124 epochs in a attempt to increase accuracy took 16hours. As a result, I didn't have enough time to fine tune the parameters to achieve the best result or accuracy but did enough in the time span given to provide a proof of concept. 
- Keras & tensor flow version conflicts, resolved by finding the right versions that mix well together

#### What I enjoyed about this project
- Learning more about computer vision and applying knowledges from different classes & personal experience 
- Have a interesting projects to talk about in interviews

#### Citations:

- Project Inspired from the following links
  - https://www.kaggle.com/msambare/fer2013
  - https://www.kaggle.com/shawon10/facial-expression-detection-cnn/data?select=fer2013.csv
  - https://www.deploymachinelearning.com/#django-and-react-tutorials





# Building Project Locally
- Create virtual environment for this project so your global python packages/dependencies are not affected
- In the virtual environment, install all the project dependencies listed in the requirements.txt file
  - "pip install -r requirements.txt"
- Go into service/server directory
  - run "python manage.py runserver" which initiates the web server to serve our project
- Go to http://127.0.0.1:8000/ to view the application local machine

      Note: Do not mess with the jupyter notebook, it will fail since this repository does not contain the data.csv file which github isn't letting me push because       it is extremely large. 

     ![image](https://user-images.githubusercontent.com/65456906/116145403-4c9e6700-a6ab-11eb-9582-6ac1d2db8e84.png)




#### Project Workflow Images


- Screen Captures


![Screen Shot 2021-04-25 at 11 30 35 AM](https://user-images.githubusercontent.com/65456906/115999524-1e8d2a00-a5ba-11eb-881d-6aed6090339b.png)

![Screen Shot 2021-04-25 at 11 31 52 AM](https://user-images.githubusercontent.com/65456906/115999529-21881a80-a5ba-11eb-9c9f-d5f102d8d1c3.png)

![Screen Shot 2021-04-25 at 11 30 56 AM](https://user-images.githubusercontent.com/65456906/115999531-2351de00-a5ba-11eb-881a-1acb36b75ee5.png)

![Screen Shot 2021-04-25 at 11 32 21 AM](https://user-images.githubusercontent.com/65456906/115999533-251ba180-a5ba-11eb-852f-b0e032901853.png)











