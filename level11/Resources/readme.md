Seems like the program.lua binds a TCP server on 127.0.0.1:5151 and waits for client connections. Then prompts each client for a password, computes its SHA-1 via sha1sum, and compares it to a hard-coded hash 'f05d1d066fb246efe0c6f7d095f909a7a0cf34a0'. And finnaly replies “Erf nope..” on mismatch or “Gz you dumb” on a correct match, then closes the connection.

We try to crack the passwords using John the Ripper, also brute-forcing it. It turns out that it's not about reversing that hash password.

The program is executing a bash command, so we try to pass a useful command as password instead of the password, and redirect the output to a file to get the flag.
