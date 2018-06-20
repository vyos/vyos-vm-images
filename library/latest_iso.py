#!/usr/bin/env python3

import os
import sys
from lxml import html
import requests
import json
from ansible.module_utils.basic import AnsibleModule

BASE_URL = 'https://downloads.vyos.io/'
PAGE_URL = BASE_URL+'?dir=rolling/current/amd64'


def run_module():
    result = dict(changed=False)
    module = AnsibleModule(argument_spec=dict())

    page = requests.get(PAGE_URL)
    tree = html.fromstring(page.content)
    path = '//*[@id="directory-listing"]/li/a[1]/@href'
    isos = [x for x in tree.xpath(path) if os.path.splitext(x)[1] == '.iso']
    latest_iso = os.path.join(BASE_URL, isos[-1])
    result['latest_iso'] = latest_iso

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
