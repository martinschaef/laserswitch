# Laser Switch
Turn Hue lights on and off with a laser

[![Demo Video](http://img.youtube.com/vi/Q8bN9leSIg4/0.jpg)](http://www.youtube.com/watch?v=Q8bN9leSIg4)

### Hardware requirements: 
- Philipps Hue
- A computer with a camera, python and opencv
- A red [laser pointer](https://www.amazon.com/gp/product/B00SYIDQT2/ref=oh_aui_detailpage_o02_s01?ie=UTF8&psc=1)

### Software requirements:

- Python 2.7
- OpenCV; I used [these instructions](http://www.mobileway.net/2015/02/14/install-opencv-for-python-on-mac-os-x/)
- [BeautifulHue](https://github.com/allanbunch/beautifulhue)

### HowTo

Create a python file `secret_keys.py` with the information about your bridge. E.g.,

```python
hue_ip="192.168.1.2"
hue_key="9o33LVASDo9nvARn"
```

If you don't have this information, follow [these instructions](https://github.com/allanbunch/beautifulhue) to pair your computer with your bridge.

Start the program with `python find_laser.py`. This will open two windows; one containing the HSV camera view and one containng the masked camera view which should be completely black and only have a white spot where the laster is detected.
Leave the program with ESC. This closes the window and writes a file `frame.png` to disk. 

Edit the `frame.png` by turning it into a grey-scale image and mark the areas with Hue lights in different colors like in [this image](https://github.com/martinschaef/laserswitch/blob/master/triggers.png), and safe the image as `triggers.png`. Now update the `trigger_actions` in [line 21 of find_laser.py](https://github.com/martinschaef/laserswitch/blob/master/find_laser.py#L21) accordingly, and you should be good to go.

### Knwon Issues

I didn't spend much time perfecting the image filtering that detects the laser. So, if you have a lot of direct sunlight that reflects in metal objects (e.g., a chrome lamp) this might be detected as laser as well and turn your lights on and off. In that case, use the control image (the one that should be mostly black), and adjust the filtering.




