---
marp: true
paginate: true
---
<!-- _class: invert -->
<!-- _paginate: false -->
# Deep Convolutional Generative Adversarial Networks

## Fundamentals and Trends in Vision and Image Processing

### Hallison Paz
#### IMPA, November 11 2021

---

# Key contributions

- Proposal of architecture guidelines for training GANs using convolutions.
- Analysis of the potential of GANs as tools for unsupervised learning



--- 
# Why convolutions

- Spatial coeherence
* Translation invariance
* Multiscale
* Already a good strategy for analysis

---
# Architecture guidelines

- Replace pooling layers with [fractional-]strided convolutions
* Use batch normalization
* Remove fully connected hidden layers for deeper architectures 
* Use **ReLU** in generator, except for the output, which uses **Tanh**.
* Use **LeakyReLU** in the discriminator

---
# Generator Architecture

![](img/dcgan-generator.png)

---
# Discriminator Architecture

- Last layer is flattened and fed into a sigmoid output.

![bg left:60% h:40%](img/dcgan-discriminator.png)

---

# Pooling vs strided convolutions

![](img/convolution-1-1.png)

<!-- _footer: image from Fei-Fei Li & Justin Johnson & Serena Yeung (CS231n, 2017, lecture 11) -->

---
# Downsampling with Pooling

![](img/MaxpoolSample2.png)

---
# Downsampling with Strided convolutions

![](img/convolution-2-1.png)

<!-- _footer: image from Fei-Fei Li & Justin Johnson & Serena Yeung (CS231n, 2017, lecture 11) -->

---

# Upsampling strategies

![](img/upsampling.png)


<!-- _footer: image from Fei-Fei Li & Justin Johnson & Serena Yeung (CS231n, 2017, lecture 11) -->

---


# Fractional-strided convolutions

![](img/fractional-strided-jj.png)

<!-- _footer: image from Fei-Fei Li & Justin Johnson & Serena Yeung (CS231n, 2017, lecture 11) -->

---

# Fractional-strided convolutions

- Also called transposed convolution

![w:1280](img/transposedconvolution.png)

<!-- _footer: Image from [Transposed Convolution Demystified](https://towardsdatascience.com/transposed-convolution-demystified-84ca81b4baba)-->

---

# Batch Normalization

![](img/batch-normalization.png)

<!-- _footer: Image from https://stackoverflow.com/questions/65613694/calculation-of-mean-and-variance-in-batch-normalization-in-convolutional-neural -->

---

# Relu x Leaky-Relu

![w:1000](img/relu-leakyrelu.jpeg)

---
<!-- _class: invert -->
<!-- _paginate: false -->

# Training and Results

---
# Training details

* Training images scaling to the range of the tanh activation function [-1, 1]
* SGD with a mini-batch size of 128
* Weights initialized from a zero-centered Normal distribution (std=0.02). 
* In the LeakyReLU, the slope was set to 0.2 
* Adam optimizer using lr=0.0002 and momentum term $β_1=0.5$

---
# Results

![](img/lsun-epoch1.png)

<!-- _footer: Generated bedrooms after one epoch of training on LSUN -->
---
# Results

![](img/lsun-epoch5.png)

<!-- _footer: Generated bedrooms after five epochs of training on LSUN -->
---

<!-- _class: invert -->
<!-- _paginate: false -->

# GANs as Tools for Unsupervised Learning

---

# Visualizing features activations

- The discrimator learned relevant features of the scene

<br/>

![w:1200](img/activation-maps.png)

---
# Using features for supervised learning

- Using discriminator's features to train a SVM classifier
<br/>

![](img/supervised-table.png)

---
# Walking in the latent space

![](img/latent-space.png)

<!-- _footer: Latent space interpolation -->

---
# Walking in the latent space

- Interpolation has semantics; 
  - It learns a manifold.
* An interesting test to validate results

![bg right:40% h:780](img/latent-space.png)

---
# Vector Arithmetic

![](img/vector-arithmetic.png)


---

<!-- _class: invert -->
<!-- _paginate: false -->
# Let's see it in practice...

## ...next class! #statytuned