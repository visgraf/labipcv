---
marp: true
theme: blue
---
<!-- _class: invert -->

# Deep Convolutional Generative Adversarial Networks

### Hallison Paz

1. Explicar Batch normalization
2. Explicar strided convolution ("learn pooling")
3. Explicar como eliminar fully connecterd

---

# Contributions

- Architectures for training GANs using convolutions.
- 



--- 
# Why convolutions

- Spatial coeherence
* Translation invariance
* Multiscale
* Already a good strategy for analysis

---
# Convolutional architectures mean

- Higher resolution
* Deeper models WHY???

---
# What took it so long?

- From 2014 -> 2016

---
# Key ideas to make convolutional GANs work

- Replace pooling for strided convolutions
* Eliminate fully connected layers
* Add **batch normalization**

---
# Generator Architecture

![](img/dcgan-generator.png)

---
# Discriminator Architecture

![h:400](img/dcgan-discriminator.png)

---
# Training
No pre-processing was applied to training images besides scaling to the range of the tanh activation function [-1, 1]. All models were trained with mini-batch stochastic gradient descent (SGD) with a mini-batch size of 128. All weights were initialized from a zero-centered Normal distribution with standard deviation 0.02. In the LeakyReLU, the slope of the leak was set to 0.2 in all models. While previous GAN work has used momentum to accelerate training, we used the Adam optimizer (Kingma & Ba, 2014) with tuned hyperparameters. We found the suggested learning rate of 0.001, to be too high, using 0.0002 instead. Additionally, we found leaving the momentum term β1 at the

---
# Results

![](img/lsun-epoch1.png)

---
# Results

![](img/lsun-epoch5.png)


---
# Unsupervised learning

![](img/latent-space.png)

---
# Walking in the latent space

- Interpolation has semantics
* A test to validate results

![bg right:40% h:780](img/latent-space.png)

---
# Vector Arithmetic

![](img/vector-arithmetic.png)

---

# Practice

### Next class! #statytuned