import joblib
from tensorflow.keras.preprocessing import image
import numpy as np

class classifier:
    def __init__(self):
        #Dataset 1 predictive models
        self.model =  joblib.load("/Users/ds070111/Documents/GitHub/PythonProject/service/server/ml/trained_model.joblib")

    def emotion_analysis(self, emotions):
        objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        print("Predicted Emotion : ", objects[np.argmax(emotions)])
        print("Probability :",np.max(emotions))

    def make_prediction(self):
        img = image.load_img('/Users/ds070111/Documents/GitHub/PythonProject/service/server/ml/Data/test.jpeg', grayscale=True, target_size=(48, 48))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        x /= 255

        custom = self.model.predict(x)
        print(custom[0])
        self.emotion_analysis(custom[0])
