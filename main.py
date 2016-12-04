import tappedout
import sys
import pprint
import detect_shapes
import cv2

# Camera 0 is the integrated web cam on my netbook
camera_port = 1

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 100

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
camera.set(3,1900)
camera.set(4,1000)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = camera.read()
	return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(ramp_frames):
	temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()

del(camera)

image = camera_capture
url = sys.argv[1]

deck = tappedout.generateDeck(url)
status = detect_shapes.boardParser(image, deck)
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(deck)
