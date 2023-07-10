import os
from frictionless import describe

def create_datapackage_yaml():
    dataset_files = os.listdir('dataset')
    if 'datapackage.yaml' not in dataset_files:
        package = describe('./data', type='package', basepath='./dataset')
        package['name'] = 'nome-pacote'
        package['owner-org'] = 'organizacao-pacote'
        for resource in package.resources:
            resource['description'] = 'Insira a descrição/explicação detalhada deste recurso.'
            resource['title'] = 'Insira um título humanamente legível para este recurso.'

        package.to_yaml('dataset/datapackage.yaml')

if __name__ == '__main__':
    create_datapackage_yaml()
