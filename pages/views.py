from django.shortcuts import render

# Create your views here.

def error_page(request):
    return render(request, "404.html")

def checkout(request):
    return render(request, "checkout.html")

def faq(request):
    return render(request, "faq.html")

def privacy_policy(request):
    return render(request, "privacy-policy.html")

def return_policy(request):
    return render(request, "return-policy.html")

def terms_conditions(request):
    return render(request, "terms-conditions.html")