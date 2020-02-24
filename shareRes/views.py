from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(req):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants': restaurants}
    return render(req, 'shareRes/index.html', content)


def restaurantDetail(req, res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'restaurant': restaurant}
    return render(req, 'shareRes/restaurantDetail.html', content)


def restaurantCreate(req):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(req, 'shareRes/restaurantCreate.html', content)


def restaurantUpdate(req, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'categories': categories, 'restaurant': restaurant}
    return render(req, 'shareRes/restaurantUpdate.html', content)


def Delete_restaurant(req):
    res_id = req.POST['resId']
    restaurant = Restaurant.objects.get(id=res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))


def Update_restaurant(req):
    resId = req.POST['resId']
    change_category_id = req.POST['resCategory']
    change_category = Category.objects.get(id=change_category_id)
    change_name = req.POST['resTitle']
    change_link = req.POST['resLink']
    change_content = req.POST['resContent']
    change_keyword = req.POST['resLoc']
    before_restaurant = Restaurant.objects.get(id=resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))


def Create_restaurant(req):
    print(req)
    category_id = req.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = req.POST['resTitle']
    link = req.POST['resLink']
    content = req.POST['resContent']
    keyword = req.POST['resLoc']

    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link,
                         restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))


def categoryCreate(req):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(req, 'shareRes/categoryCreate.html', content)


def Create_category(req):
    category_name = req.POST['categoryName']
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))


def Delete_category(req):
    print("req : ", req.POST.keys())
    category_id = req.POST['categoryId']
    print(category_id)
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

