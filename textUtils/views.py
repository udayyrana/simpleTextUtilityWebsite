from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-.//:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed To Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcounter == "on":
        count = 0
        for char in range(len(djtext)):
            if djtext[char] == " ":
                pass
            else:
                count += 1
        params = {'purpose': 'Character Counter', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
