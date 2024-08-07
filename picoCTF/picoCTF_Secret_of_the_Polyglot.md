# picoCTF
## Forensics - Secret_of_the_Polyglot

--------------------
## Solution

Downloading the provided pdf file. 
try ```head flag...pdf``` , ```tail flag...pdf```, ```cat flag...pdf```. Nothing special.
* ```❯ file flag2of2-final.pdf```
* ```flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced```

tray ```exiftool flag2of2-final.png``` => Warning : [minor] Trailer data after PNG IEND chunk 
=> There is something after the end of the image (IEND)

``` mv flag2of2-final.pdf flag2of2-final.png```
In the png, you can see **picoCTF{...** and combine this information with the info in the pdf **1n_pn9_&_pdf_7f9bccd1}**



Flag : `picoCTF{...1n_pn9_&_pdf_7f9bccd1}` 
