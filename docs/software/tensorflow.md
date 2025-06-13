# TensorFlow

TensorFlow is a library for machine learning and artificial intelligence.

TensorFlow is available in multiple variants:

- [TensorFlow as a Python package for CPU](#tensorflow-as-a-python-package-for-cpu):
  works on [Bianca](../cluster_guides/bianca.md) and [Rackham](../cluster_guides/rackham.md)
- [TensorFlow as a Python package for GPU](#tensorflow-as-a-python-package-for-gpu)
  works on [Bianca](../cluster_guides/bianca.md) and [Snowy](../cluster_guides/snowy.md)

## TensorFlow as a Python package for CPU

It is part of the `python_ML_packages/[version]-cpu`
[modules](../cluster_guides/modules.md), where `[version]` is a version,
for example, `python_ML_packages/3.11.8-cpu`.

Only `3.9.5-cpu` and `3.9.5-gpu` are available on Bianca.

???- question "How to test TensorFlow as a Python package for CPU?"

    On Rackham, load the module to get access to the library:

    ```console
    module load python_ML_packages/3.11.8-cpu
    ```

    Start Python:

    ```console
    python
    ```

    In Python, type:

    ```python
    import tensorflow as tf
    print(tf.test.is_gpu_available())
    ```

    This should print:

    ```python
    False
    ```

    The output is correct: this is the CPU version.

## TensorFlow as a Python package for GPU

It is part of the `python_ML_packages/[version]-gpu`
[modules](../cluster_guides/modules.md), where `[version]` is a version,
for example, `python_ML_packages/3.9.5-gpu`

:warning: You can load this package on nodes without GPU but python will not find TensorFlow!

If you want to work interactively and test things, first allocate resources as seen below:

### On Snowy

```console
interactive -A <proj> -n 2 -M snowy --gres=gpu:1  -t 1:00:01
```

### On Bianca

```console
interactive -A <proj> -n 1 -C gpu --gres=gpu:1 -t 01:10:00
```

???- question "How to test TensorFlow as a Python package for GPU?"

    Load the module to get access to the library:

    ```bash
    module load python_ML_packages/3.9.5-gpu
    ```

    Start Python:

    ```console
    python
    ```

    In Python, type:

    ```python
    import tensorflow as tf
    print(tf.test.is_gpu_available())
    ```

    This should print something like:

    ```python
    2024-03-15 14:13:02.038401: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1525] Created device /device:GPU:0 with 13614 MB memory:  -> device: 0, name: Tesla T4, pci bus id: 0000:08:00.0, compute capability: 7.5
    True
    ```

    The output is correct: this is the GPU version.
