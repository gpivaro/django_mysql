from django.shortcuts import render
from .models import TempHumMeas
from django.views.generic import ListView

# Create your views here.
def index(request):
    context = {"posts": TempHumMeas.objects.order_by("-time")[:5]}
    return render(request, "temperaturemonitor/home.html", context)

    # class PostListView(ListView):
    #     model = Post
    #     template_name = "temperaturemonitor/home.html"  # <app>/<model>_<viewtype>.html
    #     context_object_name = "posts"
    #     ordering = ["-date_posted"]  # query database
    #     paginate_by = 5
