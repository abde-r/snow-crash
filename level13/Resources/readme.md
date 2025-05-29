# Binary Patching
## walk-through
- Executing the 'level13' binary, a message says 'UID 2013 started us but we we expect 4242'.

- Changing the value of user Id <u>UID</u> by **'Binary Patching'** the executable using GDB to poke new bytes into the running program.

- Setting a break point at the <u>getuid()</u> func using 'break getuid', then hitting a <u>step</u> command to enter its first instruction.

- Faking the return value of getuid by overwriting the CPU register <u>EAX</u> --where the function stores its return value-- with the desired **UID: 4242** using `set $eax = 4242`, then hitting another `step` command to leave getuid() instructions.

- The rest of the program now believes that the UID is 4242, and shows the flag.