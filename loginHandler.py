from http.client import HTTPSConnection
from base64 import b64encode
#This sets up the https connection
c = HTTPSConnection("hackillinois.climate.com")
#we need to base 64 encode it 
#and then decode it to acsii as python 3 stores it as a byte string
#userAndPass = b64encode(b"dpk28065pc31d0:5mt8jml6utleeuff9paeel5f41").decode("ascii")
token_json = b'{"access_token":"83cdaa6b-4cfd-4c8c-a2b0-fd82f2496369","token_type":"bearer","expires_in":604799,"scope":"openid user","site":{"siteCode":"261e40b5169a72c05273869d"},"id_token":"eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5jbGltYXRlLmNvbS9hcGkvb2F1dGgvdG9rZW4iLCJhdWQiOiJkcGsyODA2NXBjMzFkMCIsImV4cCI6MTQ1NjAwMzE3OCwiaWF0IjoxNDU2MDAyNTc4LCJhdXRoX3RpbWUiOjE0NTYwMDI1NzgsInVzZXJfaWQiOiIxNTEwNjkiLCJzdWIiOiIxNTEwNjkiLCJlbWFpbCI6Imh1bWJsZXZsYWRpbWlydGhlZ3JlYXRAZ214LmNvbSIsImFkZHJlc3MiOnt9LCJyb2xlcyI6WyJjbGllbnQiXSwiZmFtaWx5X25hbWUiOiJTb2NpZXR5IiwiZ2l2ZW5fbmFtZSI6IlRoZSJ9.W9zCCMGNlVf5MCnzTa3x9AO_OzowM3HTLxPXJxDPoWub-mUifn_QWzau10weOLq3r6wDJ0XZClk-SrSpdTpshZ0MndgZAdezFbMTQXdxQBCjylLOgLYiCeo-TsjonQFlxCoVawlquOwYsk0e_L1KyFx2PY5DptBng0YeCm6herdTO55Nz1T0I5pGIS6udPrqQwRvBsDI6vwzYVCT0SH_2udd6K9rxtdUqKVcKyvo6ZVFB7SNLdjv2jIyjclEivivj_GJ6j7mTrFUDArixcCSDoK-rhtnJLksPoXF2HlJrHPdOLX6YWiCKlMt1yCssPe0pIA3U93EgsrPB-2E43Zhrv94jogN-vJPdRgu7ckk4x04mZcVT33lTpJJKOPqNcguisPJ2Ig8Q2FhaAaaqu7K0ZRNtFv0m8RkRSHIZWi6tza_0lNU4-9j-FSyeH-q9Szg3zO-rvabTqFN04ztY--jZ9nfAoisPbgEtpkwIjPk_Nl1kJuUbwQhS3iX_c-GHbDoSQeBqfqBPV-aoC4EM620tEmtSoUlaVthDoFHKbOvK0T4caOILvegUTj0pAainiF9xn01ISeODdmT35Xa_psw8AIS5T94cYxHk_qxPjUNMXn8k4vy-V9KKw8N4Yq8r7lJhKt9u5lwg3niKHS6ONoWo6-VlZF_y2qcVLmbw05ayvM","user":{"email":"humblevladimirthegreat@gmx.com","lastname":"Society","phone":null,"roles":["Client"],"city":null,"state":null,"source":"web","namedinsured":193206,"address1":null,"tosacceptedat":"2016-02-20 04:05:03","mailchimp":true,"firstname":"The","address2":null,"zip":null,"id":151069,"firstviews":1,"enabled":true,"country":null,"asOf":1456002466742}}'
token = "83cdaa6b-4cfd-4c8c-a2b0-fd82f2496369"
headers = { 'Authorization' : 'Bearer %s' % token,
            #"Content-type": "application/x-www-form-urlencoded",
            "Content-type": "application/json",
            "Accept": "application/json",
			 }
