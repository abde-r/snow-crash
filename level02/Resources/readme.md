we get the .pcap file from the VM using `scp -P 4242 level02@ip_of_VM:/home/user/level02/level02.pcap .`

we run wireshark to follow the logs monitoring using the command: `sudo wireshark ~/level02.pcap`

we decode the data sent from hexa and we find: password: 'ft_wandrNDRelL0L'.

we remove the duplicate lowercase characters to get the correct code, and we use it to get the flag.
