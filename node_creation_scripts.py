import json
import math
import random
import cadquery as cq
# from cadquery import Workplane
from cadquery import exporters

def get_attribute_min_max(attribute_list):
    min = math.inf
    max = - math.inf
    for attribute in attribute_list:
        attrib = float(attribute)
        if(attrib>max):max =attrib
        if(attrib<min):min =attrib
    return [min, max]

def scale_value_to_interval(v, v_min, v_max, int_min, int_max):
    v = float(v)
    return int_min + (int_max-int_min)*(v-v_min)/(v_max-v_min)

    

def make_nod(radius = 10, label = "Nodkant", text="", fontsize=8, folder="output", magnet_radius = 3.0, magnet_height = 3, glyph=None, names = []):
    #magnet shape to extract
    # text = label + "\n" + text
    if(text == "9"):text+="."
    if(text == "6"):text+="."
    if (glyph == None):
        glyph = cq.Workplane("front").circle(radius)
    
    result = glyph
    result = result.extrude(3.5)
    result = result.faces("<Z").workplane().circle(magnet_radius+1).workplane(offset=-1.0).circle(magnet_radius).loft(combine="cut").workplane(offset=-1.0).circle(magnet_radius).extrude(3,combine="cut")
    # result = result.faces(">Z").workplane().center(0, 8).text(label,fontsize,0.2,cut= False, combine = True)
    # result = result.faces(">Z").workplane().center(0, -10,).text(text,10,-0.2,cut= False, combine = True)
    result = result.faces(">Z").workplane().text(text,10,0.2,cut= False, combine = True)
    # result = result.workplane().rect(magnet_radius,magnet_height).revolve(360, tuple([0,0,0]),tuple([0,0,1]), combine = "cut")
    

    # magnet_cutout = cq.Workplane("top").rect(magnet_radius,magnet_height).revolve(360, tuple([0,0,0]),tuple([0,0,1], combine = "cut"))

    # magnet_cutout.export("mag.stl")
    # result = result.cut(magnet_cutout)


    

    # result = result.cut(magnet_cutout)

    # result = result
    # result = result.faces(">Z").workplane().circle(10).extrude(2)
    path = folder + "/" + text +".stl"
    # result.exportStl(r"" + path)
    exporters.export(result, r"" + path )
    # result.exportStl(r"" + path)
    # text.export("text.stl")

# glyph = cq.importers.importDXF(r"test.dxf").wires().toPending()
print(cq.__version__)
with open('karate.json', 'r') as file:
    data = json.load(file)

with open('names.json', 'r') as file:
    names = json.load(file)

short_names = []
for name in names["names"]:
    first = name.split(" ")[0]
    if(len(first)<6): short_names.append(first)


with open('short_names.json', 'r') as file:
    short_names = json.load(file)

print(short_names["names"])
short_names =short_names["names"]
random.shuffle(short_names)

# attribs = [node["GeneralElectionTurnout_2010"] for node in data["nodes"]]
# [min, max] = get_attribute_min_max(attribs)
radius = 15
# lbl = "0" + " "+ str(names["names"][0]).split(" ")[0]
# make_nod(radius,"0", text="Nod", folder="karate", fontsize =10)   
i = 0
for node in data["nodes"]:
        # radius = float(node["GeneralElectionTurnout_2010"]) * 10 + 10
    # radius = scale_value_to_interval(node["GeneralElectionTurnout_2010"], min, max, 10,15)
    make_nod(radius, node["id"], text=short_names[i], folder="karate", fontsize =10)    
    i+=1