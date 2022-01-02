<p align="center">
	<strong> Music_label </strong>
</p>


<p align="center">
  <a> <img src="https://img.shields.io/badge/python-3.0%2B-brightgreen"> </a>
  <a> <img src="https://img.shields.io/badge/PyQt5.0-success-brightgreen"> </a>
  <a> <img src="https://img.shields.io/badge/baidu--api-passing-green"> </a>
</p>

# 音频文件转写

Baidu Python Demo [点击下载](https://platform.bj.bcebos.com/sdk/asr/speech_python_demo.zip)

(该demo为百度自己写的，可以将其规整一下。)

# 1. 事前准备工作

百度账号！

## 1.1 账号的注册登录

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633756858569-65611f40-8e0b-4c7f-b486-20b6112afd1e.png)

## 1.2 选择产品服务

通过控制台左侧导航，选择产品服务-人工智能，进入具体AI服务项的控制面板（如文字识别、人脸识别），进行相关业务操作。

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633756794642-4994640b-22aa-4e2b-b47e-4392b3d5563e.png)

# 2. 创建语音识别应用

在控制台中，创建应用，勾选开通”语音技术“-”音频文件转写“能力。获取 AppID、API Key、Secret Key，并通过请求鉴权接口换取 token.

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633756630373-8b2b6890-5a50-4885-9e6e-2a5395088528.png)

## 2.1 [获取密钥](https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3#2-创建应用)

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633756306893-5911fc33-2586-4111-83b6-8fdd66f6032e.png)

```json
{
		"AppID": "******",
  	"API Key": "******",
  	"Secret Key": "******"
}
```



## 2.2 [鉴权认证机制: 获取Access Token](https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjgn3#2-创建应用)

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633756528963-0488fd93-ef6b-456d-b3a9-20cac18b3c87.png)

```json
{
    "refresh_token": "25.35264e084797bc0bf19dd706168455a4.315360000.1949116227.282335-24960897",
    "expires_in": 2592000,
    "session_key": "9mzdDAE89vAYH2jOTi8J2UuSelhHulALOvtk9H3rBU4CgQu0hV+Jn6QfZ/dsGC5rnCEZZTYKN7xa/ryvBO3dTEZUC75ixw==",
    "access_token": "******",
    "scope": "audio_voice_assistant_get brain_enhanced_asr audio_tts_post brain_speech_realtime public brain_all_scope brain_asr_async wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 smartapp_component smartapp_search_plugin avatar_video_test",
    "session_secret": "98507c8a97e59b8af784af8ff8d476f0"
}
```



# 3. 接口调用



## 3.1 [创建音频转写任务](https://ai.baidu.com/ai-doc/SPEECH/ck5diijkt)

接口描述：根据音频url、音频格式、语言id以及采样率等参数创建音频转写任务

请求接口：https://aip.baidubce.com/rpc/2.0/aasr/v1/create（POST）

