import sys
from django.shortcuts import render
from .generate_map import *

# Create your views here.


def ldhaplomap_input(request):
    return render(request, "ld_haplo_home.html")


def ldhaplomap_out(request):
    population = request.GET["userinput2"]
    locus, raw_pos = request.GET["userinput1"].split(':')
    
    extended_pos = []
    
    positions = raw_pos.strip().split(',')
    positions = list(map(str,positions))
    for x in positions:
        if x.find('-') != -1:
            start_stop = x.split('-')
            extended_pos.extend(list(range(int(start_stop[0]),int(start_stop[1])+1)))
        else:
            extended_pos.append(x)
    
    extended_pos.sort(key=int)
    
    encoded_file = create_graph(population,locus,extended_pos)
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