# picoCTF
## Forensics - Secret_of_the_Polyglot

--------------------
## Solution

Downloading the provided pdf file. 
try ```exiftool garden.jpg``` nothing special.

```xxd garden.jpg > garden_output.hex```
```cat garden_output.hex | grep CTF```
> 00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_

00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3365 4264  m33ts_the_3y3eBd
00230590: 4264 3263 637d 220a                      Bd2cc}".


Flag : `picoCTF{more_than_...}` 
