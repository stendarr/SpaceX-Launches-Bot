import re
from src.FormatHTML import strHTML

def beautifier(mystring):
    mystring = strHTML(mystring)
    if "Falcon" in mystring:
        name_url = mystring.addURL("https://it.wikipedia.org/wiki/" + mystring.replace(" ", "_"))
        return name_url
    if re.match("[0-9-]{10}[T].*", mystring):
        return date_and_time_beautifier(mystring)
    mystring = str(mystring).title()
    mystring = mystring.replace("_", " ")
    return mystring

def key2readable_text(mykey):
    beautydict = {
        "flight_number": "Flight number",
        "mission_name": "Mission name",
        "launch_date_utc": "Launch date (UTC time)",
        "launch_date_local": "Launch date (local time)",
        "rocket_name": "Rocket",
        "site_name_long": "Launch site"
    }
    return beautydict[mykey]

def date_and_time_beautifier(date_string):
    date_string = date_string.replace("T", "-")
    date_string = date_string.replace("Z", "")
    date_splitted = date_string.split("-")
    date = date_splitted[0] + "/" + date_splitted[1] + "/" + date_splitted[2]
    time_splitted = (date_splitted[3].replace(".", ":")).split(":")
    time = time_splitted[0] + ":" + time_splitted[1] + ":" + time_splitted[2]
    return date + " " + time

def getString(mydir):
    out = ""
    for i, j in mydir.items():
        out += key2readable_text(i) + ": " + beautifier(j) + "\n"
    return out

