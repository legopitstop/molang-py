# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 10/14/2026

### General

- Molang CLI now preserves context between inputs.
- MolangExpr is now hashable.
- Added support for string literals (Thanks to @sonu7089)
- Support for multiline Molang expressions, semicolon-separated statements, and braced blocks in conditional branches.

### New

- Added `parse_file` function
- Added `compile_file` function
- Added `eval_file` function

## [1.0.1] - 2/12/2026

### Fixes

- Package now includes `core` and `toolchain` submodules.

## [1.0.0] - 2/12/2026

### General

- Complete rewrite

## [0.0.3] - 11/25/2024

### General

- Molang now supports pydantic

## [0.0.2] - 1/18/2024

### General

- Removed ast from setup.py

## [0.0.1] - 1/18/2024

### General

- Initial release
