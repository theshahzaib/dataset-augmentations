# Dataset Augmentations
 Dataset Augmentations All in One

## Introduction
This code will do the augmentation of the labeled dataset.

## Augmentations Types
`
'brightness', 'darken', 'add_shadow', 'add_rain', 'add_graval', 'add_speed', 'hsv', 'green', 'blue', 'red', 'hue', 'linearconstrast', 'gaussian_noise', 'change', 'add_blur', 'add_fog', 'add_autumn', 'change_temperature'
`
## Requirements
```
pip install -r requirements.txt
```

## Steps
Place the images and the labels in the same folder. `The labels should be in the same name as the image with the extension .txt`

## Usage
```shell
python main.py --images dataset/ --ext jpg --type add_shadow
```

## For all augmentations (Default)
```bash
python main.py
```



