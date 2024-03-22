from requests import post, get

#get token of https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335
client_id = "QvuCFTKhs2wpUlNt2fl7JGR7wGfMiYmA"
client_secret = "NBJA7tZgYugddGoM"

url = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

response = post(url, headers=headers, data=data)

print(response.json())