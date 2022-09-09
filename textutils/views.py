from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("about world")

def website(request):
    return HttpResponse("""<a href="https://www.w3schools.com/html/html_links.asp">youtube</a>""")

def analyze(request):
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    fullcaps=request.POST.get("fullcaps","off")
    swap=request.POST.get("swap","off")
    space=request.POST.get("space","off")
    charcounter=request.GET.get("charcounter","off")
    
    if removepunc=="on":
        punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in djtext:
            if char not in punctuations:
                analyze=analyze+char
        params = {'purpose':'removed punctuations','Analyzed_text':analyze}
        return render(request,"analyze.html",params)

    elif  fullcaps=="on":
        analyze=""
        for char in djtext:
            analyze=analyze + char.upper()
        params = {'purpose':'made the text upper','Analyzed_text':analyze}
        return render(request,"analyze.html",params)

    elif swap=="on":
        swap=""
        for char in djtext:
            swap= swap + char.swapcase()
        params={"purpose":"Text Swapper","Analyzed_text":swap}
        return render(request,'analyze.html',params)

    elif space=="on":
        analyze=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyze=analyze+char
        params={"purpose":"Space remover","Analyzed_text":analyze}
        return render(request,'analyze.html',params)
    
    elif charcounter=="on":
        analyze=""
        for i in djtext:
            if i==" ":
                pass
            else:
                analyze=analyze+i
        count=len(analyze)
        params={"purpose":"Space remover","Analyzed_text":count}
        return render(request,'analyze.html',params)
        

    else:
        return HttpResponse("error")
    

# def capfirst(request):
#     return render(request,'capfirst.html')

# def newlineremover(request):
#     return HttpResponse("newlineremove")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")