import requests
import json


def freshdesk_dump(domain, freshdesk_api_key, password, contact_info, headers):
    email = contact_info.get("email")
    if not email:
        raise ValueError("Missing email in contact_info")

    # Check if contact with same email already exists
    url = f"https://{domain}.freshdesk.com/api/v2/contacts/autocomplete?term={email}"
    response = requests.get(url, auth=(freshdesk_api_key, password), headers=headers)
    if response.status_code == 200:
        results = json.loads(response.content.decode("utf-8"))
        if results:
            print(f"Contact with email {email} already exists, exiting...")
            return

    # Create new contact if no matching contact found
    r = requests.post(f"https://{domain}.freshdesk.com/api/v2/contacts", auth=(freshdesk_api_key, password),
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
