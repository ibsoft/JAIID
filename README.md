# JAIID
(Jovian Artificial Intelligence Impact Detector)

Introducing JΑΙΙD (Jovian Artificial Intelligence Impact Detector), a groundbreaking AI program at the forefront of Jovian impact flash detection.
JΑΙΙD harnesses the power of advanced artificial intelligence to revolutionize the identification and monitoring of impact flashes, specifically focusing on Jovian phenomena. With state-of-the-art AI models and cutting-edge technology, JΑΙΙD stands as a sentinel in the cosmos, tirelessly scanning Jupiter for any signs of impact events. This innovative detector not only provides real-time alerts but also offers unparalleled insights into the dynamics of celestial collisions. JΑΙΙD signifies a new era in impact detection, where artificial intelligence and celestial observation converge to enhance our understanding of cosmic events and safeguard us against potential threats.

Welcome to the future of impact flash detection—welcome to JΑΙΙD.

Ioannis A. (Yannis) Bouhras <ioannis.bouhras@gmail.com> <mycyberdevops@gmail.com>

INSTALLATION & REQUIREMENTS

WINDOWS

Python 3.10.11

LINUX

Python 3.10.12

git clone https://github.com/ibsoft/JAIID.git

cd JAIID

IF WINDOWS

python -m venv venv

IF LINUX 

python3 -m venv venv

IF WINDOWS

.\venv\Scripts\activate

IF LINUX

source venv/bin/activate

IF WINDOWS

pip install -r .\requirements.txt

pip install ultralytics
 
IF LINUX

pip install -r requirements.txt

pip install ultralytics

IF WINDOWS

python.exe -m pip install --upgrade pip

IF LINUX

python3 -m pip install --upgrade pip

IF WINDOWS 

#Test sample .mp4 video for impacts
.\win-detect.bat

IF LINUX 
#Test sample .mp4 video for impacts

./lnx-detect.sh

Look for results in run\\detect\\predict\\impactTest1.mp4

That's it!

You can check for impacts on videos, inages or gifs

yolo detect predict model="models\\best.pt" source="YOUR VIDEO OR IMAGE FILE"

If you want to create you own models you must build datasets with (Visual Object Tagging Tool). https://github.com/Microsoft/VoTT/releases

copy your exported vott dataset to /vott folder edit .py files for your needs and run train.py to make your new model.



