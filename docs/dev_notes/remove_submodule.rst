Remove Submodule
Delete the section referring to the submodule from the .gitmodules file
Stage the changes via git add .gitmodules
Delete the relevant section of the submodule from .git/config.
Run git rm --cached path_to_submodule (no trailing slash)
Run rm -rf .git/modules/path_to_submodule
Commit the changes with `git commit -m "Removed submodule "
Delete the now untracked submodule files rm -rf path_to_submodule

