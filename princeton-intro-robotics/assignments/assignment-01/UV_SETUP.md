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
.venv/bin/python -m ipykernel install --sys-prefix \
  --name princeton-intro-robotics-assignment-1 \
  --display-name "Python (Princeton Robotics Assignment 1)"
```

The prepared environment keeps its kernel specification inside `.venv` with
`--sys-prefix`, so it remains self-contained. The `.venv/` directory is
excluded by the repository's root `.gitignore`.
