from moviepy.editor import *
import os
from typing import List


class VideoModel:
    def __init__(self, audio_path: str):
        self.audio = AudioFileClip(audio_path)
        self.audio_duration = self.audio.duration

    def set_video(self, image_folder: str, image_order: List[str] | None = None):
        if image_order:
            image_files = [os.path.join(image_folder, fname) for fname in image_order]
        else:
            image_files = sorted(
                [
                    os.path.join(image_folder, fname)
                    for fname in os.listdir(image_folder)
                    if fname.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
        )

        image_duration = self.audio_duration / len(image_files)
        image_clips = [
            VideoEffects.add_fade_effect(path, image_duration) for path in image_files # 设置谈入淡出效果
        ]
        base_video = concatenate_videoclips(image_clips, method="compose", padding=-0.5) # 拼接图片片段，设置图片之间的重叠时间为0.5秒，增强连贯感

        # Calculate leftover time
        leftover = self.audio_duration - base_video.duration # 处理剩余音频时间：用一张图片生成视频片段补齐剩余时间

        filler_clip = (
            ImageClip("media/filler.png")
            .set_duration(leftover)
            .resize(base_video.size)
            .fadein(0.2) # fadein 和 fadeout 做平滑过渡
            .fadeout(0.2)
        )

        self.video = concatenate_videoclips([base_video, filler_clip], method="compose")

    def attach_audio(self, bgm_path: str | None = None): # 给视频加音频（原音 + 背景音乐）
        audios = [self.audio] # 原音
        if bgm_path:
            bgm = AudioFileClip(bgm_path).volumex(0.2).set_duration(self.audio_duration) # 背景音乐，音量调小，持续时间与原音一致
            audios.append(bgm)
        composite_audio = CompositeAudioClip(audios) # 混合原音和背景音乐
        self.video = self.video.set_audio(composite_audio) # 将混合后的音频设置到视频上

    def attach_subtitle(self, subtitles: List): # 给视频加字幕，字幕内容来自 WhisperX 生成的字幕列表
        group_size = 4 # 每4个单词为一组，生成一个字幕片段
        grouped = []

        for i in range(0, len(subtitles), group_size):
            group = subtitles[i : i + group_size]
            full_text = " ".join([w["word"] for w in group])
            grouped.append(
                {
                    "word": full_text,
                    "start": group[0]["start"],
                    "end": group[-1]["end"],
                    "words": group,
                }
            )

        self.video = SubtitleEffects.simple_subtitle(self.video, grouped) # 生成文字视频叠加到原视频上

    def generate_video(self, output_path: str):
        self.video.write_videofile(
            output_path,
            fps=24,
            codec="libx264", # 视频编码格式
            audio_codec="aac", # 音频编码格式
            audio=True,
        )

        print(f"🔊 Has audio: {self.video.audio is not None}")


class VideoEffects: # 视频特效类，包含图片淡入淡出、缩放等效果

    @staticmethod 
    def add_fade_effect(image_path, duration=3.0, fade_duration=0.5): # 图片淡入淡出效果，默认每张图片持续3秒，淡入淡出各0.5秒
        clip = ImageClip(image_path).set_duration(duration)
        clip = clip.fadein(fade_duration).fadeout(fade_duration)
        return clip

    @staticmethod
    def apply_shaky_zoom( # 图片缩放效果，默认从1倍缩放到1.1倍，持续时间内线性变化，并且加上淡入淡出效果
        image_path, duration, zoom_start=1.0, zoom_end=1.1, fade_duration=0.5
    ):
        # Load image as clip
        clip = ImageClip(image_path).set_duration(duration)

        # Apply zoom using a lambda-based resize (linear interpolation over time)
        zoomed = clip.resize(
            lambda t: zoom_start + (zoom_end - zoom_start) * (t / duration)
        )

        # Apply fade-in and fade-out
        zoomed = zoomed.fadein(fade_duration).fadeout(fade_duration)

        return zoomed

    @staticmethod
    def apply_stable_zoom( # 图片缩放效果，保持中心位置不变，默认从1倍缩放到1.1倍，持续时间内线性变化，并且加上淡入淡出效果
        image_path, duration, zoom_start=1.0, zoom_end=1.1, fade_duration=0.5
    ):
        clip = ImageClip(image_path).resize(height=720).set_duration(duration)

        w, h = clip.size

        def crop_zoom(get_frame, t):
            factor = zoom_start + (zoom_end - zoom_start) * (t / duration)
            new_w, new_h = int(w / factor), int(h / factor)
            x_center, y_center = w // 2, h // 2
            return (
                clip.crop(
                    x_center=x_center, y_center=y_center, width=new_w, height=new_h
                )
                .resize((w, h))
                .get_frame(t)
            )

        zoomed = clip.fl(crop_zoom, apply_to=["mask"])

        return zoomed.fadein(fade_duration).fadeout(fade_duration)


class SubtitleEffects: # 字幕特效类，包含简单字幕生成等功能
    @staticmethod
    def simple_subtitle(video, subtitle: List): # 生成简单字幕，字幕内容来自 WhisperX 生成的字幕列表，每4个单词为一组，生成一个字幕片段，字幕位置居中，字体为 Impact，带黑色描边，背景半透明黑色框
        subtitle_clips = []
        for word_info in subtitle:
            word = word_info["word"]
            start = word_info["start"]
            duration = word_info["end"] - word_info["start"]

            txt_clip = (
                TextClip(
                    word,
                    fontsize=50,
                    color="white",
                    bg_color="rgba(0,0,0,0.4)",
                    font="Impact",
                    stroke_color="black",
                    stroke_width=2,
                    method="caption",  # enables word wrapping
                    size=(
                        video.w - 100,
                        None,
                    ),  # wrap at screen width - 100px padding
                )
                .set_position(("center", "center"))
                .set_start(start)
                .set_duration(duration)
                .fadein(0.01)
            )

            subtitle_clips.append(txt_clip)

        return CompositeVideoClip([video] + subtitle_clips)
