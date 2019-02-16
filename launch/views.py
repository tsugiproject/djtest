from django.http import HttpResponse
from django.shortcuts import render

import jwt, json

# Create your views here.

# pip install PyJWT
# pip install cryptography

def launch(request) :
    encoded = request.POST.get('JWT');
    print(encoded)
    public_key = b"""-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBWMR90paAAdbR8d/qlxdZG
NQ22/ZqiPq5re9jlLPdW7MnnaMzo0fXgRN8kM2DpXgLN6qLtpVj3uuqBGItmCofi
0N76Nn1MvcFWl5VOUpZzpgjR2kjjiV8LOYQahQim7o2a826TSqJqNSS/eIz6OLOM
Rhpyxo82VXcXTv2izWCpqYv3dCv25ApfUrSzcapPkbGNXvG1H2N0hbtOw7U14vKn
i4S5+NiSIunApBx1GoTPhehEUlGEFGiB3kpkReOkwvNQbt6TmKIJhBofY377P278
zzLnWN/Isbm5UJjZ1izeyt6uWvhRu1vUFo3Np8CHI6rZI6VPUIyPNxljdkUomn/T
AgMBAAE=
-----END PUBLIC KEY-----"""
    decoded = jwt.decode(encoded, public_key, algorithms=['RS256'])
    js = json.dumps(decoded, indent=4)

    retval = "<pre>\n"+js+"\n</pre>\n";
    return HttpResponse(retval)
