from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id=0
    feature1.name='Car'
    feature1.details = 'car is a  4 wheeler'
    feature1.is_true = False

    feature2 = Feature()
    feature2.id=1
    feature2.name='bike'
    feature2.details = 'bike is a 2 wheeler'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id=2
    feature3.name='lorry'
    feature3.details = 'lorry is a 6 wheeler'
    feature3.is_true = True

    feature4 = Feature()
    feature4.id=3
    feature4.name='train'
    feature4.details = 'train has many wheels'
    feature4.is_true = False

    features = [feature1,feature2,feature3,feature4]

    return render(request,'index.html',{'features': features})