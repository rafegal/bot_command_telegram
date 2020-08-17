def script(**kwargs):
    import requests

    number = kwargs["PARM"]
    url = "http://pokeapi.co/api/v2/pokemon/%s" % number
    response = requests.get(url=url)
    json_response = response.json()
    name = json_response["forms"][0]["name"]
    name = str(name).title()
    image = json_response["sprites"]["front_default"]
    binds = {}
    binds["name"] = name
    binds["image"] = image
    return binds
