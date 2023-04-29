import requests
import json

api_key = "YOUR_API_KEY"
domain = "YOUR_DOMAIN"
password = "x"

contact_info = {"name": "Example User", "email": "api_v2_user_03@example.com"}
headers = {"Content-Type": "application/json"}

r = requests.post("https://" + domain + ".freshdesk.com/api/v2/contacts", auth=(api_key, password), data=json.dumps(contact_info), headers=headers)

if r.status_code == 201:
    print("Contact created successfully, the response is given below" + r.content.decode("utf-8"))
    print("Location Header : " + r.headers['Location'])
else:
    print("Failed to create contact, errors are displayed below,")
    response = json.loads(r.content.decode("utf-8"))
    print(response["errors"])

    print("x-request-id : " + r.headers['x-request-id'])
    print("Status Code : " + str(r.status_code))
