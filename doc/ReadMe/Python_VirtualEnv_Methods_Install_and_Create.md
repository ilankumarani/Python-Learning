# Python Virtual Environment — Create Methods (Install + Create)

This README lists common ways to create a Python environment.  
For each method you get:

1) **Install the tool (if needed)**  
2) **Create the environment**  
3) **Activate / Deactivate**  

`<envName>` = your environment folder or env name.

---

## 0) Built-in `venv` (no install required)
**Install:** ✅ none (comes with Python)

**Create**
```bash
python -m venv <envName>
```

**Activate**
```bash
# macOS/Linux
source <envName>/bin/activate

# Windows PowerShell
<envName>\Scripts\Activate.ps1
```

**Deactivate**
```bash
deactivate
```

---

## 1) `virtualenv` (third-party venv tool)
**Install**
```bash
python -m pip install virtualenv
```

**Create**
```bash
virtualenv <envName>
```

**Activate**
```bash
# macOS/Linux
source <envName>/bin/activate

# Windows PowerShell
<envName>\Scripts\Activate.ps1
```

**Deactivate**
```bash
deactivate
```

---

## 2) `pipenv` (Pipfile workflow)
**Install**
```bash
python -m pip install pipenv
```

**Create (in your project folder)**
```bash
cd <projectFolder>
pipenv install
```

**Activate**
```bash
pipenv shell
```

**Run a command without activating**
```bash
pipenv run python -V
```

**Exit**
```bash
exit
```

---

## 3) `poetry` (pyproject + lockfile workflow)
**Install**
```bash
python -m pip install poetry
```

**Create (in your project folder)**
```bash
cd <projectFolder>
poetry init          # or: poetry new <projectName>
poetry install       # creates a venv and installs deps
```

**Activate**
```bash
poetry shell
```

**Run a command without activating**
```bash
poetry run python -V
```

**Exit**
```bash
exit
```

> Notes:
> - Poetry usually creates its own venv automatically.
> - Some setups create `.venv` inside the project; others store venvs centrally.

---

## 4) `pdm` (pyproject-first manager)
**Install**
```bash
python -m pip install pdm
```

**Create (venv)**
```bash
cd <projectFolder>
pdm init
pdm venv create <envName>
```

**Activate**
```bash
pdm venv activate <envName>
```

**Run without activating**
```bash
pdm run python -V
```

---

## 5) `conda` (popular in Data/ML)
**Install**
- Install **Miniconda** or **Anaconda** (once, system-level)

**Create**
```bash
conda create -n <envName> python=3.11
```

**Activate**
```bash
conda activate <envName>
```

**Deactivate**
```bash
conda deactivate
```

---

## 6) `mamba` (faster conda alternative)
**Install**
- Install **mambaforge** or install `mamba` into base conda

**Create**
```bash
mamba create -n <envName> python=3.11
```

**Activate**
```bash
conda activate <envName>
```

**Deactivate**
```bash
conda deactivate
```

---

## 7) `pyenv` + `pyenv-virtualenv` (manage multiple Python versions)
**Install**
- macOS (Homebrew):
```bash
brew install pyenv pyenv-virtualenv
```

**Create**
```bash
pyenv install 3.11.4
pyenv virtualenv 3.11.4 <envName>
```

**Activate**
```bash
pyenv activate <envName>
```

**Deactivate**
```bash
pyenv deactivate
```

---

## 8) `uv` (fast modern tool; can create and sync venvs)
**Install**
```bash
python -m pip install uv
```

**Create**
```bash
uv venv <envName>
```

**Activate**
```bash
# macOS/Linux
source <envName>/bin/activate

# Windows PowerShell
<envName>\Scripts\Activate.ps1
```

**Deactivate**
```bash
deactivate
```

---

# Quick recommendation (for most backend projects)
Use:
- **`venv`** if you want simplest standard approach, or
- **`poetry`** if you want lockfiles + dependency management like Maven.

---

# `.gitignore` (ignore environments)
Add:
```gitignore
<envName>/
.venv/
```
Common extras:
```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.env
dist/
build/
*.egg-info/
```
