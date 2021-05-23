import os
def dfie(path):
  if os.path.exists(path):
    os.system(f"rm -rf {path}")
from datetime import date
from li import licenses
def pkg(**kwargs):
  filenames = kwargs.get('filenames', [kwargs["filename"]])
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
  dfie(pkgname)
  os.makedirs(f"{pkgname}/src/{pkgname}")
  os.mkdir(f"{pkgname}/tests/")

  with open(f"{pkgname}/src/{pkgname}/__init__.py", "w") as i:
    longdes = kwargs.get("longdes", kwargs["des"])
    shortdes = kwargs.get("shortdes", (longdes[:descutoff] + '..') if len(longdes) > descutoff else longdes)
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
description = {shortdes}
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
  os.system(f"python3 -m twine upload --repository {repo} {pkgname}/dist/* {ending}")
  print(kwargs)
pkg(mainfile="hello.py", filename='lack.py', pkgname="lack", version='0.0.0.0', name="Just A Mirror", des="Lack is a pseudo programming language. Why did I make it? Because fuck you thats why. Anyyways, docs and examples are at [BLANK: WILL BE UPDATED]", project="cooldude/pp", licence="mit")