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
        try:
            result = requests.post(url, json=data, headers=HEADERS)
            if result.ok:
                print(result.json())
                result_active = result.json()['result']
                return result_active
            else:
                result.raise_for_status()
                return False
        except:
            return False



    def get_key_and_date_from_license(self, license):
        """

        :param license:
        :return: keygen and data_expired
        """
        keygen, date_expired = license[:-11], license[-11:]
        keygen = keygen + "=="
        date_expired = date_expired + "="
        return keygen, date_expired

    def check_expired(self, license):
        """
        Internet Environment
        :param license:
        :return: False if not expired, True if expired / not internet
        """

        if not self.check_have_internet():
            print("Not internet")
            return True

        keygen, date_expired = self.get_key_and_date_from_license(license)

        # DECODE date_expired
        date_expired_byte = date_expired.encode('ascii')
        date_expired_decode = b64decode(date_expired_byte)          # bytes

        date_expired = datetime.strptime(date_expired_decode.decode('ascii'), '%Y%m%d').date()
        if self.check_have_internet():
            date_now = self.get_time_online()
        else:
            date_now = date.today()

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

    license = "hy4YE6hjCO6gu6/02eOHuWOvnCmaxtZez2TJpss4GFoyTlCsYBfkQUD8gSFmX2pG/FiePUSit26OV0kBFLQwAAMjAyMDA5MTI"
    lis_client = LICENSE_CLIENT()

    print(lis_client.activeLicense(license))
    print(lis_client.check_expired(license))