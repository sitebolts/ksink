import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ksink",
    version="0.0.1",
    author="SiteBolts",
    author_email="admin@sitebolts.com",
    description="Miscellaneous Python helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sitebolts/ksink",
    project_urls={
        "Bug Tracker": "https://github.com/sitebolts/ksink/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)