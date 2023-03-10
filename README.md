# ID2223 Lab 2

This repository contains our solution to the second lab assignment in the KTH course ID2223. The purpose of the lab was to fine-tune a transformer model to transcribe Swedish from audio to text. Most of the code was based on a sample Google Colab notebook provided in the course, with some minor adjustments being made. The original notebook was divided into two new notebooks: feature_pipeline2.ipynb and training2.ipynb. Feature_pipeline2.ipynb downloads the data, prepares it and stores it in Google Drive. Training2.ipynb retrieves the saved data and trains the model. The file app.py is for the user interface in HuggingFace.

Due to time constraints, the model has been downsized to do 1000 max steps and checkpoint every 200th step. The amount of training, validation and test data used has also been lowered to 30 % of each since we were otherwise unable to save the files to Google Drive.

## Links
* The model in HuggingFace: https://huggingface.co/SebLih/whisper-SV3
* The interactive application in HuggingFace: https://huggingface.co/spaces/SebLih/SV-Transcription

At the moment we are experiencing an unexpected build error in the HuggingFace space for the interactive application ("build failed with exit code: 1, message: None"); some research into this particular error suggests that this is a problem with HuggingFace itself and not our code ([1](https://discuss.huggingface.co/t/build-error-with-empty-log/19754/7), [2](https://discuss.huggingface.co/t/build-error-with-hello-world-gradio-example-logs-dont-contain-an-obvious-error/19738), [3](https://discuss.huggingface.co/t/build-error-no-log/19747)); we are currently also get the same issue when trying to restart our previously working lab 1 apps. The file app.ipynb is a version of app.py that can be run in Google Colab and creates a functional local version of the app.

## Ways to improve performance
Because of Google Colab GPU user limits it was difficult to test a large amount of parameters or alternative approaches, which means that the performance of the final model is limited. We tested different values for the different training arguments but given the time required to run the code only very few configurations could be tested. Given more time, it would have been possible to improve the model in various ways:

### Model-centric approach
Improving performance through a model-centric approach would mean to make improvements to the model directly, such as making adjustments to its architecture or fine-tuning the hyperparameters. It would definitely have been possible to work on fine-tuning the hyperparameters if we would have had more time and if we could have avoided the Google Colab GPU user limits. 

### Data-centric approach
Improving performance through a data-centric approach would mean that improvements are made to the quality of the data. In the case of this lab, this could perhaps be done either through experimenting with the dataset that is already being used (several features are removed - should any of these be retained and/or are there more features that are unnecessary) or trying to find an even larger Swedish-language dataset.
