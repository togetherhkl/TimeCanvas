# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-15 11:25:49
# LastEditTime: 2024-04-15 11:25:53
# LastEditors: HKini 1778267485@qq.com
# Description: 视频管理的相关路由
# FilePath: \TimeCanvas\backend\routers\video.py

# '''

from fastapi import APIRouter,Depends,HTTPException,File,UploadFile,Form
from fastapi.responses import StreamingResponse,FileResponse
import os
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from models import orm_models
from schemas import orm_schema
from crud import album_crud, user_crud,video_crud
import datetime

router = APIRouter()
#格式化文件大小
def format_size(size: int, precision: int = 2) -> str:
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(suffixes) - 1:
        size /= 1024
        index += 1
    return f'{size:.{precision}f} {suffixes[index]}'
#添加视频
@router.post("/video",tags=["video"],description=
             "添加视频，支持多文件上传，视频文件将保存在media/video文件夹中")
async def video_create(
    files: list[UploadFile],
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
    video_specifc_event:int=Form(...),
    video_album_type: int=Form(...),
    video_album:int=Form(...),
):
    for file in files:
        video={}
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        filename = f"{timestamp}_{baidu_uk}_{file.filename}"
        #检查数据库中是否有重名的文件，如果有重新命名
        while video_crud.get_video_by_nickname(db, filename):
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            filename = f"{timestamp}_{baidu_uk}_{file.filename}"
        #保存文件
        with open(f"media/video/{filename}", "wb") as f:
            f.write(file.file.read())
        #计算文件字节大小
        file.file.seek(0)
        file_size = 0
        while True:
            chunk = file.file.read(10000)
            if not chunk:
                break
            file_size += len(chunk)
        size = format_size(file_size)
        video['video_name']=filename
        video['video_owner']=baidu_uk
        # video['video_data']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        video['video_nickname']= file.filename
        video['video_specifc_event']=video_specifc_event
        video['video_album_type']=video_album_type
        video['video_album']=video_album
        video['video_size']=size
        video_crud.video_create(db, video)
    #返回HTTP 200状态码
    return {"msg":"success"}

#获取特定用户,特定相册类型，特定相册，特定事件的视频
@router.get("/video",tags=["video"],description=
    "获取特定用户,特定相册类型，特定相册，特定事件的视频")
