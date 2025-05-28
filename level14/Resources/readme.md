From the disassembly of the getflag command binary, which is loacted in '/bin/getflag'. The program uses `ptrace` to detect if it's being debugged.

To bypass this check, we set a break point on the ptrace call and change its return value to 0.

The getflag command uses the current running UID to decrypt the flag. We set a break point on the getuid func and change its return value to flag14 UID '3014'.

