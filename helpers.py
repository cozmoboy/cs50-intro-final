import os
import requests
import urllib.parse
import math
import classes
import random
import data

from flask import redirect, render_template, request, session


# from flask import redirect, render_template, request, session
# from functools import wraps
# from datetime import datetime
NAMES = ["Rufus", "Bagonia", "Chesterfield", "Muchacho", "Nacho", "Rebecca", "Ben", "Ola", "Rachel", "Sadie", "Zbyszek", "Halszka", "Kuba", "Armita", "Minka", "Zuzu", "Howard", "Margie", "Zeni", "Ruby", "Max"]




def savePC(pc):
    session["pc"] = pc
    return None

def arrayFromClassChoices(pcClass, keyName):
    myArray = []
    if pcClass[keyName]["choose"]:
        specs = pcClass[keyName]["list"]
        for i in range(pcClass[keyName]["number"]):
            x = random.choice(specs)
            myArray.append(x)
            specs.remove(x)
    return myArray

def classWithName(name):
    for pcClass in data.GENRES:
        if pcClass["name"] == name:
            return pcClass
    return {"name": "oops"}

    

def makePCofClass(classStr, genre):
    pcClass = classWithName(classStr)
    pc = classes.PC()
    pc.name = random.choice(NAMES) + " the " + pcClass["name"]
    pc.strength = random.randint(1, 6)
    pc.dexterity = random.randint(1, 6)
    pc.intel = random.randint(1, 6)
    pc.presence = random.randint(1, 6)
    pc.sanity = random.randint(1, 6)
    pc.hp = pc.strength + 6
    pc.currentHP = pc.hp
    pc.species = random.choice(genre["species"])
    pc.animalStock = "None"
    pc.cClass = pcClass["name"]
    pc.specials = pcClass["specials"] + arrayFromClassChoices(pcClass, "specialsXtra")
    pc.professions = arrayFromClassChoices(pcClass, "professions")
    pc.knacks = arrayFromClassChoices(pcClass, "knacks")
    pc.inventory = pcClass["xtraGear"] + genre["basicKit"]
    pc.resources = arrayFromClassChoices(pcClass, "resources")
    pc.notes = pcClass["notes"]
    pc.weaponPro = arrayFromClassChoices(pcClass, "weaponPros")
    pc.weaponMast = arrayFromClassChoices(pcClass, "weaponMasteries")
    pc.armorPro = pcClass["armor"]
    pc.money = pcClass["startCash"] + genre["startingCash"]
    pc.spells = arrayFromClassChoices(pcClass, "spells")
    pc.languages = genre["commonLanguages"] + arrayFromClassChoices(pcClass, "weaponMasteries") 
    return pc
    
    
    
    
    
    
    
            
            
    






    