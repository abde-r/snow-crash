# John the Ripper
## walk-through
- User informations in unix systems are usually stored in a file called '/etc/passwd'.

- The display output of the content of this file is: 'flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash'

- By decoding the text `42hDRfypTqqnw` using <u>**John the Ripper**</u> --a password cracking tool. Executing `john secret.txt --show`, with 'secret.txt' a file storing most used passwords.

- The result of the crack is 'abcdefg' which is the password to get the flag.
