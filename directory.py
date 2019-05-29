import os
import sys
import subprocess
from sys import platform

# os.makedirs(pname)
# os.makedirs(f"{pname}/{pname}")

print("Django Directory Structure Creator Version 1.1 Beta")
pname = input("Please enter a Project Name: ")
aname = input("Please enter an App Name: ")

# aname = "test_app6"
# pname = "test_project6"
if platform == "linux" or platform == "linux2":
    print("linux")
elif platform == "darwin":
    print("OSx")
    subprocess.run(["django-admin", "startproject", "%s" % pname], stdout=subprocess.PIPE)
    os.chdir(f'./{pname}')
    os.makedirs("apps")
    # os.makedirs(f"apps/{aname}")
    os.chdir("apps")
    subprocess.run(["django-admin", "startapp", "%s" % aname], stdout=subprocess.PIPE)
    os.makedirs(f"{aname}/templates")
    os.makedirs(f"{aname}/templates/{aname}")
    os.makedirs(f"{aname}/static")
    os.makedirs(f"{aname}/static/css")
    os.makedirs(f"{aname}/static/images")
    os.makedirs(f"{aname}/static/js")
    os.chdir('..')
    os.chdir(f'./{pname}')
    with open("settings.py", 'r') as file:
        settings = file.readlines()
    new_settings = []
    for line in settings:
        if "INSTALLED_APPS" in line:
            print("found")
            new_settings.append(line.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    '%s'," % f"    apps.{aname}"))
        else:
            new_settings.append(line)
    with open("settings.py", 'w') as file:
        file.write("".join(new_settings))

elif platform == "win32":
    print("Windows")
    subprocess.run(["django-admin", "startproject", "%s" % pname], stdout=subprocess.PIPE)
    os.chdir(f'.\\{pname}')
    os.makedirs("apps")
    os.makedirs(f"apps/{aname}")
    subprocess.run(f"django-admin startapp {aname} .\\apps/{aname}")
    os.makedirs(f"apps/{aname}/templates")
    os.makedirs(f"apps/{aname}/templates/{aname}")
    os.makedirs(f"apps/{aname}/static")
    os.makedirs(f"apps/{aname}/static/css")
    os.makedirs(f"apps/{aname}/static/images")
    os.makedirs(f"apps/{aname}/static/js")
    os.chdir(f'.\\{pname}')
    with open("settings.py", 'r') as file:
        settings = file.readlines()
    new_settings = []
    for line in settings:
        if "INSTALLED_APPS" in line:
            print("found")
            new_settings.append(line.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    '%s'," % f"apps.{aname}"))
        else:
            new_settings.append(line)
    with open("settings.py", 'w') as file:
        file.write("".join(new_settings))
