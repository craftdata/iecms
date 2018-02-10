import shutil
import os
from PIL import Image, ImageOps
from flask_appbuilder.filemanager import uuid_namegen, thumbgen_filename
from pydub import AudioSegment
from  .. import config

# filename can be a path, Strips path information and just gives the new name
def upload_img(filename):
	def save_image(image, path, format = 'JPEG'):
		if image.mode not in ('RGB', 'RGBA'):
			image = image.convert('RGBA')
		with open(path, 'wb') as fp:
			image.save(fp, format)
	
	# upname = uuid_namegen(filename)
	# thumb_name = thumbgen_filename(filename)
	
	# resize the file
	orig_img = Image.open(filename)
	new_filename = uuid_namegen(os.path.basename(filename))
	
	thumb_img = ImageOps.fit(orig_img, (30, 30), Image.ANTIALIAS)
	img = ImageOps.fit(orig_img, (400, 400), Image.ANTIALIAS)
	
	save_image(img, config.IMG_UPLOAD_FOLDER + '/' + new_filename)
	save_image(thumb_img, config.IMG_UPLOAD_FOLDER + '/' + thumbgen_filename(new_filename))
	
	return new_filename



# filename can be a path, Strips path information and just gives the new name
def upload_audio(filename):
	new_filename = uuid_namegen(os.path.basename(filename))
	shutil.copy2(filename, config.IMG_UPLOAD_FOLDER + '/' + new_filename)
	return new_filename


def split_audio(filename, mins):
	ret_list = []
	# _, file_extension = os.path.splitext(filename)
	song = AudioSegment.from_file(filename, os.path.splitext(filename)[1][1:])
	song_length = song.duration_seconds
	
	ms_mins = int(mins*60*1000) # calculate the milliseconds
	
	ret_list = [song[i:i+ms_mins] for i in  xrange(0, int(song.duration_seconds*1000), ms_mins)]
	
	return ret_list
	
	# for i in len(ret_list):
	# 	ret_list[i].export("/path/to/output.mp3",
	#                            format="mp3",
	#                            bitrate="192k",
	#                            tags={"album": "The Bends", "artist": "Radiohead", "segment": i}
	# 			)
	#
