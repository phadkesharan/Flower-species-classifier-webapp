from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FlowerFeatures
import joblib
import numpy as np

# Create your views here.

def main(request):
    return render(request, "MLapp/index.html")

def prediction(request):
    pl = request.POST['petal_length']
    pw = request.POST['petal_width']
    sl = request.POST['sepal_length']
    sw = request.POST['sepal_width']

    model = joblib.load('MLapp\model\MLapp\iris_model.sav')
    decoder = {1: "setosa", 2: "versicolor", 3: "virginica"}

    X = np.array((sl, sw, pl, pw), dtype=np.float16).reshape(1, -1)    

    prediction = model.predict(X)
    print(prediction)

    prediction = decoder[prediction[0]]
    print(prediction)

    #saving to model
    flower = FlowerFeatures(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw, species=prediction)
    flower.save()

    context  = {'result': prediction}
    return render(request, "MLapp/pred.html", context)


