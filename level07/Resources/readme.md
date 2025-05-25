We hexdump the executable file view irs raw bytes in hex. Using the command `hexdump -C level07`, then we find that the program executes an echo command to an env variable called LOGNAME.

We try to set a useful command in the env variable, so we get the flag echoed, such as 'export LOGNAME=\`getflag\`'.
