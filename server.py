from label_studio_ml.model import LabelStudioMLBase
from label_studio_ml.utils import get_single_tag_keys
from ocr_model import OCRModel
import os


class OCRLabeling(LabelStudioMLBase):
    def __init__(self, **kwargs):
        super(OCRLabeling, self).__init__(**kwargs)
        self.model = OCRModel()

    def predict(self, tasks, **kwargs):
        predictions = []
        for task in tasks:
            image_path = task["data"]["image"]
            # URL인 경우 로컬 파일 경로로 변환 필요
            if image_path.startswith("http"):
                # 여기에 URL 처리 로직 추가
                pass
            pred = self.model.predict(image_path)
            predictions.append(pred)
        return predictions


if __name__ == "__main__":
    os.system("label-studio-ml init ocr-model --script server.py")
    os.system("label-studio-ml start ocr-model")
