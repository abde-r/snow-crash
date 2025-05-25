Since we have no permission over the token file in the current directory. We should work in another emplacement wher we have permissions.

Using the command `ln -s /home/user/level08/token /tmp/flag`, we create a link of the token file. Then we pass that link as parameter to the executable to get the token.

We use the token to get the flag using the command `su flag08`, then the `getflag` command.
