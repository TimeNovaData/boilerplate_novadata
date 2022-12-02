# Itens fixos do breadcrumb que podem ser reutilizados

alterar_dados = {
    "name": "Alterar dados",
    "slug": "alterar_dados",
    "url_name": "",
}


detalhes_simples = {
    "name": "Detalhes",
    "slug": "detalhes",
    "url_name": "",
}


def make_detalhes(url_name, url_params=[], get_params={}):
    return {
        "name": "Detalhes",
        "slug": "detalhes",
        "url_name": url_name,
        "url_params": url_params,
        "get_params": get_params,
    }
