## 首页介绍
当用户进入网页时，首先呈现给用户的界面是首页，首页主要进行了对整个项目的介绍，主要分为四个窗体高度的页面，用户可以通过鼠标滚轮来上下滑动浏览，第一页位首页标题，第二页展示时光画廊功能，第三页展示项目的细节，如下图最后一页展示了版本信息。
<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/2239edef-49dd-4612-bd58-30d9a240f554">

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/43778882-12c0-4102-a8de-3dd2f27cf558">

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/6b2495a1-ef0f-4602-9329-204a899d0bd0">


<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/b242af8e-4ba5-428f-a536-d68c9541ac86">


## 用户登录使用流程
### 用户登录
用户若不是第一次登录，或者已经使用百度网盘授权，则点击“请登录”，后前端可以获取到用户百度网盘的用户名和头像，并且可以使用时光画廊。用户登录成功后，点击菜单栏中的“相册”，可以展示3个系统相册，即同学录、趣事录和旅游志，对于每一个的背景图可以到“照片管理”处管理。
<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/fd1e6764-8826-4a31-b1f8-478e3347511f">

### 创建
用户点击系统相册后，若没有数据，则空白，否则展示用户添加的相册信息。用户可以通过点击头部菜单栏中“创建”来创建对应的相册，会在右侧有弹窗。

<img width="178" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/4ccc5412-1b84-4656-a47d-104b82a3a443">

当用户成功创建相册后，会在页面呈现用户新添加的相册，其中背景图是默认的，若用户想要更改可以到“照片管理”处上传图片即可。

<img width="154" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/8bf18c87-c9d3-40c5-b6cf-fe1b5eda89c7">

### 相册管理
用户点击菜单栏中“相册管理”后，会出现系统内所有用户现有的相册，表格第一列是相册类型，第二列是相册描述，第三列为相关操作。用户点击编辑后，对应的前两列即为可编辑状态，后点击保存，则可将用户更改的信息保存，并更新。用户点击“删除”则会删除用户相册的所有信息，包括相册及相册信息。

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/8a5cf870-1973-4f48-b1fe-8e4cc116e1f4">

### 相册信息创建及使用
由于三种系统相册内关于相册信息创建及管理的方法类似，接下来主要拿同学录新建相册高中来举例，其余可依葫芦画瓢。
当用户点击新创建的相册后，可在左侧看到菜单栏。

<img width="117" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/68674a22-e977-4412-ae66-94c652db4d8d">

用户点击“添加信息”后，会跳转到添加同学页面。当用户完整填写完信息后，点击确认则添加相册信息成功。
<img width="416" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/a3cc7f32-7101-479e-8733-a88946ea8959">
对于创建中特别的是，当用户选中毕业寄语输入框后，会弹出一个弹窗。左侧有一个编辑框，用户在此输入毕业寄语，右侧有AI辅助创作，用户在右上框输入需求，点击“AI”按钮后，AI创作的结果在右下框呈现，用户可以选择自己满意的文本复制粘贴到左侧编辑框内。

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/d668b143-166b-492a-84cc-54f912f67758">

当用户提交相册信息成功后，会提示用户到百度网盘内上传同学头像，则用户需到路径为“我的网盘/我的应用数据/TimeGallery/同学录/高中/李毅”下上传同学头像，成功后到相册内，可以在姓名列表中找到新添加的同学姓名，点击名字后，右侧呈现同学信息。
<img width="416" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/59bede13-986f-44a3-b315-815ca39c818a">

毕业寄语一栏右下角有“AI总结”按钮，点击后，可对毕业寄语进行分析，分析的结果会以弹窗的形式出现示。

<img width="209" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/4c819f2d-5fa7-49d1-b5d9-ee68cdf1714e">

用户点击左侧导航栏中“管理”-“数据可视化”后，会弹出一个弹窗，内容为高中阶段同学地区分布柱状图、同学地区分布省份地图、星座雷达图、兴趣爱好词云图。

<img width="239" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/b0faa7f4-66ca-4793-985f-99039240b3a2">

### 照片管理
用户点击菜单栏中“照片管理”即可进入跳转到新页面，可在选择框内选择想要管理的图片路径，这里的照片管理可以对系统相册和相册的背景图片进行更换，对相册信息内的图片进行管理，由于方法类似，下面只讲述高中相册内李毅同学的图片管理。后点击“上传具体时间图片”，右侧出现弹窗，用户可在此上传本地图片。上传成功后，在选择框内再次选择“同学录”-“高中”-“李毅”，下方出现新上传的图片信息，包括名称和大小。对于每一张图片可点击垃圾桶图标来删除，确认删除后，会提示删除成功，并且没有该图的信息。

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/a53964a9-def6-4b59-b5e4-9d2f512faa9d">

### 视频管理
当用户点击“视频管理”即可进入新页面，用户在选择视频路径后。可点击“上传视频”来上传对应路径的视频。上传视频成功后，可选择对应路径来查看视频信息，包括视频名称、创建时间、视频大小及相关操作。相关操作包括在线播放视频和删除视频，点击对应按钮即可实现。

<img width="414" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/44cebff4-1f42-44e0-ae44-48dc870c1311">

点击“在线播放视频”按钮后，会弹出弹出，可进行视频播放操作，包括开始、暂停、声音大小调节等。

<img width="415" alt="image" src="https://github.com/togetherhkl/TimeCanvas/assets/92192378/9c4360db-4773-4ffc-959e-f963aab053fe">
