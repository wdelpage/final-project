from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="EmotionDetection",
    version="1.0.0",
    author="Wasana Delpage",
    author_email="delpage@gmail.com",
    description="A Python package for detecting emotions in text using Watson NLP services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wdelpage/EmotionDetection",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Check",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords="emotion detection, nlp, watson, sentiment analysis",
    project_urls={
        "Bug Reports": "https://github.com/wdelpage/EmotionDetection/issues",
        "Source": "https://github.com/wdelpage/EmotionDetection",
    },
)