from os import system

# read path file and store paths in array
paths = []
with open("data_backup_paths.txt", "r") as file:
  for line in file:
    paths.append(line.rstrip())
print (paths)

# copy files to central backup location, compress
system("mkdir sys_auto_backup")
system("cd sys_auto_backup")
for path in paths:
  system("cp -r "+path+" ./")
system("zip sys_auto_backup.zip sys_auto_backup")

# check drive upload status

# new approach : 
#   store gdrive list output in a file
#   read line by line from file
#   if "file_name" in line
#     use id token (first token by space delim)
text = system("gdrive list")
