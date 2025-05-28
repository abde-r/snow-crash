# ROT-13 Cipher
## walk-through
- Using the command `find / -xdev -user flag00 -print` to search for the flag00 in the root dir, we find a file called 'john'.

- Executing the command `cat /usr/sbin/john` to get 'cdiiddwpgswtgt' as its content.

- The docoded value of the text in **ROT-13 Cipher** is the first flag!
