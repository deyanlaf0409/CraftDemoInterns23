import json
import requests



def freshdesk_dump(domain, freshdesk_api_key, password, contact, headers):
    id = contact.get("unique_external_id")

    # Check if contact with same email already exists
    url = f"https://{domain}.freshdesk.com/api/v2/contacts/?unique_external_id={id}"
    response = requests.get(url, auth=(freshdesk_api_key, password), headers=headers)
    if response.status_code == 200:
        results = json.loads(response.content.decode("utf-8"))
        if results:
            # Update existing contact
            contact_id = results[0]["id"]
            url = f"https://{domain}.freshdesk.com/api/v2/contacts/{contact_id}"
            r = requests.put(url, auth=(freshdesk_api_key, password), data=json.dumps(contact), headers=headers)
            if r.status_code == 200:
                print(f"Contact with id {id} updated successfully")
            else:
                print("Failed to update contact, errors are displayed below,")
                response = json.loads(r.content.decode("utf-8"))
                print(response["errors"])

                print("x-request-id : " + r.headers['x-request-id'])
                print("Status Code : " + str(r.status_code))
            return

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

