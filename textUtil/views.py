from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text', 'default')
    removepun=request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    lineremover = request.GET.get('lineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    # analyzed=djtext

    if removepun=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (lineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed += char

        params = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char


        params = {'purpose': 'ExtraSpaceremover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charcounter == "on"):
        count=0

        for char in djtext:
            if char.isalpha():
                count+=1

        params = {'purpose': 'counting character', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("ERROR")
    params={'purpose':'Remove Punctuations','analyzed_text': analyzed}
    return render(request,'analyze.html',params)
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremove(request):
#     return HttpResponse("newlineremover")
# def spaceremove(request):
#     return HttpResponse('''spaceremover<a href="http://127.0.0.1:8000/">home</a>''')
# def charcount(request):
#     return HttpResponse("char count")

