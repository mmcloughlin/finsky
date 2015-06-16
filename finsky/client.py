import requests
import pydash

import protos.response_pb2

BASE_URL = 'https://android.clients.google.com/fdfe/'
CLIENT_ID = 'am-google'

class Client(object):
    def __init__(self, android_id, auth_token, language='en-US', **kwargs):
        self.android_id = android_id
        self.auth_token = auth_token
        self.language = language
        self.request_options_base = kwargs

    def request(self, endpoint, **kwargs):
        request_options_common = {
                'url': BASE_URL + endpoint,
                'headers': {
                    'Accept-Language': self.language,
                    'Authorization': 'GoogleLogin auth=' + self.auth_token,
                    'X-DFE-Device-Id': self.android_id,
                    'X-DFE-Client-Id': CLIENT_ID,
                    'User-Agent': (
                        'Android-Finsky/5.5.12 (api=3,versionCode=80351200,' +
                        'sdk=18,device=x86,hardware=android_x86,' +
                        'product=android_x86,platformVersionRelease=4.3,' +
                        'model=VirtualBox,buildId=JSS15J,isWideScreen=0)'),
                    },
                'verify': False,
                }
        options = pydash.merge({},
                self.request_options_base,
                request_options_common,
                kwargs,
                )
        r = requests.get(**options)
        r.raise_for_status()
        data = r.content
        message = protos.response_pb2.ResponseWrapper.FromString(data)
        return message

    def details(self, doc):
        return self.request('details',
                params={
                    'doc': doc,
                    },
                headers={
                    'X-DFE-No-Prefetch': 'true',
                    })
