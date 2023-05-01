import sys
from django.shortcuts import render
from .generate_map import *

# Create your views here.


def ldhaplomap_input(request):
    return render(request, "ld_haplo_home.html")


def ldhaplomap_out(request):
    population = request.GET["userinput2"]
    locus, raw_pos = request.GET["userinput1"].split(':')
    
    positions = raw_pos.strip().split(',')
    
    encoded_file = create_graph(population,locus,positions)
    
    return render(
        request,
        "ld_haplo_out.html",
        {
            "population": population,
            "user_input": request.GET["userinput2"],
            "encoded_file": encoded_file
        },
    )