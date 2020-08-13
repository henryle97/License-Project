# License Project 

## Install 
- Install packages from requirements.txt file:
```bash 
pip3 install -r requirements.txt
```

- Install MongoDB: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/ \
OR if have error: 
```bash
conda install -c anaconda mongodb
conda install -c anaconda pymongo
cd /
sudo mkdir -p data/db 
sudo chmod 777 data/db
mongo
```

## Usage 

### On sever:
```bash 
cd sever
python query.py 
```
- Example: URL_API: http://localhost:1915

- Generate license from email : http://localhost:1915/generate_license?email=example@email.com&duration_license=30

### On client: file license_client.py
- Edit URL_API at line 7: 
- Active license: activeLicense()  function 
- Check expired license: check_expired() function
