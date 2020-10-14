#I have created this file -  Riya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    #get text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''[]{}-!"&'()*+,./:;<=>?@\^_`|\#$%'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyze_text':analyzed}
        djtext = analyzed
        
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UPPER CASE', 'analyze_text':analyzed}
        djtext = analyzed
        
    if(newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Line', 'analyze_text':analyzed}
        djtext = analyzed
        
    if(extraspaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyze_text':analyzed}
        djtext = analyzed
            
    if(removepunc!="on" and extraspaceremove!="on" and fullcaps!="on" and newlineremove!="on"):
        return HttpResponse("<h1>Please Select Any Option</h1>")

    return render(request, 'analyze.html', params)