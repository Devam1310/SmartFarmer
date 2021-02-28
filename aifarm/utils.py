from .apps import AifarmConfig


def get_prediction(img):
    if img.shape[2] != 3:
        img = img[:, :, 0:3]

    img = img.reshape((-1, 64, 64, 3))
    pred = None
    if AifarmConfig.predictor is not None:
        pred = AifarmConfig.predictor.predict(img)
    return pred
