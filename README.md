# corpus-callosum

Convenient access point for internal Callosum developer tooling.

## Installation

```bash
pip install corpus-callosum
```

For development (editable install):

```bash
pip install -e ".[dev]"
```

## Usage

```bash
callosum --help
callosum --version
```

## Development

This project uses [Hatch](https://hatch.pypa.io/) for environment and build management.

```bash
pip install hatch

# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Build the package
hatch build
```

## Project structure

```
corpus-callosum/
├── src/
│   └── corpus_callosum/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_cli.py
├── pyproject.toml
├── LICENSE
└── README.md
```

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
