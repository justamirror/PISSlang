import os
def dfie(path):
  if os.path.exists(path):
    os.system(f"rm -rf {path}")
from datetime import date
from li import licenses
def pkg(**kwargs):
  filenames = kwargs.get('filenames', [kwargs.get("filename", kwargs.get("mainfile"))])
  pkgname = kwargs.get("pkgname", kwargs.get("filename", kwargs.get("mainfile")).replace(".py", ""))
  version = kwargs["version"]
  project = kwargs["project"]
  repo = kwargs.get("repo", "pypi")
  descutoff = kwargs.get("descutoff", 50)
  email = kwargs.get("email", "eat@mybutt.com")
  outputfile = kwargs.get("outputfile", None)
  if not kwargs.get("name"):
    if kwargs.get("email"):
      name = kwargs["email"].split("@")
      name = name[0]
    else:
      kwargs["name"]
  else:
    name = kwargs["name"]
  today = date.today()
  licence = licenses[kwargs["licence"].lower()].replace("[fullname]", name).replace("[year]", str(today.year))
  longdes = kwargs.get("longdes", kwargs["des"])
  shortdes = kwargs.get("shortdes", (longdes[:descutoff] + '..') if len(longdes) > descutoff else longdes)
  dfie(pkgname)
  os.makedirs(f"{pkgname}/src/{pkgname}")
  os.mkdir(f"{pkgname}/tests/")

  with open(f"{pkgname}/src/{pkgname}/__init__.py", "w") as i:
    if len(filenames) == 1:
      with open(filenames[0], "r") as f:
        i.write(f.read())
  if not len(filenames) == 1:
   for file in filenames:
    with open(file, "r") as f:
      with open(f"{pkgname}/src/{pkgname}/{file}", "w") as nf:
        nf.write(f.read())
  with open(f"{pkgname}/README.md", "w") as rdme:
    rdme.write(longdes)
  with open(f"{pkgname}/LICENCE", "w") as lifile:
    lifile.write(licence)
  e = "\n"
  with open(f"{pkgname}/pyproject.toml", "w") as pptoml:
    pptoml.write('''[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"''')
  with open(f"{pkgname}/setup.cfg", "w") as s:
    s.write(f"""[metadata]
name = {pkgname}
version = {version}
author = {name}
author_email = {email}
description = {shortdes.replace(e, " ")}
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/{project}
project_urls =
    Bug Tracker = https://github.com/{project}/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src
""")
  if not outputfile:
    ending = ""
  else:
    ending = f"1>> {outputfile} 2>> {outputfile}"
    with open(outputfile, "w") as optfile:
      optfile.write("")
  os.system(f"python3 -m pip install --upgrade build {ending}")
  os.system(f"python3 -m build {pkgname}/ {ending}")
  os.system(f"python3 -m pip install --upgrade twine {ending}")
  os.system(f"python3 -m twine upload --repository {repo} {pkgname}/dist/* --username __token__ --password {os.environ.get('token')} {ending}")
  print(kwargs)
version=input("version: ")
input("Edit 'deREADME.md' in the replit editor and press enter to conferm.")
des=open("README.md", "r").read()
pkg(filename='interpreter.py', pkgname="pisslang", version=version, name="Mirror", des=des, project="justamirror/PISSlang", licence="mit")