from __future__ import unicode_literals

import netaddr

# http proxy

HTTP_PROXY_ALLOWED_CIDRS = [
    netaddr.IPNetwork('127.0.0.1'),
    netaddr.IPNetwork('10/8'),
]

HTTP_PROXY_HEALTH = {
    'file_path': None,
}

HTTP_CLIENT = {
    'num_pools': 1,
    'pool': {}
}

TRACE_ID_HTTP_HEADER = 'X-Balanced-Guru'
