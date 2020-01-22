from django.shortcuts import render

from my_app.models import Search
  

# Create your views here.
def home(request):
  my_title = 'FT CraigsList'
  searches = Search.objects.all().order_by('-created')[:10:2]
  context = {
      'title': my_title,
      'searches': searches,
  }
  return render(request, 'base.html', context)

