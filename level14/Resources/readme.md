# Anti-Debugging bypass & API Hooking
## walk-through
- Disassembling the getflag command binary, which loactes in '/bin/getflag'. The program uses `ptrace` to detect if it's being debugged.

- Bypassing this check, by setting a break point on the ptrace call and change its return value to 0.

- The getflag command uses the current running UID to decrypt the flag. Breaking a point on the <u>getuid()</u> func and changing its return value to **flag14 UID: '3014'**.

