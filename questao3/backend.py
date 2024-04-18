from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np

app = FastAPI()

# Permitindo solicitações CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para receber e processar imagens
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Lendo a imagem
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Realizando uma análise simples usando OpenCV
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        # Contando o número de objetos na imagem (apenas para fins de exemplo)
        _, contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        num_objects = len(contours)

        return {"num_objects": num_objects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