| KEY          | VALUE                                                        |
| ------------ | ------------------------------------------------------------ |
| access_token | 通过 API Key 和 Secret Key 获取的 access_token，参考[Access Token获取](https://ai.baidu.com/docs#/Auth/top) |



Body中放置请求参数，参数如下：

| **参数名** | **类型** | **是否必需** | **对外状态** | **取值范围**                                                 |
| ---------- | -------- | ------------ | ------------ | ------------------------------------------------------------ |
| speech_url | str      | 是           | 音频url      | 可使用[百度云对象存储](https://cloud.baidu.com/product/bos.html)进行音频存储，生成云端可外网访问的url链接，音频大小不超过500MB |
| format     | str      | 是           | 音频格式     | ["mp3", "wav", "pcm","m4a","amr"]单声道，编码 16bits 位深    |
| pid        | int      | 是           | 语言类型     | [80001（中文语音近场识别模型极速版）, 1737（英文模型）]      |
| rate       | int      | 是           | 采样率       | [16000] 固定值                                               |





Body请求示例：

```json
{
    "speech_url": "https://platform.bj.bcebos.com/sdk%2Fasr%2Fasr_doc%2Fdoc_download_files%2F16k.pcm",
    "format": "pcm",
    "pid": 80001,
    "rate": 16000
}
```



返回参数

| **参数名**  | **类型** | **是否必需** | **对外状态** |
| ----------- | -------- | ------------ | ------------ |
| log_id      | int      | 是           | log id       |
| task_id     | str      | 否           | 任务id       |
| task_status | str      | 否           | 任务状态     |
| error_code  | int      | 否           | 错误码       |
| error_msg   | str      | 否           | 错误信息     |





Body返回示例：

```json
# 创建成功
{
    "log_id": 12345678,
    "task_status": "Created"，
    "task_id":  "234acb234acb234acb234acb"  #注意保存该id，用于后续请求识别结果
}
# 创建失败，缺少参数
{
    "error_code": 336203,
    "error_msg": "missing param: speech_url",
    "log_id": 5414433131138366128
}
```

**注意：查询识别结果时，需要该步骤返回的task_id来进行请求。请注意保存task_id列表。**



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633757724474-b29887d5-5d85-4f84-9e39-baab63c73146.png)



## 3.2 [查询转写任务结果](https://ai.baidu.com/ai-doc/SPEECH/6k5dilahb)



根据task_id的数组批量查询音频转写任务结果 

请求接口：https://aip.baidubce.com/rpc/2.0/aasr/v1/query (POST)

| KEY          | VALUE                                                        |
| ------------ | ------------------------------------------------------------ |
| access_token | 通过 API Key 和 Secret Key 获取的 access_token，参考[Access Token获取](https://ai.baidu.com/docs#/Auth/top) |



Body中放置请求参数，参数如下：

| **参数名** | **类型** | **是否必需** | **描述** | **取值范围**                                                |
| ---------- | -------- | ------------ | -------- | ----------------------------------------------------------- |
| task_ids   | list     | 是           | 任务id   | task_ids为空，返回空任务结果列表；单次查询任务数不超过200个 |



body请求示例：

```json
{
    "task_ids":  ["234acb234acb234acb234acb", "234acb234acb234acb234acd", "234acb234acb234acb234acbe"]
}
```



返回参数：

| **参数名**        | **类型** | **是否必需** |
| ----------------- | -------- | ------------ |
| log_id            | int      | 是           |
| tasks_info        | list     | 否           |
| +task_id          | str      | 是           |
| +task_status      | str      | 是           |
| +task_result      | dict     | 否           |
| ++corpus_no       | str      | 否           |
| ++result          | str      | 否           |
| ++detailed_result | list     | 否           |
| ++err_no          | int      | 否           |
| ++err_msg         | str      | 否           |
| ++sn              | str      | 否           |
| error_code        | int      | 否           |
| error_msg         | str      | 否           |
| error_info        | list     | 否           |



Body返回示例：



```json
{
    "log_id": 12345678,
    "tasks_info": [
	    { # 转写中
	    	"task_status": "Running"
		    "task_id": "234acb234acb234acb234acb",
	    },
	    { # 转写失败
	    	"task_status": "Failure"
		    "task_id": "234acb234acb234acb234acd",
		    "task_result": {
			    "err_no":  3301
			    "err_msg": "speech quality error",
			    "sn": "xxx"
		    }
	    },
	    { # 转写成功
		    "task_status": "Success",
		    "task_result": {
		    	"result": [
			        "观众朋友大家好，欢迎收看本期视频哦。毕竟..."
			    ],
                "audio_duration": 6800,
			    "detailed_result": [
			        {
			        	"res": [
			                "观众朋友大家好，欢迎收看本期视频哦。"
			            ],
			            "end_time": 6700,
			            "begin_time": 4240,
			            "words_info": [],
			            "sn": "257826606251573543780",
			            "corpus_no": "6758319075297447880"
			        }
			        ...
			    ],
			    "corpus_no": "6758319075297447880" 
			},
			"task_id": "234acb234acb234acb234ace"
	    }
	]
}
```

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633758053328-8ffa22e5-d3aa-422d-a174-67962cc368fe.png)



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633758197665-9b6351b0-a86a-436c-9caf-4dfe28ef8e1d.png)



# 4. 出现的问题

## 4.1 speech_url必须是音频url

