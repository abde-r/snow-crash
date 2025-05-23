We ltrace the binary file, we find out a system() func that executes an echo command, so why not replacing echo with something useful.

We change the path of echo used in the executable file to the path of our own malecious executable, whcih runs the `getflag` command instead of `echo` in system() func.

By executing the binary file 'level03' we get the flag.
