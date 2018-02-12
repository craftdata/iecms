curl -O http://ftp.nl.debian.org/debian/pool/main/p/protobuf/libprotobuf9_2.6.1-1_amd64.deb
wget http://ftp.de.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u7_amd64.deb
sudo dpkg -i libprotobuf9_2.6.1-1_amd64.deb
sudo apt-get install -f
sudo dpkg -i libssl1.0.0_1.0.1t-1+deb8u7_amd64.deb
sudo apt-get install -f
Install RethinkDB
export DISTRIB_CODENAME="jessie"
echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install rethinkdb


# now do the setup to start at boot
sudo cp /etc/rethinkdb/default.conf.sample /etc/rethinkdb/instances.d/instance1.conf
sudo vim /etc/rethinkdb/instances.d/instance1.conf
sudo /etc/init.d/rethinkdb restart

