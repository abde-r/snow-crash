# CroneJob
## walk-through
- Once login into the fifth level, a popping message saying **'you have a new mail'**.

- The location of the mail file is /var/mail, with `*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05` as content.

- Inside the above path, a cronejob is located, so everything inside that '/opt/openarenaserver/*' directory is executed every 2 mins.

- Creating a simple script with a useful command like `/bin/getflag > /tmp/flag05` in order to be executed to get the flag.
