__author__ = "rafeg"


def script(**kwargs):
    import random

    vendas = random.randrange(1000, 10000)
    return {"vendas": vendas}


if __name__ == "__main__":
    script()
