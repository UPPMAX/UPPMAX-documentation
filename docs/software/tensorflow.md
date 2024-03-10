# TensorFlow

TensorFlow is a library for machine learning and artificial intelligence.

TensorFlow is available in multiple variants:

- [TensorFlow as a Python package for CPU](#tensorflow-as-a-python-package-for-cpu):
  works on [Rackham](../cluster_guides/rackham.md)
- [TensorFlow as a Python package for GPU](#tensorflow-as-a-python-package-for-gpu)
  works on [Bianca](../cluster_guides/bianca.md) and [Snowy](../cluster_guides/snowy.md)

# TensorFlow as a Python package for CPU

TensorFlow as a Python package for CPU 
that works on [Rackham](../cluster_guides/rackham.md).

It is part of the `python_ML_packages/[version]-cpu` 
[modules](../cluster_guides/modules.md), where `[version]` is a version,
for example, `python_ML_packages/3.11.8-cpu`.

???- question "How to test TensorFlow as a Python package for CPU?"

    On Rackham, load the module to get access to the library:

    ```
    module load python_ML_packages/3.11.8-cpu
    ```

    Start Python:

    ```
    python
    ```

    In Python, type:

    ```
    import tensorflow as tf
    print(tf.test.is_gpu_available())
    ```

    This should print:

    ```
    False
    ```

    The output is correct: this is the CPU version.

# TensorFlow as a Python package for GPU

TensorFlow as a Python package for GPU 
that works on [Bianca](../cluster_guides/bianca.md) and [Snowy](../cluster_guides/snowy.md).

It is part of the `python_ML_packages/[version]-gpu` 
[modules](../cluster_guides/modules.md), where `[version]` is a version,
for example, `python_ML_packages/3.9.5-gpu`

Detailed documentation can be found [here](https://www.uppmax.uu.se/support/user-guides/tensorflow-user-guide/).
