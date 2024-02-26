from fastapi import APIRouter, File, UploadFile
from PIL import Image
import toml
import io
from torchvision import transforms
from torchvision.models import vgg13, VGG13_Weights
from torch import load, device

MODEL_PATH = "./models/VGG13_Weights_1e-06.pt"
PATH_TO_MODEL_CONFIG_TOML = "./model.toml"

model_config = toml.load(PATH_TO_MODEL_CONFIG_TOML)

def get_model(model_path:str=MODEL_PATH):
    # Initialize and return PyTorch model
    model = vgg13(
        weights=VGG13_Weights.IMAGENET1K_V1,
        progress=True
    )
    # Load pre-trained weights 
    model = load(model_path, map_location=device('cpu'))
    return model

model = get_model().to("cpu")


# Define transforms
transform = transforms.Compose([
    transforms.Resize(size=(360,360)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)
    predictions = model(input_tensor)
    predicted_label = predictions.argmax(1)[0].item()
    return {"prediction": model_config["labels"][f"{predicted_label}"]}