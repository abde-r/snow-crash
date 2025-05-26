As usual we hexdump the executable file, it turns out that it opens a TCP connection to <host>:6969, sends the string "HELLO\n", then reads the specified file and streams its raw bytes over the socket.

We create a custom server that listens on 10.14.59.2:6969, accepts incoming connections, and prints every chunk of data it receives to the console.

Since we have no permission over the token file, we can use the concept of 'Symlink Race'. By creating an empty file /tmp/hack, then entering an endless loop where it force-replaces the symlink /tmp/fake first to point at /tmp/hack, and immediately after to point at ~/token, cycling that switch as fast as possible.

The server then returns a received message with the token that we use to get the flag.
