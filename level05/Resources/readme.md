Once login into the fifth level, we get a message saying 'you have a new mail'.

Then we find a file in /var/mail with `*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05` as content.

In /usr/sbin/openarenasever we find script that executes everything in the /opt/openarenaserver/* directory, which means this script is executed every 2 mins in the cronejob above.

We create a simple script with a useful command in order to be executed and get the flag.
