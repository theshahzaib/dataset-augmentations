# Dataset Augmentations
 Dataset Augmentations All in One

## Introduction
This code will do the augmentation of the dataset.

## Augmentations Types
```
'brightness', 'darken', 'add_shadow', 'add_rain', 'add_graval', 'add_speed', 'hsv', 'green', 'blue',
'red', 'hue', 'linearconstrast', 'gaussian_noise','change', 'add_blur', 'add_sun_flare', 'add_fog',
'add_autumn', 'change_temperature'
```
## Requirements
```
pip install -r requirements.txt
```

## Usage
```bash
python main_augmentations.py --images dataset/ --type add_shadow --ext jpg
```

## For all augmentationns (Default)
```bash
python main_augmentations.py 
```



