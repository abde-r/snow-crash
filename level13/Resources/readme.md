As shown in the message when executing the program 'UID 2013 started us but we we expect 4242'. So we should change the value UID.

We can do that by 'Binary Patching' the executable using GDB to poke new bytes into the running program.

We set a break point at the getuid func using 'break getuid', then hitting a `step` to enter its first instruction. Now we can fake the return value of getuid by overwriting the CPU register EAX --where the function stores its return value-- with the desired UID 4242 by using `set $eax = 4242`, then hitting another `step` to leave getuid() instructions. And now the rest of the program believes that the UID is 4242.
