#!/bin/bash

#將parse.py 的執行結果輸出到 output.txt中
python3 parse.py > output.txt
#把第二行刪掉
sed -i '' '2d' scripts.js
#在第一行的後面 加入 output.txt 的內容
sed -i '' '1 r output.txt' scripts.js
#開啟瀏覽器
open index.html
