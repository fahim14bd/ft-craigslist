import requests

from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus

from .models import Search


BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def search(request):
  searches = Search.objects.all().order_by('-created')[:10:2]
  # if request.method == 'GET':
  #   search = request.GET.get('search')
  # elif request.method == 'POST':
  #   search = request.POST.get('search')

  search = request.GET.get('search')
  Search.objects.create(search=search)
  search_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
  print(search_url)
  response = requests.get(search_url)
  data = response.text
  soup = BeautifulSoup(data, features='html.parser')
  post_listings = soup.find_all('li', {'class': 'result-row'})

  final_postings = []
  
  for post in post_listings:
    post_title = post.find(class_='result-title').text
    post_url = post.find('a').get('href')

    if post.find(class_='result-price'):
        post_price = post.find(class_='result-price').text
    else:
        post_price = 'N/A'


    if post.find(class_='result-image').get('data-ids'):
        post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
        post_image_url = BASE_IMAGE_URL.format(post_image_id)
    else:
        post_image_url = 'https://www.craigslist.org/images/peace.jpg'


    final_postings.append((post_title, post_url, post_price, post_image_url))


  context = {
    'search': search,
    'searches': searches,
    'final_postings': final_postings,
    'title': 'FT CraigsList'
  }

  return render(request, 'my_app/index.html', context)
  