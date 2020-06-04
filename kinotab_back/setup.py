from pathlib import Path
from setuptools import setup, find_packages

def read_requirements(name: str):
    p = Path(__file__).parent.joinpath(name)
    reqs = [line for line in p.read_text().splitlines() if line]
    return reqs

setup(name='kinotab-back',
      version='0.1.0',
      packages=find_packages(),
      install_requires=read_requirements("requirements.txt"),
      extras_require={
            "dev": read_requirements("requirements-dev.txt"),
      },
      scripts=['manage.py'])
