# Shell Command‐Injection
## walk-through
- The script.lua binds a TCP server on host:5151 and waits for client connections. Then prompts each client for a password, computes its SHA-1 via sha1sum, and compares it to a hard-coded hash 'f05d1d066fb246efe0c6f7d095f909a7a0cf34a0'. Finnaly it replies “Erf nope..” on mismatch or “Gz you dumb” on a correct match, then closes the connection.

- Cracking the passwords using **John the Ripper**, also brute-forcing it. It turns out that it's not about reversing that hash password.

- The program is executing echo shell command. Passing a useful command as password instead like `$(getflag) > /tmp/token;`. Redirecting the output to a file to get the flag.