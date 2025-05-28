# PCAP
## walk-through
- A **PCAP** (Packet Capture) file is a digital file that stores network traffic captured during packet sniffing.

- Using the 'scp' command to copy the <u>.pcap</u> file from snow-crash VM to our host using `scp -P 4242 level02@ip_of_VM:/home/user/level02/level02.pcap .`.

- Wireshark software enable us to follow the logs monitoring, by using the command: `sudo wireshark ~/level02.pcap`.

- Following the requests sent, the decoding of its data from hexa after removing dots and non-printable characters is a text that says **password: 'ft_wandrNDRelL0L'**, which is the password to get the flag.