

# Makura
A user-friendly CNC (Command & Control) panel based on CLI that recieves and executes commands.
![](https://github.com/p0megranate/makura/blob/master/root.JPG)

# Features
- Makura can retrieve commands through twitter, modify the file & replace your twitter within the first 10 lines afterwards run `wget` & makura will attempt to look for the word `wget` on your twitter, you can also modify the prefix to your choice.

- The Makura Bot has a feature called `Retrieve` which spawns a shell based on the newest `CVE-2019-16759` vulnerability which affects vBulletin 5.x through 5.5.4. This feature also has a tacky `history-shell` which basically allows you to access the last-shell session. To reproduce that, open a shell & click CTRL-C now that will prompt makura's default terminal after that click CTRL-C again, and you will reappear in the last session. It also notifies you if it is vulnerable beforehand, I would also suggest to listen to `Retrieve` as it only allows `http://` anything else `Makura` & `Retrieve` will kick you out of the vBulletin session.

- Host implementation is used in Makura to ease any internal process changes, if you run `host`, Makura will ask you to send a command which will then echo back whatever change you made internally.

- Makura allows you to generate a `PHP Shell` using a command of your choice, if you run `shell_exec`, Makura will ask you to send a command which will then be used to make a `PHP Shell` where you can upload it to the target of your choice. Just a little automation to help you out.

- To exit the program just type `exit` and it'll prompt you to your original root directory.

- Note the original exploit for the vBulletin CVE has been modified with a little bit of tweaking to suit this program.


Also a cool feature is, you can use phrases like:

`Hey Makura, root me a vbulletin instance`

It will reply back with input of the URL, it also works with everything else but the PHP shell I retained the special keyword just because it seems to run smoothly that way.
# Requirements
- Python 3x (3.5)
- Requests
- urllib.request
- platform
- time
- re


# Thanks

Thank you to the anonymous researcher who provided the vBulletin exploit which is located at: https://seclists.org/fulldisclosure/2019/Sep/31

# Disclaimer

I am not responsible for any actions you perform using this tool, this is solely for the purpose of security research.

# Additional Help
If you would like to help, you are free to tag along with helping me modifying the bot to be better, I also am planning to develop a chat system within it because it seems fun & it reminds me of the earlier days.

# Bugs
There is a small bug which skips a line and replaces it with the default error message, if you know a fix for it then you can merge it with the repository and I will confirm it.

# Quick Notice

Do not change the file name, because on CTRL-C or any exits it attempts to fetch for the original file name so unless you got a quick trick for that since I had to be creative here, I wouldn't suggest modifying the file name.


