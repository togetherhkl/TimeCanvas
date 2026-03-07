import json
import ollama
from typing import List


class TextModel:
    def generate_content(self, topic: str="an historical inspiring fact that changed today's computer science world") -> str:

        system_message = """
        You are a YouTube Shorts Assistant help me to generate content. 
        No explanation, No additional text, No additional decorations, No screenplay, only content as plain paragraph but include commas, exclamations, question marks accordingly. 
        Use simple english, No roman representations.
        Ask for like, share and subscribe at the end of content.
        """

        user_message = f"""
        Create a 40-second content about {topic},

        Did you know...
        """

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_message.strip()},
                {"role": "user", "content": user_message.strip()},
            ],
        )

        content = response["message"]["content"]
        final_response = f"Welcome to the channel, {content}"

        return final_response

    def generate_image_prompts(self, content: str) -> List[str]:
        system_message = """
        You are an artist and a prompt engineer who could describe image in words clearly by a content sequentially. 
        No explanation, No additional text, No additional decorations, only list of strings as array as response. 

        Response has to be strictly json list of strings. No string prefix or suffix around json output.
        """

        user_message = f"""
        Give list of 5 descriptive, clear image prompts for below content sequentially

        Return ONLY a valid JSON array of strings.

        {content}
        """

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_message.strip()},
                {"role": "user", "content": user_message.strip()},
            ],
        )

        content = response["message"]["content"]
        # print('大模型生成的图片提示词原始内容：', content)
        final_response = json.loads(content)

        return list(final_response)
    
    def generate_story(self, captions_dict: dict):
        """
        captions_dict: {filename: caption}
        Returns:
        {
            "ordered_images": ["1.png", "2.png", ...],
            "story": "Full story text"
        }
        """

        # System message: defines LLM behavior
        system_message = """
            You are a story planner and writer.
            Your task:
            1. Sort the given images in a logical order to form a coherent story.
            2. Based on the sorted images, generate a short, engaging story suitable for narration.
            The output must be in JSON format:
            {"ordered_images": [list of filenames in story order],
            "story": "the story text"}
            Please:
            - Determine the logical sequence of images for the story
            - Generate a short story based on the ordered images
            - Return ONLY valid JSON containing "ordered_images" and "story"
            - Do NOT include any explanation, notes, or extra text
        """

        # User message: provide captions
        caption_text = "\n".join([f"{k}: {v}" for k, v in captions_dict.items()])

        user_message = f"""
            Here are the images with their captions:
            {caption_text}

            Please:
            - Determine the logical sequence of images for the story
            - Generate a short story based on the ordered images
            - Return ONLY valid JSON containing "ordered_images" and "story"
        """

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_message.strip()},
                {"role": "user", "content": user_message.strip()},
            ],
        )

        # Parse LLM output as JSON
        content = response["message"]["content"]
        # print('大模型生成的故事和图片顺序原始内容：', content)
        final_response = json.loads(content)

        return final_response
