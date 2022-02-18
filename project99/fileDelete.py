import time
import os
import shutil

def princh():

    path = "project99/deleteIt"

    days = 0

    seconds = time.time()- (days*24*60*60)

    if os.path.exists(path):
        if seconds >= get_file_or_folder_age(path):

            # removing the folder
            if not shutil.rmtree(path):

                # success message
                print(f"{path} is removed successfully")

            else:

                # failure message
                print(f"Unable to delete the "+path)

#-----------------------------------------------------------

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)

#-----------------------------------------------------------

def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:
		# failure message
		print("Unable to delete the "+path)

#-----------------------------------------------------------

def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

#-------------------------------------

princh()