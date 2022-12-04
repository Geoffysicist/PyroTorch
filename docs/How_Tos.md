## Pip

### Upgrading pip
```
pip install --upgrade pip
```

### Installing a package ith pip
```
pip install package_name
```

## Dealing with virtual environments

### Create a virtual environment
```
python -m venv .venv
```

### Freeze a virtuak environment to a requirements.txt file
```
pip freeze > requirements.txt
```

### Load a virtual environment from a requirements.txt file
```
pip install -r requirements.txt
```

## Versions and Releases

### Versions
x.y.z

- x: major version when you make incompatible API change
- y: minor version when you add functionality in a backwards compatible manner
- z: patch version when you make backwards compatible bug fixes

for more details see [Semantic Versioning 2.0.0](https://semver.org/#semantic-versioning-200)

### Releases

[Managing releases in a repository](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository)
