import os
import requests
import urllib.parse
import math

from flask import redirect, render_template, request, session


# from flask import redirect, render_template, request, session
# from functools import wraps
# from datetime import datetime

def savePC(pc):
    session["pc"] = pc
    return None

def getPC():
    return session.get("pc")