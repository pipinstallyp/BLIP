from distutils.core import setup

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f]

setup(
    name='blip-vit',
    packages=['blip', 'blip.models', 'blip.configs'],
    version='0.0.3',
    description='BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation',
    author='salesforce',
    author_email='junnan.li@salesforce.com',
    url='https://github.com/fernandoTB/BLIP',
    download_url='https://github.com/fernandoTB/BLIP/archive/refs/tags/0.0.3.tar.gz',
    keywords=['0.0.3'],
    install_requires=requirements,
    classifiers=[],
    package_data={'': [
        '*.txt',
        '*.yaml',
        '*.json'
    ]}
)
