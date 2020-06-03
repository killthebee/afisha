from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template import loader


def render_fp(request):
    template = loader.get_template('index.html')
    context = {}
    render_page = template.render(context, request)
    return HttpResponse(render_page)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_fp),
]
