from django.shortcuts import render

import requests as req

def main_page(request):
    return render(request, 'login/login.jsp')

