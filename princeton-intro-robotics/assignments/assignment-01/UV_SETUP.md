# Assignment 1: local `uv` environment

This directory includes a local Python environment for running `Lab1.ipynb`.
The environment is intentionally ignored by Git; recreate it with the commands
below if needed.

## Use the prepared environment

From the repository root:

```bash
source princeton-intro-robotics/assignments/assignment-01/.venv/bin/activate
jupyter lab princeton-intro-robotics/assignments/assignment-01/Lab1.ipynb
```

In Jupyter, choose the kernel named **Python (Princeton Robotics Assignment 1)**.

## Use it in VS Code

Install the Microsoft **Python** and **Jupyter** extensions if they are not
already installed. In VS Code:

1. Open this repository (or the `assignment-01` folder).
2. Run **Python: Select Interpreter** and choose
   `assignments/assignment-01/.venv/bin/python`.
3. Open `Lab1.ipynb`, click the kernel picker in the upper-right, and choose
   **Python (Princeton Robotics Assignment 1)**.

The kernelspec is installed in your user Jupyter directory and points at the
project-local interpreter, matching the setup used by the `diffusion` project.

The environment uses Python 3.11 and current compatible wheels for the packages
listed in the public course environment (`numpy`, `scipy`, `sympy`, `matplotlib`,
`notebook`, `jupyterlab`, `ipykernel`, `opencv-python`, `ipywidgets`, and
`ipympl`). The public Conda file requests Python 3.9 and an old SciPy release;
Python 3.11 avoids compiling obsolete packages on current Apple Silicon while
preserving the APIs used by the starter notebook.

## Recreate it

Install [`uv`](https://docs.astral.sh/uv/) first, then run:

```bash
cd princeton-intro-robotics/assignments/assignment-01
uv venv .venv --python 3.11
uv pip install --python .venv/bin/python \
  numpy scipy sympy matplotlib notebook jupyterlab ipykernel \
  opencv-python ipywidgets ipympl
.venv/bin/python -m ipykernel install --user \
  --name princeton-intro-robotics-assignment-1 \
  --display-name "Python (Princeton Robotics Assignment 1)"
```

The kernelspec contains the absolute path to this checkout's `.venv`. If the
repository is moved or the venv is recreated at a different path, rerun the
last command. The `.venv/` directory itself is excluded by the repository's
root `.gitignore`.
