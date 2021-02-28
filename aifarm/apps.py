from django.apps import AppConfig
from django.conf import settings
import tensorflow.keras as keras
import logging

logger = logging.getLogger('app')


class AifarmConfig(AppConfig):
    name = 'aifarm'
    pred_classes = ['Apple___Apple_scab', 'Apple___Black_rot',
                    'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                    'Cherry_(including_sour)___healthy',
                    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                    'Corn_(maize)___Common_rust_',
                    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)',
                    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
                    'Orange___Haunglongbing_(Citrus_greening)',
                    'Peach___Bacterial_spot', 'Peach___healthy',
                    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                    'Potato___Early_blight', 'Potato___Late_blight',
                    'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
                    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch',
                    'Strawberry___healthy', 'Tomato___Bacterial_spot',
                    'Tomato___Early_blight', 'Tomato___Late_blight',
                    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
                    'Tomato___Spider_mites Two-spotted_spider_mite',
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                    'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

    simple_pred_classes = ['Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Healthy',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Healthy',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Disease-Infected',
                           'Healthy']
    try:
        predictor = keras.models.load_model(settings.MEDIA_ROOT + '/plant-disease.h5')
        logger.info('Model loaded into memory')
    except:
        predictor = None
        logger.info('Model not found')
