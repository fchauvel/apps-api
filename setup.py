from setuptools import setup, find_packages

setup(
    name="apps-api",
    version="0.0.1",
    url="https://github.com/fchauvel/apps-api.git",
    author="Franck Chauvel",
    author_email="franck.chauvel@gmail.com",
    description="Web API for Apps",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn"
    ],
    extras_require={
        "dev": [
            "pytest",
            "httpx"
        ],
    }
)
