from django.shortcuts import render
from django.http import Http404, JsonResponse
from .forms import UploadImageForm
from PIL import Image
import numpy as np
import logging
from .utils import get_prediction
from .apps import AifarmConfig

logger = logging.getLogger('app')


def plantai(request):
    return render(request, 'plantai.html')


def predict(request):
    context = {}
    logger.info('inside predict')
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        logger.info('inside POST')
        if form.is_valid():
            logger.info('form is valid')
            image = form.cleaned_data.get("image")
            image = Image.open(image)
            img = np.array(image.resize((64, 64), Image.ANTIALIAS))
            logger.info(img.shape)
            preds = get_prediction(img)
            class_ = 'Model currently unavailable'
            if preds is not None:
                class_ = AifarmConfig.simple_pred_classes[np.argmax(preds[0])]
            logger.info(preds)
        return render(request, 'prediction.html', {'class': class_})

    else:
        return Http404()
