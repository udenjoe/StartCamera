from picamera import PiCamera
from time import sleep
from fractions import Fraction

image_effects = ['none', 'negative', 'solarize', 'sketch', 'denoise', 'emboss',
	'oilpaint', 'hatch', 'gpen', 'pastel', 'watercolor', 'film', 'blur', 'saturation', 'colorswap',
	 'washedout', 'posterise', 'colorpoint', 'colorbalance', 'cartoon',
	'deinterlace1', 'deinterlace2']

with PiCamera(sensor_mode=6) as camera:
	camera.start_preview()
	camera.video_stabilization = True
	count = 0
	while(True):
		camera.image_effect = image_effects[count]
		camera.annotate_text_size = 120
		camera.annotate_text = image_effects[count]
		sleep(10)
		count += 1
		if(count is len(image_effects)):
			count = 0
