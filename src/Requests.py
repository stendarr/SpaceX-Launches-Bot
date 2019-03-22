import urllib.request, json


def make_request(url, args):
    if args:
        url += "?filter="
        for arg in args:
            url += arg + ","
    request = urllib.request.urlopen(url)
    raw_data = request.read()
    encoding = request.info().get_content_charset('utf8')
    return json.loads(raw_data.decode(encoding))


def unpack(mydir):
    for i, j in mydir.items():
        if type(j) == dict:
            for m, n in j.items():
                mydir[m] = n
            del mydir[i]
    return mydir


# Flight number, mission name, launch date and time, rocket used, launch site name
def next_launch():
    args = ["flight_number", "mission_name", "launch_date_utc", "launch_date_local", "rocket/rocket_name",
            "launch_site/site_name_long"]
    data = make_request("https://api.spacexdata.com/v3/launches/next", args)
    data = unpack(data)
    return data


# Flight number, mission name, launch date and time, rocket used, launch site name
def latest_launch():
    args = ["flight_number", "mission_name", "launch_date_utc", "launch_date_local", "rocket/rocket_name",
            "launch_site/site_name_long"]
    data = make_request("https://api.spacexdata.com/v3/launches/latest", args)
    data = unpack(data)
    return data
