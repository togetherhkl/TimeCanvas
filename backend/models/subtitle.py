import whisperx
from typing import List


class SubtitleModel:
    def __init__(self):
        self.model = whisperx.load_model("medium", device="cpu", compute_type="float32")

    def generate_subtitle(self, audio_filepath: str) -> List:
        result = self.model.transcribe(audio_filepath) # 使用 WhisperX 进行语音转文本，得到初步的字幕结果，包括每个单词的起止时间和文本内容
        model_a, metadata = whisperx.load_align_model( # 加载 WhisperX 的对齐模型，用于将初步的字幕结果进行时间对齐，得到更准确的字幕时间戳
            language_code=result["language"], device="cpu"
        )
        aligned = whisperx.align( # 对初步的字幕结果进行时间对齐，得到更准确的字幕时间戳，输出格式为每个单词的起止时间和文本内容
            result["segments"], model_a, metadata, audio_filepath, device="cpu"
        )

        print("✅ Subtitles generated!")

        subtitle = []
        for word_data in aligned["word_segments"]:
            subtitle.append(word_data)

        return subtitle
