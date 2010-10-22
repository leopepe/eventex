from django.shortcuts import render_to_response
from django.conf import settings

def homepage(request):
    """ 
    #
    # Manual Django render method.
    # 
    #  needs: from django.template import loader, Context
    #         from django.http import HttpResponse

    t = loader.get_template('index.html')
    c = Context()

    content = t.render(c)

    return HttpResponse(content)
    """
    context = {'MEDIA_URL': settings.MEDIA_URL}

    return render_to_response('index.html', context)
