---
tags:
  - Python
  - plotting
  - Matplotlib
---


# Matplotlib

Matplotlib ([Matplotlib homepage](https://matplotlib.org))
is a Python 2D plotting library,
which produces publication-quality
figures in a variety of hardcopy formats and
interactive environments across platforms.

Matplotlib can be used in Python scripts, the Python and IPython shell,
web application servers, and six graphical user interface toolkits.

### Loading the Matplotlib module

Here is how to load the default Matplotlib module:

```bash
module load matplotlib
```

### Example

Here is the minimal Python code to create a Matplotlib plot:

```python
import matplotlib.pyplot as plt

plt.plot([0, 1, 4, 9, 16])
plt.savefig('my_plot.png')
```

### Matplotlib main package(s)"

- `contourpy`
- `Cycler`
- `fonttools`
- `kiwisolver`
- `matplotlib`

!!! tip "Load this version and get many other bundles on the fly!"

    Included are

    - Python-bundle-PyPI
    - SciPy-bundle

### Matplotlib installed versions

These are the Matplotlib installed versions and their dependencies.

#### Matplotlib 3.9.2-gfbf-2024a

Packages:

- `contourpy-1.3.0`
- `Cycler-0.12.1`
- `fonttools-4.53.1`
- `kiwisolver-1.4.5`
- `matplotlib-3.9.2`

Dependencies:

- `Python/3.12.3-GCCcore-13.3.0`
- `Python-bundle-PyPI/2024.06-GCCcore-13.3.0`
- `SciPy-bundle/2024.05-gfbf-2024a`

#### Matplotlib 3.10.5-gfbf-2025b

Packages:

- `contourpy-1.3.3`
- `cycler-0.12.1`
- `fonttools-4.58.5`
- `kiwisolver-1.4.8`
- `matplotlib-3.10.5`

Dependencies:

- `Python/3.13.5-GCCcore-14.3.0`
- `Python-bundle-PyPI/2025.07-GCCcore-14.3.0`
- `SciPy-bundle/2025.07-gfbf-2025b`
