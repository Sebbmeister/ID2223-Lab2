# ID2223 Lab 2

This repository contains our solution to the second lab assignment in the KTH course ID2223. The purpose of the lab was to fine-tune a transformer model to transcribe Swedish from audio to text. Most of the code was based on a sample Google Colab notebook provided in the course, with some minor adjustments being made. The original notebook was divided into two (feature_pipeline.ipynb and training.ipynb). The file app.py is for the user interface in HuggingFace. Due to time constraints, the model has been downsized to do 1000 max steps and checkpoint every 200th step. The amount of training, validation and test data used has also been lowered to 30 % of each since we were otherwise unable to save the files to Google Drive.

## Links
* The model in HuggingFace: https://huggingface.co/SebLih/whisper-SV3
* The interactive application in HuggingFace:

## Ways to improve performance
Because of Google Colab GPU user limits it was difficult to test a large amount of parameters or alternative approaches, which means that the performance of the final model is limited. We tested different values for the different training arguments but given the time required to run the code only very few configurations could be tested. Given more time, it would have been possible to improve the model in various ways:

### Model-centric approach
Improving performance through a model-centric approach would mean to make improvements to the model directly, such as making adjustments to its architecture or fine-tuning the hyperparameters. It would definitely have been possible to work on fine-tuning the hyperparameters if we would have had more time and if we could have avoided the Google Colab GPU user limits. 

### Data-centric approach
Improving performance through a data-centric approach would mean that improvements are made to the quality of the data. In the case of this lab, this could perhaps be done either through experimenting with the dataset that is already being used (several features are removed - should any of these be retained and/or are there more features that are unnecessary) or trying to find an even larger Swedish-language dataset.
