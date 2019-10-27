# sla-check
Shared Local Admin Checker

*DO NOT INCLUDE DOMAIN CONTROLLERS*

Credits to https://github.com/SecureAuthCorp/impacket and https://github.com/byt3bl33d3r/CrackMapExec

Uses formatted output from secretsdump and does analysis on the hashes 

`for i in "`cat file`";do python secretsdump.py domain/username:password@$i|sed -e 's/^/'$i'\t/';done > hashdump`

Usage:
python sharedlocaladmin.py [hashdump file]

Removes disabled accounts by default

More info can be found here: 
