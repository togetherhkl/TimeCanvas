from TTS.api import TTS


class AudioModel:
    def __init__(self, storage_path: str = ""):
        self.storage_path = storage_path
        self.tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)
        self.speaker = self.tts.speakers[104] # 选择一个特定的说话人，104是VCTK数据集中一个说话人的ID，可以根据需要选择其他说话人

    def generate_audio(self, content: str, filename: str):
        outfile_path = f"{self.storage_path}{filename}.wav"

        self.tts.tts_to_file(
            text=content,
            file_path=outfile_path,
            speaker=self.speaker,
            speed=0.95, # 调整语速，0.95表示比原始语速慢5%，可以根据需要进行微调
            pitch=0.8, # 调整音调，0.8表示比原始音调低20%，可以根据需要进行微调
        )

        print(f"✅ Audio generated! {outfile_path}")

        return outfile_path
