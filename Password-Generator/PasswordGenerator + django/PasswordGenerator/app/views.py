from django.http import HttpResponse
from django.template import loader
import random

# def index(request):
#   template = loader.get_template('index.html')
#   return HttpResponse(template.render())



def index (request):
  nums = [0,1,2,3,4,5,6,7,8,9]
  lowercaseـletters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  capitalـletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  symbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '+' ]

  lists = [nums , lowercaseـletters , capitalـletters , symbols]
  pass_list = []

  for i in range(12):
    pass_list.append(random.choices(lists[random.randint(0,3)]))

  x = []
  for i in pass_list:
    x.append(i[0])

  resulte = ''.join([str(elem) for elem in x])

  context = {
    "resulte" : resulte
  }

  template = loader.get_template('index.html')
  return HttpResponse(template.render(context))

  # return HttpResponse(resulte)