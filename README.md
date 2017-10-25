## 前言

由於當助教改作業的流程很繁瑣（我hen懶），所以就寫了這個工具幫助我簡化流程。

首先，學生會在一個名為宅學習的平臺上撰寫作業，寫完後存檔會得到一個unique的URL，接著將這個URL貼到臉書課程社團的作業繳交貼文之留言處。
然後助教在改作業時，就要點擊留言的網址，切換瀏覽器分頁，看完作業再關閉切換下一個。 所以改一份作業大概是三次點擊，假設修課人數有六十人… 大約就是180次的點擊🙄


## 安裝Python 相對應套件

#### Option A - Automatically

 ```shell
  $ ./intsall.sh
  ```

 or

  ```shell
  $ bash install.sh
  ```

#### Option B - Manually

```shell
$ sudo easy_install pip

$ pip3 install requests

$ pip3 install beautifulsoup4

$ pip3 install lxml
```

## 使用教學
1. 先到貼文留言處，打開chrome debugger模式

2. 將貼文留言處的程式碼全部複製，貼到data.html中（直接覆寫）。

3. 執行shell script

```shell
$ ./run.sh
```
or

```shell
$ bash run.sh
```
