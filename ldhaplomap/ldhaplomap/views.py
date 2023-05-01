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
    unencoded_file = encoded_file.decode('utf-8')
    
    return render(
        request,
        "ld_haplo_out.html",
        {
            "population": population,
            "loc_pos": request.GET["userinput1"],
            "heatmap": unencoded_file
        },
    )