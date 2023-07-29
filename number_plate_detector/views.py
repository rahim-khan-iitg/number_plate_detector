from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import torch
import pandas as pd
from PIL import Image,ImageDraw
import math
from . import forms
import easyocr
import numpy as np
def read_text(arr):
    reader=easyocr.Reader(['en'])
    text=reader.readtext(arr,paragraph=True)
    return text[0][1]

def get_bounding_box(df:pd.DataFrame,img:Image):
    draw=ImageDraw.Draw(img)
    text=list()
    if len(df)==0:
        return
    for i in range(len(df)):
        (xmin,ymin,xmax,ymax)=tuple(df.iloc[i][0:4])
        xmin,xmax,ymin,ymax=math.floor(xmin),math.ceil(xmax),math.floor(ymin),math.ceil(ymax)
        draw.line((xmin,ymin)+(xmax,ymin),fill=(255,0,0),width=2)
        draw.line((xmin,ymin)+(xmin,ymax),fill=(255,0,0),width=2)
        draw.line((xmin,ymax)+(xmax,ymax),fill=(255,0,0),width=2)
        draw.line((xmax,ymin)+(xmax,ymax),fill=(255,0,0),width=2)
        cropped=img.crop((xmin,ymin,xmax,ymax))
        c=np.array(cropped)
        text.append(read_text(c))
    return text

@csrf_exempt
def home(request):
    model=torch.hub.load('ultralytics/yolov5','custom',path='media/model/best.pt')
    if request.method=="POST":
        form=forms.Image(request.POST,request.FILES)
        img=Image.open(request.FILES['image'])
        result=model(img)
        df=result.pandas().xyxy[0]
        text=get_bounding_box(df,img)
        if text==None:
            text=[]
        else:
            text=" ,".join(text)
        img.save("media/images/a.jpg")
        return render(request,"index.html",{"image":forms.Image,"encoded_image":'media/images/a.jpg',"text":text})
    return render(request,"index.html",{"image":forms.Image})