#then connect
#"&scope=user%20openid"+ \
"""
body = "grant_type=authorization_code"+ \
"&redirect_uri=http://127.0.0.1:8000/cropcircles/logged_on"+ \
"&code=eyJhbGciOiJSUzI1NiJ9.eyJrZXkiOiIwZWIyYjFkZWM3ODZlYjExZWQxZGUwZmQ5MzEzNDU5MiIsIm5vbmNlIjoiM282cmhmbWloMXByNTBwdDFsM2xnYjhyIiwiZXhhdCI6MTQ1NjAwMjU4Nn0.aj8awRVSx8c64pJfg8L09eUpjTIVUaJPNU5oKUB2M_dqoN0bUtTKavN1ldc6ACp1T7wCpIpx_gm7wOEeakAIROmmHV9kkyqQGotXJE0iU00deFoc4VJXWTeWCaGbz0f9_F5ov5BauxFxLv8N8paFlQO7EWWeyAEdj8ALKo1ud-rCSKpcppwab039KHQbR59Hfp-8LDgOksQ5F9PlBOAbDVwVuAw4VsFZNBifsrSWkYbjgoGUQbGdmkDJZQNj4Q8Iu1biA4cNFpW1XcWjQWVcvyJzML1keZc7Fy0XuNj-BcIb5IdFjDQde80pzTeiGllx9NVzleZt1bN5A_hxTQNdPc_OFD1iHa2LOEDDMsIftKJ6GGNE8rJ2zFxzdCcvXkpxneiSLXf3n9RbbzpQeiMARJzYuTn_qbdzG0GuiC8IJBO4SOgqpQBs2g1hdj6PyWcgF6RlXiXkNt4LmAXS52THggfRQNFKx77kenk1B9_rfNZ3MHgEMyU2zIbMSsxREXd2_yMq70ZaeuSl0jBVgEECxce35uoMyXm1iMc7fcbX3oArgb9GlR0vAIRTEi54CDIZmPiHqPKOBIxpkAIHI49K7K7VX0VodZZzOSSnxhynDiWTHytXNuLBsaE8hRxWccXTIkY72cL_OvxUztyJyXPieOqzV2x9IG9rNEKVxO3PS04"
c.request('POST', '/api/oauth/token', headers=headers, body=body)
"""
"""
b'{"access_token":"83cdaa6b-4cfd-4c8c-a2b0-fd82f2496369","token_type":"bearer","expires_in":604799,"scope":"openid user","site":{"siteCode":"261e40b5169a72c05273869d"},"id_token":"eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5jbGltYXRlLmNvbS9hcGkvb2F1dGgvdG9rZW4iLCJhdWQiOiJkcGsyODA2NXBjMzFkMCIsImV4cCI6MTQ1NjAwMzE3OCwiaWF0IjoxNDU2MDAyNTc4LCJhdXRoX3RpbWUiOjE0NTYwMDI1NzgsInVzZXJfaWQiOiIxNTEwNjkiLCJzdWIiOiIxNTEwNjkiLCJlbWFpbCI6Imh1bWJsZXZsYWRpbWlydGhlZ3JlYXRAZ214LmNvbSIsImFkZHJlc3MiOnt9LCJyb2xlcyI6WyJjbGllbnQiXSwiZmFtaWx5X25hbWUiOiJTb2NpZXR5IiwiZ2l2ZW5fbmFtZSI6IlRoZSJ9.W9zCCMGNlVf5MCnzTa3x9AO_OzowM3HTLxPXJxDPoWub-mUifn_QWzau10weOLq3r6wDJ0XZClk-SrSpdTpshZ0MndgZAdezFbMTQXdxQBCjylLOgLYiCeo-TsjonQFlxCoVawlquOwYsk0e_L1KyFx2PY5DptBng0YeCm6herdTO55Nz1T0I5pGIS6udPrqQwRvBsDI6vwzYVCT0SH_2udd6K9rxtdUqKVcKyvo6ZVFB7SNLdjv2jIyjclEivivj_GJ6j7mTrFUDArixcCSDoK-rhtnJLksPoXF2HlJrHPdOLX6YWiCKlMt1yCssPe0pIA3U93EgsrPB-2E43Zhrv94jogN-vJPdRgu7ckk4x04mZcVT33lTpJJKOPqNcguisPJ2Ig8Q2FhaAaaqu7K0ZRNtFv0m8RkRSHIZWi6tza_0lNU4-9j-FSyeH-q9Szg3zO-rvabTqFN04ztY--jZ9nfAoisPbgEtpkwIjPk_Nl1kJuUbwQhS3iX_c-GHbDoSQeBqfqBPV-aoC4EM620tEmtSoUlaVthDoFHKbOvK0T4caOILvegUTj0pAainiF9xn01ISeODdmT35Xa_psw8AIS5T94cYxHk_qxPjUNMXn8k4vy-V9KKw8N4Yq8r7lJhKt9u5lwg3niKHS6ONoWo6-VlZF_y2qcVLmbw05ayvM","user":{"email":"humblevladimirthegreat@gmx.com","lastname":"Society","phone":null,"roles":["Client"],"city":null,"state":null,"source":"web","namedinsured":193206,"address1":null,"tosacceptedat":"2016-02-20 04:05:03","mailchimp":true,"firstname":"The","address2":null,"zip":null,"id":151069,"firstviews":1,"enabled":true,"country":null,"asOf":1456002466742}}'
"""


c.request('GET', '/api/users/details?email=humblevladimirthegreat%40gmx%2Ecom', headers=headers, )#body='email=humblevladimirthegreat%40gmx%2Ecom', )
#get the response back
print (c)
res = c.getresponse()
#help(res)
# at this point you could check the status etc
# this gets the page text
data = res.read()  
print (data)
