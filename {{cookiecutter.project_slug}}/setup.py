from pathlib import Path

from setuptools import find_packages, setup

name = "{{ cookiecutter.project_slug }}"
current_dir = Path(__file__).parent.resolve()

with open(current_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=f"{name}",
    version="0.1.0",
    packages=find_packages(),
    url=f"https://github.com/thg-consulting/{name}",
    author="thg",
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
)

