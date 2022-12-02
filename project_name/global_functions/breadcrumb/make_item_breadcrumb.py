from global_functions.redirect import reverse_lazy_plus


def make_item_breadcrumb(item: dict) -> dict:
    return {
        "name": item["name"],
        "slug": item["slug"],
        "link": reverse_lazy_plus(
            item["url_name"],
            url_params=item["url_params"] if "url_params" in item else [],
            get_params=item["get_params"] if "get_params" in item else {}
        ).url
        if item["url_name"]
        else "",
    }
