We use the CGI program, passing a script containing a useful command to get executed in order to receive the flag.

By using the command `echo 'getflag > /tmp/flag' > /tmp/SCRIPT` as a parameter for the CGI script. The program capitalizes the x variable so we as well should uppercase it to match the it and avoid not recognizing it.

Then it gets executed after passing it as parameter like: `curl localhost:4646/?x='`/*/SCRIPT`'`. Since '/tmp/SCRIPT' is translated to '/TMP/SCRIPT' by the CGI, we can use the bash wildcard such as '/*/script' to find any occurences of the matching pattern. 

