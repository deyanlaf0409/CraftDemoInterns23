import json
import requests


def freshdesk_dump(domain, freshdesk_api_key, password, contact, headers):
    # name = contact.get("name")
    unique_id = contact.get("unique_external_id")
    print(unique_id)
    url = f"https://{domain}.freshdesk.com/api/v2/contacts/{unique_id}"
    response = requests.get(url, auth=(freshdesk_api_key, password), headers=headers)
    print(response)
    if response.status_code == 200:
        results = json.loads(response.content.decode("utf-8"))
        print(results)
        if results:
            contact_id = results[0]["id"]
            update_contact(domain, freshdesk_api_key, password, contact, headers, contact_id)
    else:
        create_contact(domain, freshdesk_api_key, password, contact, headers)



def create_contact(domain, freshdesk_api_key, password, contact, headers):
    # Create new contact if no matching contact found
    r = requests.post(f"https://{domain}.freshdesk.com/api/v2/contacts", auth=(freshdesk_api_key, password),
                      data=json.dumps(contact), headers=headers)

    if r.status_code == 201:
        print("Contact created successfully, the response is given below" + r.content.decode("utf-8"))
        print("Location Header : " + r.headers['Location'])
    else:
        print("Failed to create contact, errors are displayed below,")
        response = json.loads(r.content.decode("utf-8"))
        print(response["errors"])

        print("x-request-id : " + r.headers['x-request-id'])
        print("Status Code : " + str(r.status_code))


def update_contact(domain, freshdesk_api_key, password, contact, headers, contact_id):
    r = requests.put(f"https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}", auth=(freshdesk_api_key, password),
                     data=json.dumps(contact), headers=headers)

    if r.status_code == 200:
        print("Contact updated successfully, the response is given below", r.content)
    else:
        print("Failed to update contact, errors are displayed below,")
        response = json.loads(r.content)
        print(response["errors"])

        print("x-request-id : ", r.headers['x-request-id'])
        print("Status Code : ", r.status_code)
