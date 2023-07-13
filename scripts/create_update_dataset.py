from dotenv import load_dotenv
import os

load_dotenv()

def create_update_dataset():
    ckan_host = os.getenv('CKAN_HOST')
    ckan_key = os.getenv('CKAN_KEY')

    try:
        os.system(f'dpckan --datastore --datapackage dataset/datapackage.json --ckan-host {ckan_host} --ckan-key {ckan_key} dataset create')
    except:
        os.system(f'dpckan --datastore --datapackage dataset/datapackage.json --ckan-host {ckan_host} --ckan-key {ckan_key} dataset update')

if __name__ == '__main__':
    create_update_dataset()
