from setuptools import setup, find_packages

setup(
    name='Shiny_SDK',
    version='0.3',
    keywords=('Shiny-Project'),
    description='Python SDK from Shiny.',
    classifiers=[
    ],
    url = 'https://shiny.kotori.moe',
    license='MIT License',
    install_requires=['requests'],

    author='Eridanus Sora',
    author_email='sora@sound.moe',

    packages=find_packages(where="lib"),
    include_package_data = True,
    platforms='any',
)