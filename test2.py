from transformers import AutoTokenizer, VisionEncoderDecoderModel, AutoImageProcessor
from PIL import Image
import requests

feature_extractor = AutoImageProcessor.from_pretrained("MixTex/ZhEn-Latex-OCR")
tokenizer = AutoTokenizer.from_pretrained("MixTex/ZhEn-Latex-OCR", max_len=296)
model = VisionEncoderDecoderModel.from_pretrained("MixTex/ZhEn-Latex-OCR")

rq = requests.get('https://cdn-uploads.huggingface.co/production/uploads/62dbaade36292040577d2d4f/eOAym7FZDsjic_8ptsC-H.png', stream=True)
imgen = Image.open(rq.raw)

#imgzh = Image.open(requests.get('https://cdn-uploads.huggingface.co/production/uploads/62dbaade36292040577d2d4f/m-oVg8dsQbQZ1fDWbwKtO.png', stream=True).raw)
imgen = Image.open('pdf_to_test/one_calculus_big.png')
print(tokenizer.decode(model.generate(feature_extractor(imgen, return_tensors="pt").pixel_values)[0]).replace('\\[','\\begin{align*}').replace('\\]','\\end{align*}'))
