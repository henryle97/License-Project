
import pymongo
from pymongo import MongoClient

class LicenseDatabase:
    def __init__(self):
        self.myMongo = MongoClient('mongodb://localhost:27017/')
        self.licenseDB = self.myMongo['LicenseDB']
        license_collection = self.licenseDB["license_col"]
        #print(self.licenseDB.list_database_names())
        for x in license_collection.find({}):
            print(x)

        # license, num_actived, max_active

    def addLicense(self, license):
        license_collection = self.licenseDB["license_col"]
        if license_collection.count_documents({"license" : license}) > 0:
            return False
        data_dict = {"license" : license, "num_actived": 0, "max_active" : 1}
        license_collection.insert_one(data_dict)
        print("Added license ")
        return True

    def findLicense(self, license):

        query = {"license": license}
        license_collection = self.licenseDB["license_col"]
        if license_collection.count_documents(query) == 0:
            print("Not found license: ", license)
            return False
        else:
            print("Found license:", license)
            return True

    def updateNumActivedLicense(self, license):
        query = {"license": license}
        license_collection = self.licenseDB["license_col"]
        license_list_result = license_collection.find(query, limit=1)
        for license_res in license_list_result:
            if license_res['num_actived'] < license_res['max_active']:
                # increase num_actived
                license_collection.update_one(query, {"$inc": {"num_actived": 1}})
                return True
            else:
                print("Reach maximum active")
                return False




if __name__ == "__main__":
    db = LicenseDatabase()
    #db.addLicense(license="ogIiViCKe8Z4lbm0lw5wsMi47dSsCAPdjHvHw3sLZy8fNQyXn2X8H9FFmAFU/u1yiVJae7bylCB4TRudMp95rw==MjAyMDA5MTA=")
    db.findLicense(license="ZdKsMW+kKm1mFUYKJSe/z+G3AFS5B7sS7hBc3UG/vlNj9gMWgJQPPZqUk6EOI/Cml8+fAALvkDEQv2XMg+WiRg==MjAyMDA5MTA=")






