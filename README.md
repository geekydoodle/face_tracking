<div align="center"><h1>Face Tracking</h1></div>

<div align="center"><p>A guide showing how to do Face Tracking using OpenCV on a Raspberry pi.</p></div>

<div align="center"><img src="imgs/thumbnail.png"></div>

<h2>Versions that I am using.</h2>

<p>In my case I am using Python 3.7.3, If you want to download Python 3.7.3 go to https://www.python.org/downloads/ and download it and for the OpenCV I am using OpenCV 4.5.5.62 because I am using Python 3.7.3 if you are using some other version of python you might need to play around with the OpenCV version.</p>

<h2>0. Update and Upgrade your pi.</h2>

```
sudo apt-get update && sudo apt-get upgrade
```

 <h2>1. Simple method of installing Python 3.7 on Raspberry pi.</h2>

```
sudo apt-get install python3.7
```
<h2>2. Install Git</h2>

```
sudo apt-get install git
```

<h2>3. Clone the repository.</h2>

```
git clone https://github.com/geekydoodle/face_tracking.git
```

<h2>4. Change directory into the folder.</h2>

```
cd face_tracking
```

<h2>5. Make a venv</h2>

<p>Install venv package</p>
  
```
sudo apt-get install python3.7-venv
```

<p>6. Make a venv</p>

```
python3.7 -m venv name_of_venv
```

<h2>7. Activate the venv</h2>

```
source name_of_env/bin/activate
```

<p>After activating the venv you should see a pop up on your terminal like:<br>(test) pi@raspberrypi:~ $</p>

<h2>8. Install OpenCV</h2>

<p>There are two versions of OpenCV the 1st one opencv-python and the 2nd one opencv-contrib-python, opencv-python contains the main modules package but the opencv-contrib-python contains both main modules and extra modules.</p>

<p>Install opencv-contrib-python.</p>

```
pip3.7 install opencv-contrib-python==4.5.5.62
```

<p>Install opencv-python.</p>

```
pip3.7 install opencv-python==4.5.5.62
```

<h2>9. Run script</h2>

<p>For webcam</p>

```
python3.7 face_tracking_on_webcam.py
```

<p>For img</p>

```
python3.7 face_tracking_on_img.py
```

<p>Happy Computer Visioning!!!!!</p>
