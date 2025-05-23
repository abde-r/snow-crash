We cat the content of the binary file .pl. Seems like it's a CGI that that takes whatever we pass in the query parameter and sends it back to the browser.

Again we expolit the content of x variable with something useful such as `curl 'http://localhost:4747/level04.pl?x=%24(getflag)'` to get the flag.
