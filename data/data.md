# Dataset info
This dataset is the subset of **[MS COCO2017](https://cocodataset.org/#home)** with train and val dataset with annotations
```cmd
coco2017
    ├──annotations
    │  ├──captions_train2017.json
    │  ├──captions_val2017.json
    │  ├──clean.py
    │  ├──data_analysis.ipynb
    │  ├──train_captions_custom.json
    │  └──val_captions_custom.json
    ├──train2017
    │  ├───000000000009.jpg
    │  └───<contain many images>
    └──val2017
       ├───000000000245.jpg
       └───<contain many images>
```
## Download Method
Since the download was slow from the [official website](https://cocodataset.org/#home), I used the following method to download the dataset:
- **[Kaggle dataset](https://www.kaggle.com/datasets/awsaf49/coco-2017-dataset)**
- **aria2** 
    - Install [**arria2 build**](https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0-win-64bit-build1.zip) from github
    - Extract it and add to path
    - then in cmd run the following command:
        ```cmd
        aria2c -x 16 -s 16 http://images.cocodataset.org/zips/train2017.zip
        ```

## Data Cleaning
- **clean.py** - This file is used to clean the dataset and create a custom dataset with only 5 captions per image.
- **data_analysis.ipynb** - This file is used to analyze the dataset and create a custom dataset with only 5 captions per image.
- **train_captions_custom.json** - This file is the custom dataset with only 5 captions per image for training.
- **val_captions_custom.json** - This file is the custom dataset with only 5 captions per image for validation.
