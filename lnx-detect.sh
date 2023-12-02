#!/bin/bash

model_path="./models/best-model-20231202.pt"
source_directory="detection-images"


for image_file in "$source_directory"/*.jpg "$source_directory"/*.png "$source_directory"/*.gif; do
    echo "Processing: $image_file"
    yolo detect predict model="$model_path" source="$image_file"
done

echo "Batch processing complete."

