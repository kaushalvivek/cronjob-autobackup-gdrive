![version:1.0](https://img.shields.io/badge/version-1.0-blue) ![languge:python3](https://img.shields.io/badge/Python-3.6-brightgreen)

# Automatic File Backup to Google Drive

This sript is a cronjob for automated periodic file backups to Google Drive. It is built upon the ```gdrive``` org's initiative.

## Pre-Requisites
- ```python3``` installed on system
- A Google Drive account
- ```gdrive``` command-line utility, [click here to install](https://github.com/gdrive-org/gdrive)
- **```gdrive``` initialised** : check initialisation instructions below

### ```gdrive``` Initialisation
- After installation (Step 3 of pre-requisites), run ```gdrive list```
- Paste the prompted address in your browser
- Sign into your Google Drive account
- Copy the displayed authentication code
- Paste the authentication code in your terminal

## Deployment
- Satisfy the pre-requisites, ensure that ```gdrive``` is initialised.
- Add the paths to folders/files you'd like to back-up in ```data_backup_paths.txt```in separate lines
- Type ```crontab -e```in your terminal
- Add the following line to the crontab file, fill in the <PATH_TO_SCRIPT>  
  ```20 4 * * * python3 <PATH_TO_SCRIPT>/auto_backup.py```
  
This crontab setting will backup all your designated files once a day, at 4:20 am. The backups are smart updates and only incremental/decremental changes are reflected. You can change the update frequency as per your need, just don't mess your network bandwidth up. And don't get yourself flagged by Google.

Raise issues if you have any comments/suggestions/problems.