用户必须要将音频文件上传至云端，这样接口才能正确



错误示例：



将音频文件放在window桌面下。

请求接口：正确返回tasks_id。

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633759477390-626dc0f7-ae4f-44b8-ab2d-811546d2e856.png)



BUT！

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633759609490-8de26c83-d0a2-4352-bc23-6f8897e0758f.png)



解决方案：



可使用[百度云对象存储](https://cloud.baidu.com/product/bos.html)进行音频存储，生成云端可外网访问的url链接，音频大小不超过500MB。





创建个Bucket，上传文件，会生成一个外网访问的url链接。

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1633762959464-8a137643-abe9-4835-acde-7e394aa16b63.png)

## 

## 4.2 音频文件不对应



可以使用[音频文件转码](https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf)


# 自然语言情感分析

# 1. baidu-aip



```plain
Help on package aip:

NAME
    aip - aip public

PACKAGE CONTENTS
    base
    bodyanalysis
    easydl
    face
    imagecensor
    imageclassify
    imageprocess
    imagesearch
    kg
    nlp
    ocr
    speech
```



## 1.1 nlp

**nlp全称Natural Language Processing，自然语言处理。**



所以需要查看nlp里面有什么。



## 1.2 aip-nlp

```plain
NAME
    aip.nlp - 自然语言处理

CLASSES
    aip.base.AipBase(builtins.object)
        AipNlp
    
    class AipNlp(aip.base.AipBase)
     |  AipNlp(appId, apiKey, secretKey)
     |  
     |  自然语言处理
     |  
     |  Method resolution order:
     |      AipNlp
     |      aip.base.AipBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  commentTag(self, text, options=None)
     |      评论观点抽取
     |  
     |  depParser(self, text, options=None)
     |      依存句法分析
     |  
     |  dnnlm(self, text, options=None)
     |      DNN语言模型
     |  
     |  ecnet(self, text, options=None)
     |      文本纠错
     |  
     |  emotion(self, text, options=None)
     |      对话情绪识别接口
     |  
     |  keyword(self, title, content, options=None)
     |      文章标签
     |  
     |  lexer(self, text, options=None)
     |      词法分析
     |  
     |  lexerCustom(self, text, options=None)
     |      词法分析（定制版）
     |  
     |  newsSummary(self, content, max_summary_len, options=None)
     |      新闻摘要接口
     |  
     |  sentimentClassify(self, text, options=None)
     |      情感倾向分析
     |  
     |  simnet(self, text_1, text_2, options=None)
     |      短文本相似度
     |  
     |  topic(self, title, content, options=None)
     |      文章分类
     |  
     |  wordEmbedding(self, word, options=None)
     |      词向量表示
     |  
     |  wordSimEmbedding(self, word_1, word_2, options=None)
     |      词义相似度
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from aip.base.AipBase:
     |  
     |  __init__(self, appId, apiKey, secretKey)
     |      AipBase(appId, apiKey, secretKey)
     |  
     |  getVersion(self)
     |      version
     |  
     |  post(self, url, data, headers=None)
     |      self.post('', {})
     |  
     |  report(self, feedback)
     |      数据反馈
     |  
     |  setConnectionTimeoutInMillis(self, ms)
     |      setConnectionTimeoutInMillis
     |  
     |  setProxies(self, proxies)
     |      proxies
     |  
     |  setSocketTimeoutInMillis(self, ms)
     |      setSocketTimeoutInMillis
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from aip.base.AipBase:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```

查看上图，情感分析为**sentimentClassify(self, text, options=None)**



# 2. 如何使用aip.nlp

## 2.1 创建应用

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634388236993-47ff0a2e-870d-4649-84f3-f87e3c8ee09e.png)



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634388265319-e41503c2-8e3c-48a4-b064-c5a00ca6faa7.png)



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634388289243-3961fdc9-114a-498e-bea2-f8543a8e3e54.png)

```json
{
	"client_appId" = "25004504",
	"client_apiKey" = "******",
	"client_secretKey" = "******"
}
```



## 2.2 具体代码实现

