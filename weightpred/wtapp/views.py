from django.shortcuts import render
from .form import weightform
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.contrib import messages
from .models import predictor
from .serializers import predictorSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


class WeightsView(viewsets.ModelViewSet):
    queryset = predictor.objects.all()
    serializer_class = predictorSerializers


#@api_view(["POST"])
def predictweight(unit):
    try:
        mdl = joblib.load("weightmodel.pkl")
        print(unit)
        y_pred = mdl.predict(unit)
        print("ypred",y_pred)
        newdf = pd.DataFrame(y_pred, columns=['weight'])
        return newdf
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
def clnvalue(df):
    nlist=[]
    value=int(df['heightfeet'])*12+int(df['heightinches'])
    nlist.append(value)
    print("nlist=",nlist)
    height=pd.DataFrame(nlist)
    age=pd.DataFrame(df['age'])
    print("height=",height," age=",age)
    newdf=pd.concat([height,age],axis=1)
    print("newdf=",newdf)
    return newdf
def weightreq(request):
    if request.method=='POST':
        form=weightform(request.POST)
        if form.is_valid:
            mydict=(request.POST).dict()
            df=pd.DataFrame(mydict,index=[0])
            result=predictweight(clnvalue(df))
            messages.success(request,'Your Weight should be: {} kg'.format(result.iloc[0,0]))
    form=weightform()
    return render(request,'forms/cxform.html',{'form':form})

