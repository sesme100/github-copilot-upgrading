# Upgraded Directory Structure

The `upgraded` directory contains the copied and upgraded content from the `legacy` directory. Below is the structure of the `upgraded` directory and a brief explanation of its contents:

## Directory Structure
```
upgraded/
├── MANIFEST.in
├── README.rst
├── distribute-0.6.10.tar.gz
├── distribute_setup.py
├── docs/
│   ├── Makefile
│   ├── build/
│   │   ├── doctrees/
│   │   └── html/
│   └── source/
├── guachi/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── tests/
│       ├── test_configmapper.py
│       ├── test_configurations.py
│       ├── test_database.py
│       └── test_integration.py
├── guachi.egg-info/
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
└── setup.py
```

## Explanation of Contents

### Root Files
- **`MANIFEST.in`**: Specifies additional files to include in the source distribution.
- **`README.rst`**: Provides a description of the project.
- **`distribute-0.6.10.tar.gz`**: Archive file for the `distribute` package.
- **`distribute_setup.py`**: Script to set up the `distribute` package.
- **`setup.py`**: Installation script for the project.

### `docs/`
- Contains documentation files for the project.
- **`Makefile`**: Used to build the documentation.
- **`build/`**: Contains generated documentation files.
- **`source/`**: Contains the source files for the documentation.

### `guachi/`
- Contains the main Python package for the project.
- **`__init__.py`**: Marks the directory as a Python package.
- **`config.py`**: Handles configuration logic.
- **`database.py`**: Manages database interactions.
- **`tests/`**: Contains unit tests for the `guachi` package.

### `guachi.egg-info/`
- Contains metadata about the `guachi` package.
- **`dependency_links.txt`**: Lists dependency links.
- **`PKG-INFO`**: Metadata about the package.
- **`SOURCES.txt`**: Lists source files included in the package.
- **`top_level.txt`**: Lists top-level modules in the package.