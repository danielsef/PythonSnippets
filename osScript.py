from os.path import expanduser, join, dirname, abspath
home = expanduser("~")  # this is the path to the home folder of the current user
curdir = dirname(abspath(__file__))  # This one returns the path to the file that is running
filepath = join (curdir, 'filename.txt')  # This one joins the path of my current directory to a file name (or any other path) independent of the system


print(home)
print(curdir)
print(filepath)


