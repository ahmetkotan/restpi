import re
import subprocess

ip_patt = re.compile("inet\saddr\:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
process = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
output = process.stdout.read()

ip_list = ip_patt.findall(output)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ip_list