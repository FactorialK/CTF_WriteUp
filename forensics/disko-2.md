# DISKO-2

## Description
Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image here.

## Step
```
gunzip disko-2.dd

//fdisk 會顯示 partition table（sector 單位）
fdisk -l disko-1.dd
```
Device Boot Start End Sectors Size Id Type 
disko-2.dd1 2048 53247 51200 25M 83 Linux 
disko-2.dd2 53248 118783 65536 32M b W95 FAT32

```dd if=disko-2.dd bs=512 skip=2048 count=51200 status=none | strings | grep -i "CTF"```
then you get the Flag
