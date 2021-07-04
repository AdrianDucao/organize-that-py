# organize-that-py
it is an automation to move downloaded files to their respected directories, removing the clutter from Downloads directory making things nicer and organize.

## dependencies
* Python ^3.x

## Installation on Fedora 30+
clone the repo to your desired directory and will create daemon to make it persistent process.
```bash
$ git clone https://github.com/AdrianDucao/organize-that-py.git

$ cd organize-that-py

$ sudo chmod 775 organize.py

$ sudo cp organize.service /lib/systemd/system/organize.service

$ sudo systemctl daemon-reload

$ sudo systemctl start organize.service

$ sudo systemctl enable organize.service
```



if you find this useful please star this or fork it if you can make it better