```python
import aip

client_appId = '25004504'
client_apiKey = '******'
client_secretKey = '******'

lyrics = '今天天气很好'
print(lyrics)

# 调用自然语言处理api
my_nlp = aip.nlp.AipNlp(client_appId, client_apiKey, client_secretKey)

print(my_nlp.sentimentClassify(lyrics))

# sentimentClassify(self, text, options=None)
```

# 1. PyQt5下载

使用豆瓣提供的镜像服务。

## 1.1 命令行安装

### 1.1.1 pip install PyQt5 -i https://pypi.douban.com/simple

### 1.1.2 pip install PyQt5-tools -i https://pypi.douban.com/simple



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372698746-8a02a126-6093-4c16-b35f-0f1fdf06f885.png)



安装完成后在Python安装目录下的Lib\site-packages目录中可以看到PyQt5、pyqt5-tools目录。



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372576631-c815f25e-b0d2-440e-815c-1d2d9d2361bf.png)



## 1.2 Pycharm安装

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372757967-a30bd956-c34f-41d1-8914-ce997d0a6b98.png)![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372765054-1618d373-9199-43bd-aa9a-81c9e1cac5df.png)

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372773214-3067b4c0-519d-40d5-9cc7-ec525f9a03cf.png)



## 1.3 使用PyQt

在pycharm中新建一个python文件，然后在其他写入代码：

```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication

app = QApplication(sys.argv)
widget = QWidget()
widget.resize(800, 600)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()
sys.exit(app.exec())
```

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372643107-1d0692ab-1bb9-41eb-992b-152babefe3c4.png)

##  

# 2. PyQt5在Pycharm中配置

File->Settings->Tools->External Tools.

| 工具        | *.exe          | 说明                                         |
| ----------- | -------------- | -------------------------------------------- |
| Qt Designer | ./designer.exe | 打开Qt Designer界面，对软件的界面进行设计    |
| PyUIC       | ./python.exe   | 将Qt Designer设计的UI文件转换为,py文件       |
| PyRCC       | ./pyrcc5.exe   | 将资源文件如图片等转成python代码能识别的文件 |



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372896649-433609ba-c2c6-4897-bf23-0068b5b0cd71.png)

## 2.1 添加Qt Designer



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372956245-89f341e3-87ce-4c25-84ef-03d03acdad72.png)

## 2.2 添加PyUIC

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372974916-ecc96bea-b625-41c4-8b7c-048483a45dfd.png)



## 2.3 添加PyRCC

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634372983842-912c05fb-3f3e-49b7-8fc2-f21777bbefc5.png)



## 2.4 成品展示



![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634373292997-58804216-d7b1-4eca-9363-61be196bef7b.png)



**因为每个人安装配置不同，对于找不到.exe文件可以自行百度。**







# 3. PyQt设计界面

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634643454049-76068cbd-4825-4603-b10d-6ab06c1b1438.png)

本来想要美化界面，突然想要透明化是不是挺好，然后就是上图孤零零的Upload。



# 4. 集成.py文件

## 4.1 各文件

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634634956256-144f1a2c-58c7-406e-8370-47e9980df52f.png)

## 4.2 大致流程

![img](https://cdn.nlark.com/yuque/0/2021/png/22670381/1634634843941-e83c6e97-6958-4d59-b5b3-2fe2b25e4636.png)



# 5. 缺点

## 5.1 API调用速度慢

由于每次调用api时，会返回一个状态，例如Running，但是之后并不会返回result，所以需要调用多次直到状态为Success，这里设置sleep(7)

```python
if dict_json['tasks_info'][0]['task_status'] == 'Success' :
	my_txt = dict_json['tasks_info'][0]['task_result']['result'][0]

	print(my_txt)

	with open('../speech_txt/lyrics.txt', "w", encoding='utf-8') as f :
		f.write(my_txt)
		emotion_analysis.emo()

elif dict_json['tasks_info'][0]['task_status'] == 'Running':
	time.sleep(7)
	query() # 递归调用
```

## 5.2 健壮性不强

由于开发时间有限，程序每次只能运行一个文件，但是可以运行多个文件，后续有时间会补上。



## 5.3 结果不准确

这个准确度控制不了，因为是调用的百度的nlp。



# 6. 完结撒花

结对作业bye。
