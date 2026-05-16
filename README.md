# JAIID
(Jovian Artificial Intelligence Impact Detector)

Introducing JΑΙΙD (Jovian Artificial Intelligence Impact Detector), a groundbreaking AI program at the forefront of Jovian impact flash detection.
JΑΙΙD harnesses the power of advanced artificial intelligence to revolutionize the identification and monitoring of impact flashes, specifically focusing on Jovian phenomena. With state-of-the-art AI models and cutting-edge technology, JΑΙΙD stands as a sentinel in the cosmos, tirelessly scanning Jupiter for any signs of impact events. This innovative detector not only provides real-time alerts but also offers unparalleled insights into the dynamics of celestial collisions. JΑΙΙD signifies a new era in impact detection, where artificial intelligence and celestial observation converge to enhance our understanding of cosmic events and safeguard us against potential threats.

Welcome to the future of impact flash detection—welcome to JΑΙΙD.

Ioannis A. (Yannis) Bouhras <ioannis.bouhras@gmail.com> <mycyberdevops@gmail.com> - Project based on Ultralytics YOLO8 real-time object detection and image segmentation model !!!


FOR REAL TIME IMPACT DETECTION PLEASE VISIT --> https://github.com/ibsoft/JAIID_WEB

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

You can check for impacts on videos, images or gifs

yolo detect predict model="models\\best.pt" project=PROJECT_NAME name=NAME source="YOUR VIDEO OR IMAGE FILE"

If you want to create you own models you must build datasets with (Visual Object Tagging Tool). https://github.com/Microsoft/VoTT/releases

copy your exported vott dataset to /vott folder edit .py files for your needs and run train.py to make your new model.

Download latest community models from here https://github.com/ibsoft/ibsoft-updates/tree/main/jaiid



https://github.com/user-attachments/assets/64f90691-be7d-470c-be1d-c43ef73111d7

<img width="1154" height="1171" alt="00000522" src="https://github.com/user-attachments/assets/96add250-d986-4a6c-8404-4c5585c06df4" />
<img width="1536" height="768" alt="results-1536x768" src="https://github.com/user-attachments/assets/19d30de1-0108-4ac3-9ac0-754c27fe61ce" />
<img width="1052" height="982" alt="jaid" src="https://github.com/user-attachments/assets/54385c0f-b441-41fc-8745-baaa79d92935" />
<img width="1024" height="683" alt="F1_curve-1024x683" src="https://github.com/user-attachments/assets/45fc6512-648f-4f53-8271-fa4364cd42db" />
<img width="1536" height="1380" alt="detects-sample-1536x1380" src="https://github.com/user-attachments/assets/af2f64ca-932d-4333-b2d9-c38acec15a44" />
<img width="880" height="720" alt="91" src="https://github.com/user-attachments/assets/4ee8063e-5c7c-48b7-84eb-098ee3e7630c" />




