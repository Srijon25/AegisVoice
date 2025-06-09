from setuptools import setup, find_packages

setup(
    name='aegisvoice',
    version='1.0.0',
    description='Open software for cancel phrase verification and threat response simulation.',
    author='Srijon Kumar Shill',
    author_email='theunpredictable157@gmail.com',
    url='https://github.com/Srijon25/AegisVoice',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'SpeechRecognition>=3.8.1',
        'PyAudio>=0.2.11',
        'RapidFuzz>=3.0.0',
        'scikit-learn>=1.2.0',
        'streamlit>=1.25.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

