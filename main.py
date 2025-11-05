import os
import uuid
import shutil
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
from ultralytics import YOLO

# 1. Initialize API Application
app = FastAPI(title="YOLOv8 Traffic Detection API")
try:
    model = YOLO("best.pt")
except Exception as e:
    print(f"Error loading model 'best.pt': {e}")
    model = None

def cleanup_files(temp_file_path: str, result_folder_path: str):
    """Background task to delete temp files & folders"""
    try:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
            print(f"File temp {temp_file_path} deleted.")
        if os.path.exists(result_folder_path):
            shutil.rmtree(result_folder_path)
            print(f"Folder result {result_folder_path} deleted.")
    except OSError as e:
        print(f"Error while cleanup: {e}")

@app.post("/predict")
async def predict(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    """
    Receives files (images/videos), performs detection, 
    and returns the resulting files.
    """
    if not model:
        return {"error": "Model 'best.pt' failed to load."}

    # create uniqe file name
    file_extension = os.path.splitext(file.filename)[1]
    temp_file_path = f"temp_{uuid.uuid4()}{file_extension}"

    # save file into the temp folder
    try:
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())
    except Exception as e:
        return {"error": f"failed to save: {e}"}

    try:
        results = model.predict(temp_file_path, save=True)
    except Exception as e:
        os.remove(temp_file_path)
        return {"error": f"Failure to execute model predictions: {e}"}

    # Specify the path of the output file
    result_folder_path = results[0].save_dir
    result_file_path = os.path.join(result_folder_path, os.path.basename(temp_file_path))

    # cleanup
    background_tasks.add_task(cleanup_files, temp_file_path, result_folder_path)

    #Send the resulting file back to the user
    return FileResponse(
        result_file_path,
        media_type=file.content_type,
        filename=f"result_{file.filename}"
    )

@app.get("/")
def read_root():
    return {"Halo": "Welcome to your Traffic Detection API. Use the /docs endpoint to view the documentation."}