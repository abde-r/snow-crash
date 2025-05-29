# John the Ripper
## walk-through
- User informations in unix systems are usually stored in a file called '/etc/passwd'.

- The display output of the content of this file is: 'flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash'

- By decoding the text `42hDRfypTqqnw` using <u>**John the Ripper**</u> --a password cracking tool. Executing `john token.txt --show`, with 'token.txt' the file that stores the encrypted token in the form of 'user:42hDRfypTqqnw'.

- The result of the crack is 'abcdefg' which is the password to get the flag.