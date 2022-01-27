class Test:
    def test_one(self, url):
    import requests
    url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/700006917"
    response = requests.get(url)
    print(response.json())

    def test_two(self):
    import requests
    url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/700006917"
    response = requests.get(url)
    code = response.status_code
    assert code == 200, "Expected status code is 200"
    print(response)
    print(response.json())

    def test_three(self):
    import requests
    url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/70000000000"
    response = requests.get(url)
    code = response.status_code
    print(response)
    assert code == 404, "Expected status code is 404"
    print(response.content)

    def test_four(self):
    import requests
    url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/!№;№%;:?:*??(****)"
    response = requests.get(url)
    code = response.status_code
    print(response)
    assert code == 400, "Expected status code is 400"
    print(response.content)

    def test_five(self):
    import requests
    url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/bjythfj"
    response = requests.get(url)
    code = response.status_code
    print(response)
    assert code == 400, "Expected status code is 400"
    print(response.content)

""" 
url = "https://allinone-ota.api.nutsservices.nl/api/Fulfillment/Offer/700006910"
response = requests.get(url)
code = response.status_code
assert code == 200 , "Expected status code is 200"
print(response)
print(response.headers)
"""