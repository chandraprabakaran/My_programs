import os

# File path 1
path1 = 'file.txt'

# File path 2
path2 = 'file1.txt'

# File path 3
path3 = 'file2.txt'

# Open the files and get
# the file descriptors
# associated with them
# using os.open() method
fd1 = os.open(path1, os.O_RDWR)
fd2 = os.open(path2, os.O_RDWR)
fd3 = os.open(path3, os.O_RDWR)

# Write a bytestring
str = b"new file has been written"
os.write(fd1, str)
os.write(fd2, str)
os.write(fd3, str)

# Sync. all buffers to disk
# i.e force write everything
# to disk using os.sync() method
os.sync()
print("Force write everything committed successfully")

# Close the file descriptors
os.close(fd1)
os.close(fd2)
os.close(fd3)


from dirsync import sync
source_path = '/Users/chandru/PycharmProjects/veeam/source'
target_path = '/Users/chandru/PycharmProjects/veeam/destination'

sync(source_path, target_path, 'sync') #for syncing one way
# print("it is done")
# sync(target_path, source_path, 'sync') #for syncing the opposite way
print("it is done")
sync(source_path, target_path, 'update')


