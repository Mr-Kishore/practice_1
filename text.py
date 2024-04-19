import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('sign_langage_model.h5')

classes = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cap = cv2.VideoCapture(0)

while True:
    #capture frame by frame
    ret, frame = cap.read()

    #preprocess the frame
    resized_frame = cv2.resize(frame,(224, 224))
    normalized_frame = resized_frame / 255.0
    expanded_frame = np.expand_dims(normalized_frame, axis=0)

    #recognize sign language from the frame
    prediction = model.predict(expanded_frame)
    predict_class = classes[np.argmax(prediction)]

    #display the captured frame
    cv2.inshow('sign language Recognitio', frame)

    #exit if "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #release the capture
    cap.release()
    cv2.destroyAllWindows()