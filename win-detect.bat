@echo off
setlocal enabledelayedexpansion

set "model_path=.\models\best-model-20231202.pt"
set "source_directory=detection-images"


mkdir %output_directory%

for %%i in (%source_directory%\*.jpg %source_directory%\*.png %source_directory%\*.gif) do (
    set "image_file=%%i"
    echo Processing: !image_file!
    yolo detect predict model=!model_path! source=!image_file!
)

echo Batch processing complete.
pause
