from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import json


class OCRModel:
    def __init__(self):
        # Microsoft의 TrOCR 모델 사용
        self.processor = TrOCRProcessor.from_pretrained(
            "microsoft/trocr-base-handwritten"
        )
        self.model = VisionEncoderDecoderModel.from_pretrained(
            "microsoft/trocr-base-handwritten"
        )

    def predict(self, image_path):
        # 이미지 로드 및 전처리
        image = Image.open(image_path).convert("RGB")
        pixel_values = self.processor(image, return_tensors="pt").pixel_values

        # 예측 수행
        generated_ids = self.model.generate(pixel_values)
        generated_text = self.processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )[0]

        # Label Studio 형식으로 결과 반환
        result = {
            "result": [
                {
                    "value": {"text": [generated_text]},
                    "type": "textarea",
                    "to_name": "image",
                    "from_name": "transcription",
                }
            ]
        }
        return result
