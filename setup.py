from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="cohelp",
    packages=["cohelp"],
    version="0.1.8",
    python_requires=">=3.6",
    install_requires=[
        l.strip() for l in Path("requirements.txt").read_text("utf-8").splitlines()
    ],
    extras_require=dict(
        dev=["black==19.10b0", "pre-commit==2.5.1"],
        docs=[r for r in Path("docs/requirements.txt").read_text("utf-8").splitlines()],
    ),
    author="Shou-Wen Wang",
    author_email="shouwen_wang@hms.harvard.edu",
    long_description=Path("pypi.rst").read_text("utf-8"),
    long_description_content_type="text/x-rst",
    license="BSD",
)
