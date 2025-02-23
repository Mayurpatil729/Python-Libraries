<!-- @format -->

## Autograd in PyTorch

Autograd in PyTorch is an automatic differentiation engine that tracks computations on tensors and computes gradients for optimization. It dynamically creates a computational graph and efficiently performs backpropagation. This is crucial for training deep learning models, as it automates gradient calculation.

## Important Functions in Autograd

1. **`requires_grad=True`** → Enables gradient tracking for a tensor.
2. **`.backward()`** → Computes gradients using backpropagation.
3. **`.grad`** → Accesses the computed gradient of a tensor.
4. **`detach()`** → Returns a new tensor without gradient tracking.
5. **`torch.no_grad()`** → Temporarily disables autograd (useful for inference).
6. **`torch.autograd.grad(outputs, inputs, grad_outputs)`** → Computes gradients manually for specific tensors.
7. **`optimizer.zero_grad()`** → Resets accumulated gradients before backpropagation.
8. **`create_graph=True`** → Enables higher-order derivatives (second-order gradients).
