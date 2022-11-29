import os
import requests
import urllib.parse
import math
import classes
import random
import dataBG

from flask import redirect, render_template, request, session


# from flask import redirect, render_template, request, session
# from functools import wraps
# from datetime import datetime
NAMES = ["Rufus", "Bagonia", "Chesterfield", "Muchacho", "Nacho", "Rebecca", "Ben", "Ola", "Rachel", "Sadie",
         "Zbyszek", "Halszka", "Kuba", "Armita", "Minka", "Zuzu", "Howard", "Margie", "Zeni", "Ruby", "Max"]


def savePC(pc):
    session["pc"] = pc
    return None


def arrayFromClassChoices(pcClass, keyName):
    myArray = []
    if pcClass[keyName]["choose"]:
        specs = pcClass[keyName]["list"].copy()
        for i in range(pcClass[keyName]["number"]):
            x = random.choice(specs)
            myArray.append(x)
            specs.remove(x)
    return myArray


def dictionaryWithNameFromArray(name, array):
    for dict in array:
        if dict["name"] == name:
            return dict
    return {"name": "oops"}


def showMe(myString, xObect):
    print(".........HERE IT COMES................", flush=True)
    print("......................................", flush=True)
    print(myString, flush=True)
    print("********.", flush=True)
    print(xObect, flush=True)
    print("......................................", flush=True)
    print(".........END..........................", flush=True)


def makePCofClass(classStr, genreStr):
    pcClass = dictionaryWithNameFromArray(classStr, dataBG.CLASSES)
    genre = dictionaryWithNameFromArray(genreStr, dataBG.GENRES)
    showMe("this is the class: ", pcClass)
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
    pc.specials = arrayOfDictionariesWithNames(pcClass["specials"], dataBG.SPECIALS) + arrayOfDictionariesWithNames(arrayFromClassChoices(pcClass, "specialsXtra"), dataBG.SPECIALS)
    pc.professions = arrayOfDictionariesWithNames(arrayFromClassChoices(pcClass, "professions"), dataBG.SPECIALS)
    pc.knacks = arrayOfDictionariesWithNames(arrayFromClassChoices(pcClass, "knacks"), dataBG.PROFESSIONS)
    pc.inventory = pcClass["xtraGear"] + genre["basicKit"]
    pc.resources = arrayFromClassChoices(pcClass, "resources")
    pc.notes = pcClass["notes"]
    pc.weaponPro = arrayFromClassChoices(pcClass, "weaponPros")
    pc.weaponMast = arrayFromClassChoices(pcClass, "weaponMasteries")
    pc.armorPro = pcClass["armor"]
    pc.money = pcClass["startCash"] + genre["startingCash"]
    pc.spells = arrayOfDictionariesWithNames(arrayFromClassChoices(pcClass, "spells"), dataBG.SPELLS)
    pc.languages = genre["commonLanguages"] + arrayFromClassChoices(pcClass, "xtraLang")
    pc.genre = genreStr
    savePC(pc)
    return pc

def setCurrentHP(hpNew):
    pc = session.get("pc")
    pc.currentHP = hpNew
    savePC(pc)
    return None



def arrayOfDictionariesWithNames(names, dataArray):
    newArray = []
    for name in names:
        newArray.append(dictionaryWithNameFromArray(name, dataArray))
    return newArray