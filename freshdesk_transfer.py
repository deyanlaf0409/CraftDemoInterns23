import requests
import json


def freshdesk_dump(domain, freshdesk_api_key, password, contact_info, headers):
    r = requests.post("https://" + domain + ".freshdesk.com/api/v2/contacts", auth=(freshdesk_api_key, password),
                      data=json.dumps(contact_info), headers=headers)

    if r.status_code == 201:
        print("Contact created successfully, the response is given below" + r.content.decode("utf-8"))
        print("Location Header : " + r.headers['Location'])
    else:
        print("Failed to create contact, errors are displayed below,")
        response = json.loads(r.content.decode("utf-8"))
        print(response["errors"])

        print("x-request-id : " + r.headers['x-request-id'])
        print("Status Code : " + str(r.status_code))
