# sla-check
Shared Local Admin Checker

Uses formatted output from secretsdump and does analysis on the hashes

for i in `cat file`;do python secretsdump.py domain/username:password@$i|sed -e 's/^/'$i'\t/';done > hashdump

Usage:
python sharedlocaladmin.py [hashdump file]

Removes disabled accounts by default

More info can be found here: 
