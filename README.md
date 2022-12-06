# Dataset Augmentations
 Dataset Augmentations All in One

## Introduction
This code will do the augmentation of the dataset.

## Augmentations Types
`
'brightness', 'darken', 'add_shadow', 'add_rain', 'add_graval', 'add_speed', 'hsv', 'green', 'blue', 'red', 'hue', 'linearconstrast', 'gaussian_noise', 'change', 'add_blur', 'add_fog', 'add_autumn', 'change_temperature'
`
## Requirements
```
pip install -r requirements.txt
```

## Usage
```shell
python main.py --images dataset/ --type add_shadow --ext jpg
```

## For all augmentations (Default)
```bash
python main.py
```



