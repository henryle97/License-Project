import json
from base64 import  b64decode

from datetime import date, timedelta, datetime
from urllib.request import urlopen, URLError
import requests

URL_API = 'http://localhost:1915'

PAGE_GET_TIME = 'http://just-the-time.appspot.com/'
# LICENSE =  KEYGEN + DATA_EXPIRED (KEYGEN == rsa)
HEADERS = {
    'Content-Type': 'application/json'
}

class LICENSE_CLIENT:

    def __init__(self):

        pass
    def activeLicense(self, license):
        """
        Kich hoat license
        :param license:
        :return:
        """
        # res = self.db.findLicenseAndUpdate(license)
        # return res
        data = {"license": license}
        url = URL_API + '/check_license'
        result = requests.post(url, json=data, headers=HEADERS)
        if result.ok:
            print(result.json())
            result_active = result.json()['result']
            return result_active
        else:
            result.raise_for_status()
            return False


    def get_infor_from_license(self, license):
        """

        :param license:
        :return: keygen and data_expired
        """
        keygen, data_expired = license[:-12], license[-12:]
        return keygen, data_expired

    def check_expired(self, license):
        keygen, data_expired = self.get_infor_from_license(license)

        # DECODE date_expired
        data_expired_byte = data_expired.encode('ascii')
        data_expired_decode = b64decode(data_expired_byte)          # bytes

        date_expired = datetime.strptime(data_expired_decode.decode('ascii'), '%Y%m%d').date()
        if self.check_have_internet():
            date_now = self.get_time_online()
        else:
            date_now = date.today()
        # date_now = date.today()
        if date_now > date_expired:
            print("Expired license")
            return True

        else:
            print("Not expired license")
            return False
    def get_time_online(self):
        """

        :return: date object
        """
        page_time = urlopen(PAGE_GET_TIME)
        time_now = page_time.read().strip()
        date_now = datetime.strptime(time_now.decode('utf-8'), '%Y-%m-%d %H:%M:%S').date()
        return date_now

    def check_have_internet(self):
        try:
            urlopen('http://216.58.192.142', timeout=1)
            return True
        except URLError as err:
            return False



if __name__ == "__main__":

    license = "d32X6dakM7G6p6bo8f+zoTvpSWBuW45jKNXuVISOLWUPAcPa2W7rzX8TK7q4JJyQCponqe4TrEqq2Rb0HFMmwg==MjAyMDA5MTA="
    lis_client = LICENSE_CLIENT()

    print(lis_client.activeLicense(license))
    print(lis_client.check_expired(license))