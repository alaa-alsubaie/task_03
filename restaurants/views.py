from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [ 
                 {"restaurant_name":"Mac" ,"Food_type":"Junk "} ,
			     {"restaurant_name":"Salad" ,"Food_type":"Healthy "},
			     {"restaurant_name":"coco" ,"Food_type":"Sweet"}
			   ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{
    "restaurant_name":"coco",
    "Food_type":"Sweet",
    "Location":"Avenues mall"
    }

    }
    return render(request, 'detail.html', context)
