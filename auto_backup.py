from os import system

# read path file and store paths in array
paths = []
with open("data_backup_paths.txt", "r") as file:
  for line in file:
    paths.append(line.rstrip())

# copy files to central backup location, compress
system("mkdir sys_auto_backup")
for path in paths:
  system("cp -r "+path+" ./sys_auto_backup")
system("zip sys_auto_backup.zip sys_auto_backup")

# check drive upload status
system("gdrive list > gdrive_status.txt")
file = open ("gdrive_status.txt","r")

file_id = None
for line in file:
  if "sys_auto_backup.zip" in line:
    file_id = line.partition(' ')[0]
    break

# upload/update file to drive
if file_id == None :
  system("gdrive upload sys_auto_backup.zip")
else:
  system("gdrive update "+file_id+" sys_auto_backup.zip")

# cleanup
system("rm -rf sys_auto_backup.zip")
system("rm -rf sys_auto_backup")
system("rm -rf gdrive_status.txt")

