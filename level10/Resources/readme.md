# Symlink Race
## walk-through
- Hexdumping the executable file. The program opens a TCP connection to host:6969. Sends a string and reads and streams the raw bytes of a specified file over the socket.

- Creating a custom server listening on VM_IP:6969, that accepts incoming connections, and prints every chunk of data it receives to the console.

- The concept of 'Symlink Race' helps since no permission are granted over the token file.

- By creating an empty file /tmp/hack, then running an endless loop where it force-replaces the symlink /tmp/fake first to point at /tmp/hack, and immediately after to point at ~/token, cycling that switch as fast as possible.

- The server then returns a received message with the token used to get the flag.