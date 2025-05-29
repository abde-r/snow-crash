# Symbolic Link
## walk-through
- Creating a link of the token file using the command `ln -s /home/user/level08/token /tmp/flag`.

- Due to permissions restrictions over the token file in the current directory. The new token is created in '/tmp/' directory.

- The executable file 'level08' reads a file passed to it as argument, as long as the file name is not 'token'.

- Using the new token to get the flag using the command `su flag08`, then the `getflag` command.