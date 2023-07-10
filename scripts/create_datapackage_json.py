import os
from frictionless import describe

def create_datapackage_json():
    package = describe('datapackage.yaml', type='package', basepath='dataset')
    package.to_json('datapackage.json')

if __name__ == '__main__':
    create_datapackage_json()