async def get_video(
    video_album_type: int,
    video_album:int,
    video_specifc_event:int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return video_crud.get_video(db, baidu_uk, video_album_type, video_album, video_specifc_event)

#视频播放的媒体数据流
@router.get("/videostream/{video_name}",tags=["video"],description=
    "视频播放的媒体数据流")
def video_stream(
    video_name,
):
    def iterfile():  # (1)
        with open("media/video/"+video_name, mode="rb") as file_like:  # (2)
            yield from file_like  # (3)
    return StreamingResponse(iterfile(), media_type="video/mp4")

#下载视频
@router.get("/videodownload/{video_name}",tags=["video"],description=
    "下载视频")
def video_download(
    video_name,
    video_nickname,
):
    def iterfile():
        with open("media/video/"+video_name, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename="+video_nickname})

#删除视频
@router.delete("/video",tags=["video"],description=
    "删除视频")
async def video_delete(
    video_id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    video = video_crud.get_video_by_id(db, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="视频不存在")
    if str(video.video_owner) != str(baidu_uk):
        raise HTTPException(status_code=403, detail="无权删除")
    if(os.path.exists("media/video/"+video.video_name)):
        os.remove("media/video/"+video.video_name)
    return video_crud.video_delete(db, baidu_uk, video_id)
    
from models.text import TextModel
from models.image import ImageModel, ImageCaptionModel
from models.audio import AudioModel
from models.subtitle import SubtitleModel
from models.video import VideoModel
import util
import os
from typing import List, Tuple, Optional
import time
import random


def get_output_path() -> str:
    def get_video_number() -> int:
        file_path = "database/video_count.txt"
        data = util.read_file(file_path)
        count = 1
        if data:
            count = int(data)

        util.write_file(str(count + 1), file_path)

        return count

    n = get_video_number()
    output_path = f"outputs/{n}"

    os.makedirs(output_path, exist_ok=True)

    return output_path


DEFAULT_TOPICS = [
    "a historical inspiring fact that changed computer science",
    "an ancient story about a clever king or warrior",
    "a strange or funny fact from world history",
    "a scientific discovery that changed human life",
    "a breakthrough in medical science that saved millions",
    "a dramatic moment from World War 1 or World War 2",
    "a surprising origin of a modern invention",
    "a fun random fact that will make people smile",
]


def get_content(topic: str | None, storage: str) -> Tuple[str, List[str]]:
    text_model = TextModel()
    if not topic:
        topic = random.choice(DEFAULT_TOPICS)
    # topic = DEFAULT_TOPICS[9]
    content = text_model.generate_content(topic)
    content_storage = f"{storage}/content/"
    os.makedirs(content_storage)
    util.write_file(content, f"{content_storage}content.txt")
    prompts = text_model.generate_image_prompts(content)
    util.write_file(str(prompts), f"{content_storage}prompts.json")

    return (content, prompts)


def create_images(prompts: List[str], storage: str) -> str:
    image_storage = f"{storage}/images/"
    os.makedirs(image_storage)

    image_model = ImageModel(image_storage)
    timestamp = str(time.time())

    image_model.generate_images(prompts, timestamp)

    return image_storage


def create_audio(content: str, storage: str) -> str:
    audio_storage = f"{storage}/audio/"
    os.makedirs(audio_storage, exist_ok=True)

    audio_model = AudioModel(audio_storage)
    timestamp = str(time.time())
    file_path = audio_model.generate_audio(content, timestamp)

    return file_path


def create_subtitle(audio_filepath: str) -> List:
    subtitle_model = SubtitleModel()
    return subtitle_model.generate_subtitle(audio_filepath)

def image_caption(image_folder: str, storage: str) -> str:
    image_caption_model = ImageCaptionModel()
    # 返回字典，key是图片文件名，value是对应的caption
    captions = {
        fname: image_caption_model.caption(os.path.join(image_folder, fname))
        for fname in os.listdir(image_folder)
        if fname.lower().endswith((".png", ".jpg", ".jpeg"))
    }
    captions_storage = f"{storage}/content/"
    os.makedirs(captions_storage, exist_ok=True)
    util.write_file(str(captions), f"{captions_storage}captions.json")
    return captions

def get_story(captions: dict) -> str:
    text_model = TextModel()
    return text_model.generate_story(captions)

def create_video(
    audio_path: str,
    image_folder: str,
    subtitle: Optional[List],
    bgm_path: Optional[str],
    storage: str,
    image_order: List[str] | None = None
):
    video_path = f"{storage}/video.mp4"
    video_model = VideoModel(audio_path)
    video_model.set_video(image_folder, image_order=image_order)
    video_model.attach_audio(bgm_path)
    if subtitle:
        video_model.attach_subtitle(subtitle)
    video_model.generate_video(video_path)


@router.post("/text-to-video", tags=["video"], description="根据随机主题生成文本并创建视频")
async def text_to_video(
    topic: str = Form(default=None),
    # db: Session = Depends(db_depend.get_db),
    # baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    try:
        # 每次调用都获取新的存储路径
        storage = get_output_path()
        
        content, image_prompts = get_content(topic, storage)

        audio_path = create_audio(content, storage)

        subtitle = create_subtitle(audio_path)

        images_folder = create_images(image_prompts, storage)

        create_video(
            audio_path=audio_path,
            image_folder=images_folder,
            subtitle=subtitle,
            bgm_path="bgms/classic.mp3",
            storage=storage,
        )
        
        video_path = f"{storage}/video.mp4"
        return {
            "msg": "视频生成成功",
            "video_path": video_path,
            "storage_path": storage,
            "content": content[:200] + "..." if len(content) > 200 else content  # 返回内容摘要
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"视频生成失败: {str(e)}")

@router.post("/image-to-video", tags=["video"], description="根据图片文件夹中的图片生成故事视频")
async def image_to_video(
    image_folder: str = Form(default='/root/workspace/TimeCanvas/backend/media/images'),
    # db: Session = Depends(db_depend.get_db),
    # baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    try:
        # 每次调用都获取新的存储路径
        storage = get_output_path()
        
        # 检查图片文件夹是否存在
        if not os.path.exists(image_folder):
            raise HTTPException(status_code=404, detail=f"图片文件夹不存在: {image_folder}")
            
        # 检查文件夹中是否有图片文件
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        if not image_files:
            raise HTTPException(status_code=400, detail=f"图片文件夹中没有找到图片文件: {image_folder}")
        
        captions = image_caption(image_folder, storage)
        res = get_story(captions)
        story = res['story']
        ordered_images = res['ordered_images']
        print("排序后的图片顺序：", ordered_images)
        audio_path = create_audio(story, storage)
        subtitle = create_subtitle(audio_path)
        create_video(
            audio_path=audio_path,
            image_folder=image_folder,
            subtitle=subtitle,
            bgm_path="bgms/classic.mp3",
            storage=storage,
            image_order=ordered_images
        )
        
        video_path = f"{storage}/video.mp4"
        return {
            "msg": "视频生成成功",
            "video_path": video_path,
            "storage_path": storage,
            "story": story[:200] + "..." if len(story) > 200 else story,  # 返回故事摘要
            "image_count": len(image_files),
            "ordered_images": ordered_images
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"视频生成失败: {str(e)}")

#获取生成的视频文件流
@router.get("/generated-video/{storage_folder}", tags=["video"], description="获取生成的视频文件流")
def get_generated_video(
    storage_folder: str,
    # db: Session = Depends(db_depend.get_db),
    # baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    video_path = f"outputs/{storage_folder}/video.mp4"
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="生成的视频文件不存在")
    
    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="video/mp4")

#下载生成的视频文件
@router.get("/generated-video-download/{storage_folder}", tags=["video"], description="下载生成的视频文件")
def download_generated_video(
    storage_folder: str,
    # db: Session = Depends(db_depend.get_db),
    # baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    video_path = f"outputs/{storage_folder}/video.mp4"
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail="生成的视频文件不存在")
    
    filename = f"generated_video_{storage_folder}.mp4"
    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(
        iterfile(), 
        media_type="application/octet-stream", 
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )