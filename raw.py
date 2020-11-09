import requests

ofsc42 = 'YzIwNTk3NjFiN2E5N2JhYTZiMDE3NjhlNTNhYzZmZWQwMDAtZWNhY2NmNzc4N2ZlNmVmNjJiMzE2NmE5YzM4MDI2YmItYzc1OTg4MDMwMzc1YWU3NWMwM2ZkMTU3MjUwM2IzODk'
trust = '$fast$sha256$df13ae8cbbeb9ded2a25187f33a2e1f2215f3e86ad539f7c8134647eb492ee0c.e25c3727f19face292ee04c544d5d27d'


def search_by_code(code: str):
    cookies = {
        'build': '20.5.13.0.14',  # TODO
        'lastAuthId': 'toa_._telefonica-pe_.__._mobility',  # TODO
        'disableAppCache': '1',  # TODO
        'ofsc42': ofsc42,  # TODO
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-PLATFORM': '1',
        'X-OA': '2',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://telefonica-pe.etadirect.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://telefonica-pe.etadirect.com/mobility/',
        'Accept-Language': 'en,es;q=0.9,es-ES;q=0.8,la;q=0.7,fr;q=0.6,pt;q=0.5',
    }

    params = (
        ('m', 'search'),
        ('a', 'search'),
    )

    data = {
        'from': '',
        'size': '60',
        'searchFields[137]': 'true',
        'searchFields[309]': 'true',
        'searchFields[341]': 'true',
        'searchFields[368]': 'true',
        'searchFields[appt_number]': 'true',
        'searchFields[customer_number]': 'true',
        'searchFields[cname]': 'true',
        'searchFields[cemail]': 'true',
        'searchFields[cphone]': 'true',
        'searchFields[ccell]': 'true',
        'searchFields[caddress]': 'true',
        'searchValue': code,
        'searchDate': 'at_all',
        'skip_delta': '0',
        '__protocol': '5',
        'dv': '{"c":"337|20201107161816","q":"2309123|20201107162858"}',
        'pid': '0',
        'u': 'HACKATON14',
        'f': 'json',
        'pids': '[]',
        'aids': '[]',
        'restriction': '0',
        'fakeIds': '{}',
        'trust': trust,  # TODO
        'fakeIdsClean': '0',
        'limitActivitiesByPool[notscheduled]': '5'
    }

    response = requests.post('https://telefonica-pe.etadirect.com/mobility/index.php',
                             headers=headers, params=params, cookies=cookies, data=data)
    return response.json()


def retrieve_data_by_code(aid: str, pid: str):
    cookies = {
        'disableAppCache': '1',
        'build': '20.5.13.0.14',
        'lastAuthId': 'toa_._telefonica-pe_.__._mobility',
        'ofsc42': ofsc42,
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'X-PLATFORM': '1',
        'X-OA': '2',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryQztSKdSTCAtACZZ3',
        'Origin': 'https://telefonica-pe.etadirect.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://telefonica-pe.etadirect.com/mobility/',
        'Accept-Language': 'en,es;q=0.9,es-ES;q=0.8,la;q=0.7,fr;q=0.6,pt;q=0.5',
    }

    params = (
        ('m', 'sync'),
        ('a', 'write'),
        ('ajax', '1'),
        ('window_id', '1604882883-0000-0000'),
    )

    data = '$------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="__protocol"\r\n\r\n5\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="dv"\r\n\r\n{"q":"28140|2021107162858"}\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="pid"\r\n\r\n'+pid+'\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="u"\r\n\r\nHACKATON14\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="f"\r\n\r\njson\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="pids"\r\n\r\n[]\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="aids"\r\n\r\n["9203927"]\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="restriction"\r\n\r\n0\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="qid"\r\n\r\nundefined\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="fakeIds"\r\n\r\n{}\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="trust"\r\n\r\n' + \
        trust + \
        '\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="fakeIdsClean"\r\n\r\n0\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="dq"\r\n\r\n2020-10-09\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="date"\r\n\r\n2020-10-09\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="dispatcher"\r\n\r\n1\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="mandatory[1][0]"\r\n\r\n9203927\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="limitActivitiesByPool[notscheduled]"\r\n\r\n5\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3\r\nContent-Disposition: form-data; name="skip_delta"\r\n\r\n0\r\n------WebKitFormBoundaryQztSKdSTCAtACZZ3--\r\n'

    response = requests.post('https://telefonica-pe.etadirect.com/mobility/',
                             headers=headers, params=params, cookies=cookies, data=data)
    return response.json()
