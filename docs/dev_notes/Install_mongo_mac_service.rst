et up launchctl to auto start `mongod`

    `$ ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents`

    `/usr/local/opt/mongodb/` is a symlink to `/usr/local/Cellar/mongodb/x.y.z` (e.g., `2.4.9`)

    You can use launchctl to start and stop `mongod`

        `$ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist`
        `$ launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist`
                
            You can also more conveniently use `brew` to start, stop, and verify service status

                `$ brew services list | grep mongodb
                $ brew services start mongodb
                $ brew services stop mongodb`

#### Notes

The default plist provided by homebrew stores the mongod configuration at `/usr/local/etc/mongod.conf`. This configuration specifies the `dbpath` to be `/usr/local/var/mongodb` instead of the default `/data/db`.

For more about `launchctl` see:

https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/launchctl.1.html#//apple_ref/doc/man/1/launchctl

http://launchd.info/
Incidentally if the luanchctl does't wok use:

 `launchctl load -wF ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist`
