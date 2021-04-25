import joblib
from tensorflow.keras.preprocessing import image
import numpy as np
import os.path

class classifier:
    def __init__(self):
        #Dataset 1 predictive models
        self.model =  joblib.load("/Users/ds070111/Documents/GitHub/PythonProject/service/server/ml/trained_model.joblib")

    def emotion_analysis(self, emotions):
        objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        print("Predicted Emotion : ", objects[np.argmax(emotions)])
        print("Probability :",np.max(emotions))
        return (objects[np.argmax(emotions)], np.max(emotions))

    def make_prediction(self, f):
        f = os.path.abspath(os.path.dirname(__file__))+ '/static/images/'+f
        img = image.load_img(f, grayscale=True, target_size=(48, 48))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        x /= 255

        custom = self.model.predict(x)
        print(custom[0])
        return self.emotion_analysis(custom[0])
