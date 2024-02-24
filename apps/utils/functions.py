from typing import Dict, List, Tuple, Union

from django.urls import reverse_lazy


def breadcrumbs_format(
    crumbs: List[Tuple[str, Union[str, None]]]
) -> List[Dict]:
    crumb_list = []
    for crumb in crumbs:
        crumb_dict = {}
        crumb_name = crumb[0]
        crumb_url = crumb[1] if crumb[1] else '#'
        crumb_dict['name'] = crumb[0]
        crumb_dict['url'] = (
            reverse_lazy(crumb_url) if ':' in crumb_url else crumb_url
        )

        crumb_list.append(crumb_dict)

    return crumb_list
