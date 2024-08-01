# picoCTF
## Forensics - Scan Surprise

--------------------
## Solution

Unzip the **challenge.zip**, then you'll get a *flag.png*

1. ssh to the picoCTF server after launching the instance.
2. using ```zbarimg``` to show the QR-code png then get the flag
3. ``` QR-Code:picoCTF{p33k_@.....}```


Flag : `picoCTF{p33k_@....}` 


## Related work
I installed a png-parser tool to analyze the png.
```
Filename: flag.png | Size: 352

[00000000-00000032] (0)
IHDR:
Data size : 13

[00000033-00000050] (1)
PLTE:
Data size : 6

[00000051-00000064] (2)
tRNS:
Data size : 2

[00000065-00000085] (3)
pHYs:
Data size : 9

[00000086-00000339] (4)
IDAT:
Data size : 242

[00000340-00000351] (5)
IEND:
Data size : 0
```
IHDR: 文件的第一個塊，必須存在。定義了圖像的基本屬性。
PLTE: 可選塊，僅在使用調色板的圖片中存在。
tRNS: 可選塊，僅在需要透明度信息時存在。
pHYs: 可選塊，提供圖像的物理尺寸信息。
IDAT: 包含實際的圖像數據，可能有多個 IDAT 塊。
IEND: 文件的最後一個塊，表示 PNG 文件的結束。

```png-parser -d flag.png``` then I got a long string inside the IDAT chunk.





