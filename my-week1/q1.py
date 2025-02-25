import torch

# 1. Reshaping a Tensor
print("---- Reshaping ----")
tensor_reshape = torch.tensor([[1, 2, 3], [4, 5, 6]])
reshaped_tensor = tensor_reshape.reshape(3, 2)
print("Original Tensor:\n", tensor_reshape)
print("Reshaped Tensor:\n", reshaped_tensor)
