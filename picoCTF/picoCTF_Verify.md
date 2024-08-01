# picoCTF
## Forensics - Verify

--------------------
## Solution

Unzip the **challenge.zip**, then you'll have a decrpt shell script, chekcum.txt for sha256 checking and the files containing a number of file with contexts.

1. ssh to the picoCTF server after launching the instance.
2. ```cat checksum.txt``` to show your sha256 value of the targeted file.
3. ```sha256sum files/* | grep desired_sha256_value``` and you get the targeted file.
4. using the provided decrypt script to gain  your flag.

Flag : `picoCTF{trust_}` 
