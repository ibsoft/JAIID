import os
import subprocess
from ultralytics import YOLO
import yaml
import glob



try:
    subprocess.run(['python', "lnx-convert-vot2yolo.py"], check=True)
    print(f"The script convert2yolo.py has been successfully executed.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the script: {e}")


with open('mydataset.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)

print(yaml_content)


# Create a new YOLO model from scratch
model = YOLO('models/best.pt')

#model.conf = 0.25  # confidence threshold (0-1)
#model.iou = 0.45  # NMS IoU threshold (0-1)

#results = model.train(data="mydataset.yaml", epochs=80, conf=0.5, iou=0.5)

results = model.train(data="mydataset.yaml", epochs=80, conf=0.5, iou=0.5)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
#results = model('best.pt')

# Export the model to ONNX format
#success = model.export(format='onnx')

#process

""" video_directory = 'detection-videos'

# Replace 'models/best.pt' with the path to your YOLO model
yolo_model = 'models/best.pt'

# Get all .mp4 files in the directory
mp4_files = glob.glob(os.path.join(video_directory, '*.mp4'))

# Specify the command to run YOLO detection
yolo_command = 'yolo detect predict model={} {}'

# Iterate over each .mp4 file and run YOLO detection
for mp4_file in mp4_files:
    try:
        # Construct the full YOLO command
        full_command = yolo_command.format(yolo_model, mp4_file)

        # Execute the YOLO command using subprocess
        subprocess.run(full_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing {mp4_file}: {e}") """