from setuptools import find_namespace_packages, find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='kishan katravath',
    author_email='creategani@gamail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)