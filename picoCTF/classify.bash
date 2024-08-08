#!/bin/bash

# 遍歷所有 Markdown 文件
for file in *.md; do
  # 提取文件内容的第一行
  header=$(head -n 1 "$file")

  # 提取第二行
  second_line=$(sed -n '2p' "$file")

  # 提取标题中的关键词
  pico_keyword=$(echo "$header" | grep -o 'pico')
  forensics_keyword=$(echo "$second_line" | grep -o 'Web')

  # 只在文件包含所需的关键词时执行
  if [[ ! -z "$pico_keyword" && ! -z "$forensics_keyword" ]]; then
    # 创建目录名
    directory_name="${pico_keyword}_${forensics_keyword}"

    # 创建目录（如果不存在）
    mkdir -p "$directory_name"

    # 移动文件到相应的目录
    mv "$file" "$directory_name/"
  fi
done
