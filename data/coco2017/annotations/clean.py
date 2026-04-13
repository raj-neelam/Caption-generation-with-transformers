train_data_dir = "captions_train2017.json"
val_data_dir = "captions_val2017.json"

import json

with open(train_data_dir, "r") as f:
    train_data = json.load(f)

with open(val_data_dir, "r") as f:
    val_data = json.load(f)

# train_data cleaning

id_to_file = {img['id']: img['file_name'] for img in train_data['images']}

samples = {}

for ann in train_data['annotations']:
    img_id = ann['image_id']
    file_name = id_to_file[img_id]
    samples[file_name] = []

for ann in train_data['annotations']:
    img_id = ann['image_id']
    caption = ann['caption']
    file_name = id_to_file[img_id]
    samples[file_name].append(caption)


with open("train_captions_custom.json", "w") as f:
    json.dump(samples, f, indent=4)

# val_data cleaning

id_to_file = {img['id']: img['file_name'] for img in val_data['images']}

samples = {}

for ann in val_data['annotations']:
    img_id = ann['image_id']
    file_name = id_to_file[img_id]
    samples[file_name] = []

for ann in val_data['annotations']:
    img_id = ann['image_id']
    caption = ann['caption']
    file_name = id_to_file[img_id]
    samples[file_name].append(caption)


with open("val_captions_custom.json", "w") as f:
    json.dump(samples, f, indent=4)

