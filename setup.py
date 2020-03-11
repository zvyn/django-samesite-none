from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="django-samesite-none",
    version="0.0.2",
    description="Django middleware which sets SameSite flag to 'None' for cookies where it is None",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Milan Oberkirch",
    author_email="milan.oberkirch@geops.de",
    url="https://github.com/zvyn/django-samesite-none",
    packages=["django_samesite_none"],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    keywords="django-samesite-none",
    classifiers=[
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
