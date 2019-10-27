
Credits to https://github.com/SecureAuthCorp/impacket and https://github.com/byt3bl33d3r/CrackMapExec

Be sure to have the latest versions installed:
https://github.com/SecureAuthCorp/impacket/tree/master/examples/secretsdump.py
https://github.com/byt3bl33d3r/CrackMapExec/wiki/Installation

Shared Local Administrator Checker:

*DO NOT INCLUDE DOMAIN CONTROLLERS*

Uses formatted output from secretsdump.py and does analysis on the hashes 

`for i in "`cat file`";do python secretsdump.py domain/username:password@$i|sed -e 's/^/'$i'\t/';done > hashdump`

Usage:
python sharedlocaladmin.py [hashdump file]

Removes disabled accounts by default

More info can be found here: 
https://medium.com/@dvs17/shared-local-account-bad-practices-24a63a3bed0a
