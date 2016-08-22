from git import Repo

"""
	The very basics of gitpython usage - becasue I keep forgetting!
	More info:
	http://gitpython.readthedocs.io/en/stable/intro.html
"""

# The git URL
git_url='git@github.com:colinhenryfraser/gitpython_example.git'

# the local directory to clone to
local_dir = "my_git_repo" 

# Clone
git_repo = Repo.clone_from(url=git_url,
                           to_path=local_dir)

# Do some work in the repo
with open("{0}/new_file.txt".format(local_dir), "w+") as f:
    f.write("Some new stuff...")

# Add the file
git_repo.index.add(["new_file.txt"])

# Commit
git_repo.index.commit("Added the file new_file.txt")

# Push
git_repo.remotes.origin.push()
