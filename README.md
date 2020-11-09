# Automation

## Python scripts I use to automate certain tasks

Use at your own risk.

### How to use these scripts?

To run most of these scripts, you will need to add the scripts to crontab.
Type `crontab -e` into your terminal like this:

```ubuntu@ubuntu:~$ crontab -e``` 

the `-e` flag represents us openning the crontab in edit mode. If you do not have a default text editor your system may ask you to pick one. Nano is simple to use and recommended for beginners.

At the end of the file, write the following:

```@reboot python /path/to/python/scripts/```
