1首页介绍
当用户进入网页时，首先呈现给用户的界面是首页，首页主要进行了对整个项目的介绍，主要分为四个窗体高度的页面，用户可以通过鼠标滚轮来上下滑动浏览，第一页位首页标题，如下图1-1所示；第二页展示时光画廊功能，如图1-2所示；第三页展示项目的细节，如下图1-3所示；最后一页展示了版本信息，如图1-4所示。

图1-1 首页标题

图1-2 首页功能介绍

图1-3 首页细节介绍

图1-4 首页版本信息

2用户登录使用流程
2.1用户授权
用户点击右上角的“请登录”后，若是用户第一次使用系统，则会自动跳转至百度网盘授权页面，用户可以通过二维码或者输入用户命和密码来授权登录，具体跳转后的界面如图2-1所示。

图2-1 用户授权界面
2.2用户登录
用户若不是第一次登录，或者已经使用百度网盘授权，则点击“请登录”，即如图2-2所示，后前端可以获取到用户百度网盘的用户名和头像，并且可以使用时光画廊。

图2-2 登录
用户登录成功后，点击菜单栏中的“相册”，可以展示3个系统相册，即同学录、趣事录和旅游志，具体呈现如图2-3所示，对于每一个的背景图可以到“照片管理”处管理。具体默认系统相册呈现如图2-3所示。

图2-3 系统相册
2.3创建
用户点击系统相册后，若没有数据，则空白，否则展示用户添加的相册信息。用户可以通过点击头部菜单栏中“创建”来创建对应的相册，会在右侧有弹窗，如图2-4所示。

图2-4 创建同学录
当用户成功创建相册后，会在页面呈现用户新添加的相册，如图2-5所示，其中背景图是默认的，若用户想要更改可以到“照片管理”处上传图片即可。

图2-5 新相册
2.4相册管理
用户点击菜单栏中“相册管理”后，会出现系统内所有用户现有的相册，如图2-6所示，表格第一列是相册类型，第二列是相册描述，第三列为相关操作。

图2-6 相册管理
用户点击编辑后，对应的前两列即为可编辑状态，如图2-7所示，后点击保存，则可将用户更改的信息保存，并更新，如图2-8所示。用户点击“删除”则会删除用户相册的所有信息，包括相册及相册信息。

图2-7 编辑状态

图2-8 保存成功
2.5相册信息创建及使用
由于三种系统相册内关于相册信息创建及管理的方法类似，接下来主要拿同学录新建相册高中来举例，其余可依葫芦画瓢。
当用户点击新创建的相册后，可在左侧看到菜单栏，如图2-9所示。

图2-9 左侧菜单栏
用户点击“添加信息”后，会跳转到添加同学页面，如图2-10所示。当用户完整填写完信息后，点击确认则添加相册信息成功。

图2-10 添加同学
对于创建中特别的是，当用户选中毕业寄语输入框后，会弹出一个弹窗，如图2-11所示。左侧有一个编辑框，用户在此输入毕业寄语，右侧有AI辅助创作，用户在右上框输入需求，点击“AI”按钮后，AI创作的结果在右下框呈现，用户可以选择自己满意的文本复制粘贴到左侧编辑框内，具体呈现如图2-12所示。

图2-11 毕业寄语

图2-12 AI辅助创作
当用户提交相册信息成功后，会提示用户到百度网盘内上传同学头像，则用户需到路径为“我的网盘/我的应用数据/TimeGallery/同学录/高中/李毅”下上传同学头像，成功后到相册内，可以在姓名列表中找到新添加的同学姓名，点击名字后，右侧呈现同学信息，如图2-13所示。

图2-13 李毅信息
后用户可以分别到“照片管理”和“视频管理”上传与李毅同学的图片和视频，上传成功后，相册内李毅信息会更新，如图2-14所示。

图2-14 李毅全部信息
图2-14中，用户在左上方搜索框内输入同学姓名后点击搜索图标可以搜索到该同学，可以定位到该同学的信息。也可进行模糊搜索，例如输入框内输入“王”字，搜索结果出现同学姓名中带“王”字的姓名，如图2-15所示。

图2-15 搜索结果
图2-14中，姓名列表中每一栏，后第一个图标可以编辑同学的信息，跳转到新的页面，如图2-16所示，当用户修改后成功提交，则同学信息就更新。第二个图标为删除，点击后可以直接删除该同学的所有信息，包括基本信息、图片和视频。

图2-16 编辑
图2-14中，毕业寄语一栏右下角有“AI总结”按钮，点击后，可对毕业寄语进行分析，分析的结果会以弹窗的形式出现，如图2-17所示。

图2-17 AI总结
图2-14中，用户点击左侧导航栏中“管理”-“数据可视化”后，会弹出一个弹窗，内容为高中阶段同学地区分布柱状图、同学地区分布省份地图、星座雷达图、兴趣爱好词云图。地图分布柱状图如图2-18所示，地区分布省份地图如图2-19所示，星座雷达图如图2-20所示，词云如图2-21所示。

图2-18 地区柱状图

图2-19 地区分布省份地图

图2-20 星座雷达图

图2-21 词云图
2.6照片管理
用户点击菜单栏中“照片管理”即可进入跳转到新页面，可在选择框内选择想要管理的图片路径，这里的照片管理可以对系统相册和相册的背景图片进行更换，对相册信息内的图片进行管理，由于方法类似，下面只讲述高中相册内李毅同学的图片管理。
在选择框内选择“同学录”-“高中”-“李毅”，如图2-22所示。

图2-22 照片管理
后点击“上传具体时间图片”，右侧出现弹窗，如图2-23所示，用户可在此上传本地图片。

图2-23 上传图片
上传成功后，在选择框内再次选择“同学录”-“高中”-“李毅”，下方出现新上传的图片信息，包括名称和大小，如图2-24所示。

图2-24 图片信息
对于每一张图片可点击垃圾桶图标来删除，确认删除后，会提示删除成功，并且没有该图的信息，如图2-25所示

图2-25 删除图片成功
2.7视频管理
当用户点击“视频管理”即可进入新页面，用户在选择视频路径后，如图2-26所示。可点击“上传视频”来上传对应路径的视频。

图2-26 视频管理页面
上传视频成功后，可选择对应路径来查看视频信息，如图2-27所示，包括视频名称、创建时间、视频大小及相关操作。相关操作包括在线播放视频和删除视频，点击对应按钮即可实现。

图2-27 视频信息
点击“在线播放视频”按钮后，会弹出弹出，可进行视频播放操作，包括开始、暂停、声音大小调节等，如图2-28所示。

图2-28 在线播放视频