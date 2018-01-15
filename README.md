外包測試案

# 主要目的

在對話系統中，我們時常會需要收集使用者的基本聯絡資料來做後續聯絡。現在大多數人的處理方式請使用者到額外的表單輸入網頁填入資料，這會讓對話系統的使用流程中斷。我們希望在對話系統中，就能收集完使用者基本聯絡資料；而不用讓使用者額外到另外一個網頁輸入資料。

你的工作是使用現成技術，製作出一個基本的對話控制系統以及介面；並可以通過對話系統收即到使用者資料。

情境是：

```
User: 你好
Robot：Hello
Robot：你的名字是？
User: 我的名字是林雪碧
Robot：你好林雪碧
Robot：你的 email 是？
User：lin@xotours.xyz
Robot：林雪碧，你的 email 是 lin@xotours.xyz
```

# 技術需求及限制

這不是一個研發專案，而是一個商業應用。所有的技術已經成熟，需要把現成技術串起來而不是研發。

* 使用 [wit.ai](https://wit.ai/) 作為對話控制中心
	* 請使用 Python Script 建立資料，而不是手動在 GUI 建立資料。
* 後端使用 Python Flask framework，作為串接 wit.ai 以及前端的中間層。
	* 如果有對話 finite state machine 也可以加在這一層。
* 前端使用 React
	* 有 mobile 以及 desktop 版本。
* 請使用提供的 Docker 檔案作為開發框架，裡面包含了
	* server：python flask folder
	* client：react folder
	* docker-compose：專案設定架構
	* 使用方法：安裝 docker、docker-compose，在根目錄

	```
	$docker-compose up --build -d
	```

	就可以同時建立 server 以及 client，server 網址是 `http://localhost:8080`，client 網址是 `http://localhost:3000`。


# 驗收標準

## 使用情境

### Case 1

```
User: 你好
Robot：Hello
Robot：你的名字是？
User: 我的名字是林雪碧
Robot：你好林雪碧
Robot：你的 email 是？
User：lin@xotours.xyz
Robot：林雪碧，你的 email 是 lin@xotours.xyz
```

### Case 2

```
User: 你好
Robot：Hello
Robot：你的名字是？
User: 陳可樂
Robot：你好陳可樂
Robot：你的 email 是？
User：是 cola@xotours.xyz
Robot：陳可樂，你的 email 是 cola@xotours.xyz
```

### Case 3

```
User: 你好
Robot：Hello
Robot：你的名字是？
User: 王沙士
Robot：你好王沙士
Robot：你的 email 是？
User：我才不想告訴你呢
Robot：你的 email 是？
User：heysong@gmail.com
Robot：王沙士，你的 email 是 heysong@gmail.com
```

## 技術檢核

* 我們會使用 `docker-compose up --build` 來建立專案並測試
* 使用 script 建立 wit.ai 訓練資料。我們會使用空的 wit.ai 來測試。
* 使用 wit.ai 擷取出使用名字以及 email，而**不是**使用 Python 擷取出名字及 email。
* 問句 `你的名字是？` 可能的回答支援兩種：
	* `{使用者名字}`
	* 我的名字是`{使用者名字}`
* 問句 `你的 email 是？` 可能的回答支援兩種：
	* `{email}`
	* 是 `{cola@xotours.xyz}`
* 如果回答的不是 email，則需要一直詢問到問出 email 為止。
* 前端介面使用 RWD (CSS Media Query)。在視窗大小為 800 時，請符合圖 `desktop.jpg`，在視窗大小為 550 時，請符合圖 `mobile.jpg`。
	* 手機外殼及平版外殼只是參考用，不用實做
	* `desktop.jpg` 右方的文章內容，請從 yahoo 新聞複製圖片和文章內容就好。資料寫死，也不用實做按鈕及連結功能。
	* 使用者頭像和機器人頭像可以更換成類似的圖就好
	* 按鈕`+`、按鈕`耳機`、按鈕`麥克風`都不用實做按下去的功能，但必須是個按鈕。
* 在對話輸入框，按下 enter 以後送出資料。

# 開發框架

在檔案夾中 `wells-snack`，裡面有兩個資料夾及一個檔案。

## 建立專案方法

1. 請先[安裝 docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04) 以及 [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)。
2. 切換到 `docker-compose.yml` 檔案的所在目錄

```
$ docker-compose up --build
```

3. 等看到 `You can now view client in the browser.` 訊息以後，可以打開瀏覽器連線至 `http://localhost:3000` 查看範例網頁。

## 檔案架構

* docker-compose.yml

	> 環境參數設定檔，開發時請把 `WIT_SERVER_ACCESS_TOKEN` 改成自己申請的 token

* server
	* fungogo/chatbot/model

		> model。已經含有和 wit.ai 溝通的範例

	* fungogo/chatbot/route

		> controller。已經含有和 client side 溝通範例

	* scripts/init.py

		> 初始化 wit.ai 資料的 script。已經含有建立 greeting、bye intent 的程式碼。

		> 使用指令：


			$ docker exec -it wellssnack_server_1 /bin/sh
			$ python scripts/init.py

* client
	* src/App.js

		> React Root Component。已經有和 server side 溝通的基本程式碼。


# 資源

* wit.ai
	* [wit.ai API tutorial] (https://github.com/wit-ai/wit-api-only-tutorial)
	* [API document] (https://wit.ai/docs/http/20160330)
	* [Python client] (https://github.com/wit-ai/pywit)
* wit.ai 對話流程控制：
	* [Bolg: sunsettiing stories] (https://wit.ai/blog/2017/07/27/sunsetting-stories)
	* [Stories Migration Tutorial] (https://github.com/wit-ai/wit-stories-migration-tutorial)
* Server side: Python Flask
	* [Offical website](http://flask.pocoo.org/)
	* [Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/introduction/)
	* [Document](http://flask.pocoo.org/docs/0.12/)
* Client side: React
	* 使用 [create-react-app](create-react-app) 建立專案
	* [React Tutorial](https://reactjs.org/tutorial/tutorial.html)
* Docker as container
	* [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)
	* [Install docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)
* 頁面 icon 可以直接使用 fontawsome
	* [FontAwsome](http://fontawesome.io/)

# 法律相關

* 驗收過程中，請交付程式原始碼供技術檢核
* 過程中產生的程式原始碼歸公司資產，不得轉讓、販賣、或洩漏予第三者 程式外包

# 聯絡人

有任何疑問請聯絡 `Up` up@xotours-ai.xyz
