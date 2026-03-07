import os
import torch
import time
from diffusers import StableDiffusionPipeline
from typing import List


class ImageModel:
    def __init__(self, storage_path: str = ""):
        self.storage_path = storage_path

        print("🔄 Loading image model...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "SG161222/Realistic_Vision_V5.1_noVAE",
            torch_dtype=torch.float32,
            safety_checker=None,
            feature_extractor=None,
        ).to("cuda")
        print("✅ Image Model loaded")

        self.generator = torch.manual_seed(42)

        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        os.environ["HF_HUB_OFFLINE"] = "1"

    def generate_image(self, prompt: str, filename: str):
        outfile_path = f"{self.storage_path}{filename}.png"

        image = self.pipe(
            prompt=prompt,
            height=848,
            width=480,
            num_inference_steps=40,
            generator=self.generator,
        ).images[0]

        image.save(outfile_path)
        print(f"✅ Image saved as {outfile_path}")

    def generate_images(self, prompts: List[str], filename_prefix: str):
        for i, prompt in enumerate(prompts, start=1):
            self.generate_image(prompt, f"{filename_prefix}_{i}")


from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptionModel:

    def __init__(self):

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-large", # 
            # local_files_only=True # 只从本地加载模型，避免在线下载，确保在离线环境下也能使用
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-large",
            # local_files_only=True # 只从本地加载模型，避免在线下载，确保在离线环境下也能使用
        ).to("cuda")

    def caption(self, image_path):

        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(image, return_tensors="pt").to("cuda")

        out = self.model.generate(**inputs)

        caption = self.processor.decode(out[0], skip_special_tokens=True)

        return caption
    
if __name__ == "__main__":
    image_caption_model = ImageCaptionModel()
    image_folder = "/root/workspace/video-creator/outputs/37/images"
    
    # 返回字典，key是图片文件名，value是对应的caption
    captions = {
        fname: image_caption_model.caption(os.path.join(image_folder, fname))
        for fname in os.listdir(image_folder)
        if fname.lower().endswith((".png", ".jpg", ".jpeg"))
    }
    print(captions)