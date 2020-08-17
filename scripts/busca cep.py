def script(**kwargs):
    import requests

    cep = kwargs["PARM"]
    url = "http://viacep.com.br/ws/{}/json/"
    if cep:
        response = requests.get(url=url.format(cep))
        if response.status_code == 200:
            content = response.json()
            logradouro = content["logradouro"]
            bairro = content["bairro"]
            cidade = content["localidade"]
            return {
                "cep": cep,
                "logradouro": logradouro,
                "bairro": bairro,
                "cidade": cidade,
            }

if __name__ == "__main__":
    script(**{"PARM": "14802120"})

