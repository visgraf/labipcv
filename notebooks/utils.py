import imageio
import matplotlib.pyplot as plt
import os
import pickle
import torch


def images_to_vectors(images, d):
    return images.view(images.size(0), d * d)

def vectors_to_images(vectors, d):
    return vectors.view(vectors.size(0), 1, d, d)

# Noise
def noise(size, nz, device):
    return torch.randn(size, nz, 1, 1, device=device)

def real_data_target(size, device):
    '''
    Tensor containing ones, with shape = size
    '''
    return torch.ones(size).to(device)

def fake_data_target(size, device):
    '''
    Tensor containing zeros, with shape = size
    '''
    return torch.zeros(size).to(device)

# Visualization
def log_images(test_images, savepath):
  figure = plt.figure(figsize=(8, 8))
  figure.subplots_adjust(wspace=-0.08, hspace=0.01)
  rows, cols = len(test_images)//4, 4
  for i, img in enumerate(test_images):
      figure.add_subplot(rows, cols, i+1)
      plt.axis("off")
      if img.shape[0] == 1:
        plt.imshow(img.squeeze(), cmap='gray')
      else:  
        plt.imshow(img.squeeze().transpose(1, 2, 0))
  
  figure.savefig(savepath)
  plt.show()
  
def save_models(generator, discriminator, epoch, folder):
  torch.save(generator, os.path.join(folder, f"generator_e{epoch}.pth"))
  torch.save(discriminator, os.path.join(folder, f"discriminator_e{epoch}.pth"))

def load_models(epoch, folder):
  generator = torch.load(os.path.join(folder, f"generator_e{epoch}.pth"))
  discriminator = torch.load(os.path.join(folder, f"discriminator_e{epoch}.pth"))
  return generator, discriminator

def save_losses(g_loss, d_loss, epoch, folder):
  with open(os.path.join(folder, f"gloss_{epoch}.pickle"), 'wb') as f:
    pickle.dump(g_loss, f)
  with open(os.path.join(folder, f"dloss_e{epoch}.pickle"), 'wb') as f:
    pickle.dump(d_loss, f)

def load_losses(epoch, folder):
  with open(os.path.join(folder, f"gloss_{epoch}.pickle"), 'rb') as f:
    g_loss = pickle.load(f)
  with open(os.path.join(folder, f"dloss_e{epoch}.pickle"), 'rb') as f:
    d_loss = pickle.load(f)
  return g_loss, d_loss

def plot_losses(losses):
  fig = plt.figure(figsize=(16, 8))
  ax = fig.gca()
  for loss_name, loss_values in losses.items():
    loss_values = [k.item() for k in loss_values]  
    ax.plot(loss_values, label=loss_name)
  ax.legend(fontsize="16")
  ax.set_xlabel("Iteration", fontsize="16")
  ax.set_ylabel("Loss", fontsize="16")
  ax.set_title("Loss vs iterations", fontsize="16");

def make_gif(gifpath, source_dir):
  images = []
  for filename in sorted(os.listdir(source_dir), key = lambda x: float(x.split('.')[0])):
      if filename.endswith('.jpg'):
          filepath = os.path.join(source_dir, filename)
          images.append(imageio.imread(filepath))
  imageio.mimsave(gifpath, images)