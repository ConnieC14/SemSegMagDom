# Magnetization Domain Semantic Segmentation

Conducted research in magnetization domain semantic segmentation using a novel adaptation of semi-supervised AugSeg model and fully supervised segment-anything model.

## Background
3D Imaging of magnetization domains at nanoscale has been one of the challenging research areas
which is being explored in the last few years. 3D Imaging reveals the nanoscale electronic and structural
heterogeneities which are prevalent in condensed matter physics and beyond. Using ptycho-
tomography based computational imaging techniques, the 3D magnetization domains are
reconstructed. However, the magnetic signals are very weak and the data acquired is in low Signal to
Noise Ratio (SNR) regime with additional noise / artifacts in the 2D images. During the vector
tomographic reconstruction of the 3D magnetization domains from these 2D images, there is presence
of noise and artifacts which corrupt the magnetization domains. In this project, we utilized both
supervised and semi-supervised deep learning (DL) approaches to segment and identify these 3D
magnetization domains for 2D slices of the object.

## Results
A total of 2448 2D magnetization domain image slices were utilized for the AugSeg model. This model
was trained over 30 epochs with 2298 training samples, 128 labelled samples, and 22 validation
samples. A batch size of 15 was used and training was split across 2 GPUs using distributed parallelizing.
The code infrastructure was modified from an existing code base to support this dataset. A pretrained
resnet101 model was used for the model’s encoder, and a deeplabv3 decoder was used.

<img width="555" alt="image" src="https://github.com/user-attachments/assets/5e9e0b47-92a1-42f7-8f58-23db666ea0aa">

## Contributions
- Implemented and adapted ML models (PyTorch, TensorFlow) for accurate segmentation of magnetization domains, significantly reducing noise and artifacts.
- Led the manual labeling effort of 150 images to create a high-quality dataset for training and validation.

## References
- [1] MINAEE, SHERVIN, ET AL. “IMAGE SEGMENTATION USING DEEP LEARNING: A SURVEY.” IEEE TRANSACTIONS ON
PATTERN ANALYSIS AND MACHINE INTELLIGENCE, 2021, PP. 1–1. CROSSREF,
https://doi.org/10.1109/tpami.2021.3059968.
- [2] PELÁEZ-VEGAS, ADRIAN, PABLO MESEJO, AND JULIÁN LUENGO. "A SURVEY ON SEMI-SUPERVISED SEMANTIC
SEGMENTATION." ARXIV PREPRINT ARXIV:2302.09899 (2023).
- [3] ZHAO, ZHEN, ET AL. "AUGMENTATION MATTERS: A SIMPLE-YET-EFFECTIVE APPROACH TO SEMI-SUPERVISED
SEMANTIC SEGMENTATION." PROCEEDINGS OF THE IEEE/CVF CONFERENCE ON COMPUTER VISION AND
PATTERN RECOGNITION. 2023.
