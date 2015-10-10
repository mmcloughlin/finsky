import requests
import pydash

import finsky.protos.response_pb2

# disable InsecureRequestWarning when using verify=False
# https://github.com/kennethreitz/requests/issues/2214
requests.packages.urllib3.disable_warnings()

BASE_URL = 'https://android.clients.google.com/fdfe/'
CLIENT_ID = 'am-google'
DEFAULT_DEVICE = {
        'model': 'Nexus 5',
        'build': 'KTU84P',
        'android_version': '4.4.4',
        }


class Client(object):
    def __init__(self, android_id, auth_token, language='en-US', device={},
                 **kwargs):
        self.android_id = android_id
        self.auth_token = auth_token
        self.language = language
        self.device = pydash.merge({}, DEFAULT_DEVICE, device)
        self.request_options_base = kwargs

    def user_agent(self):
        ua = 'Android-Finsky/5.6.8 '
        ua += '(api=3,versionCode=80360800,sdk=19,device=hammerhead,'
        ua += 'hardware=hammerhead,product=hammerhead,'
        ua += 'platformVersionRelease=%s,' % (self.device['android_version'])
        ua += 'model=%s,buildId=%s,isWideScreen=0)' % (
                self.device['model'], self.device['build'])
        return ua

    def request(self, endpoint, **kwargs):
        request_options_common = {
                'url': BASE_URL + endpoint,
                'headers': {
                    'Accept-Language': self.language,
                    'Authorization': 'GoogleLogin auth=' + self.auth_token,
                    'X-DFE-Device-Id': self.android_id,
                    'X-DFE-Client-Id': CLIENT_ID,
                    'User-Agent': self.user_agent(),
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
        message = finsky.protos.response_pb2.ResponseWrapper.FromString(data)
        return message

    def details(self, doc):
        message = self.request('details',
                               params={
                                   'doc': doc,
                                   },
                               headers={
                                   'X-DFE-No-Prefetch': 'true',
                                   })
        return message.payload.detailsResponse

    def delivery(self, doc, version_code, certificate_hash, offer_type):
        message = self.request('delivery',
                               params={
                                   'doc': doc,
                                   'vc': version_code,
                                   'ot': offer_type,
                                   'ch': certificate_hash,
                                   },
                               )
        return message.payload.deliveryResponse

    def delivery_from_details(self, details_response):
        """
        Make a delivery request based on the results of an app details
        request.
        """
        doc = details_response.docV2
        ch = doc.details.appDetails.certificateSet[0].certificateHash[0]
        kwargs = {
                'doc': doc.docid,
                'version_code': doc.details.appDetails.versionCode,
                'certificate_hash': ch,
                'offer_type': doc.offer[0].offerType,
                }
        return self.delivery(**kwargs)

    def download_user_agent(self):
        ua = 'AndroidDownloadManager/%s ' % (self.device['android_version'])
        ua += '(Linux; U; Android %s; %s Build/%s)' % (
                self.device['android_version'], self.device['model'],
                self.device['build'])
        return ua

    def download(self, url, cookies):
        """
        Download file at the given URL with an authentication cookie specified
        in the cookies dictionary. The authentication cookie is typically
        called "MarketDA", but the name is specified in the delivery response,
        so could in principle change.
        """
        download_request_options = {
                'url': url,
                'headers': {
                    'User-Agent': self.download_user_agent(),
                    'Accept-Encoding':  'identity',
                    },
                'cookies': cookies,
                'verify': False,
                }
        options = pydash.merge({},
                               self.request_options_base,
                               download_request_options,
                               )
        r = requests.get(**options)
        r.raise_for_status()
        return r.content

    def download_from_delivery(self, delivery_response, gzipped=False):
        """
        Perform a download given a response from the delivery request.
        """
        data = delivery_response.appDeliveryData
        url = data.gzippedDownloadUrl if gzipped else data.downloadUrl
        cookie = data.downloadAuthCookie[0]
        kwargs = {
                'url': url,
                'cookies': {
                        cookie.name: cookie.value,
                    }
                }
        return self.download(**kwargs)
