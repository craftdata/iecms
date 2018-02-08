git submodule add --force https://github.com/craftdata/mongo_fdw.git

# In case the submodule itself has submodules
git submodule update --init --recursive
