# pip Commands Cheat Sheet (Python) — with comments

> Tip: Prefer `python -m pip ...` over plain `pip ...` so you always use the **pip for the Python interpreter** you intended.

---

## Check pip & get help

```bash
python -m pip --version        # Show pip version + which Python it's tied to
python -m pip -V               # Same as above (short form)
python -m pip help             # Show top-level help and common commands
python -m pip help <command>   # Show help for a specific command (e.g., install, list, freeze)
```

---

## Install packages

```bash
python -m pip install pkg                  # Install a package from PyPI
python -m pip install pkg==1.2.3           # Install an exact version
python -m pip install "pkg>=1.2,<2.0"      # Install a version range (constraints)
python -m pip install -U pkg               # Upgrade package to the newest compatible version
python -m pip install --upgrade-strategy eager pkg  # Also upgrade dependencies more aggressively
python -m pip install --pre pkg            # Allow pre-release versions (alpha/beta/rc)
python -m pip install --user pkg           # Install for current user only (no admin rights)
python -m pip install --no-cache-dir pkg   # Don’t use pip download cache (fresh download)
python -m pip install --force-reinstall pkg # Reinstall even if already installed
python -m pip install --no-deps pkg        # Install only the package, skip dependencies
python -m pip install -r requirements.txt  # Install from a requirements file
python -m pip install -r requirements.txt --upgrade  # Upgrade all packages from the file
python -m pip install -e .                 # Editable install for local project (dev mode)
python -m pip install .                    # Install local project (non-editable)
python -m pip install ./dist/pkg-1.0.0-py3-none-any.whl  # Install from a wheel file
python -m pip install git+https://github.com/user/repo.git # Install directly from a Git repo
python -m pip install "pkg[extra1,extra2]" # Install optional “extras” defined by the package
```

---

## Uninstall packages

```bash
python -m pip uninstall pkg   # Uninstall a package
python -m pip uninstall -y pkg # Uninstall without confirmation prompt
```

---

## List installed packages

```bash
python -m pip list                 # List installed packages and versions
python -m pip list --outdated      # Show packages with newer versions available
python -m pip list --uptodate      # Show packages that are up-to-date
python -m pip list --format=freeze # List in requirements.txt-like format
```

---

## Package details & dependency health

```bash
python -m pip show pkg     # Show package metadata (version, location, dependencies, etc.)
python -m pip show -f pkg  # Also show installed files for that package
python -m pip check        # Validate that installed packages have compatible dependencies
```

---

## Freeze / requirements.txt

```bash
python -m pip freeze                       # Output all installed packages pinned to versions
python -m pip freeze > requirements.txt    # Save a pinned list to requirements.txt
python -m pip freeze --exclude-editable    # Exclude editable installs (-e)
python -m pip freeze --local               # Show only local packages (omit global/site packages)
```

---

## Check available versions (replacement for deprecated `pip search`)

```bash
python -m pip index versions pkg      # Show available versions on the index (often PyPI)
python -m pip index versions pkg --pre # Include pre-releases
```

---

## Download / build wheels

```bash
python -m pip download pkg                # Download package archives without installing
python -m pip download -r requirements.txt # Download all packages listed in requirements file
python -m pip wheel pkg                   # Build a wheel for a package (if possible)
python -m pip wheel -r requirements.txt   # Build wheels for everything in requirements
python -m pip wheel --wheel-dir dist/ pkg # Put generated wheels into a folder (e.g., dist/)
```

---

## Cache management

```bash
python -m pip cache dir          # Show cache directory location
python -m pip cache info         # Show cache size/info
python -m pip cache list         # List cached files
python -m pip cache remove pkg   # Remove cached files matching a package name/pattern
python -m pip cache purge        # Clear the entire pip cache
```

---

## Config (global/user/site)

```bash
python -m pip config list              # List current pip configuration
python -m pip config debug             # Show how config is loaded + where from
python -m pip config get <key>         # Read a config key
python -m pip config set <key> <value> # Set a config key (e.g., index-url, trusted-host)
python -m pip config unset <key>       # Remove a config key
```

---

## Debug / troubleshooting

```bash
python -m pip debug           # Show environment info pip uses (paths, tags, etc.)
python -m pip debug --verbose # Same but with extra details
```

---

## Handy install flags

```bash
python -m pip install -q pkg                            # Quiet mode
python -m pip install -v pkg                            # Verbose mode (debugging install issues)
python -m pip install --proxy http://user:pass@host:port pkg  # Use a proxy
python -m pip install --trusted-host <host> pkg         # Trust a host (useful with internal indexes)
python -m pip install -i https://pypi.org/simple pkg    # Set primary index URL for this command
python -m pip install --extra-index-url https://... pkg # Add an extra index (keep PyPI too)
```

---

## Quick “daily-use” mini set

```bash
python -m pip install -U pip      # Upgrade pip itself
python -m pip install -r requirements.txt  # Install project dependencies
python -m pip list --outdated     # See what can be upgraded
python -m pip freeze > requirements.txt    # Export pinned deps
python -m pip uninstall pkg       # Remove a package
```
