### Hexlet tests and linter status:
[![Actions Status](https://github.com/Andradit/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Andradit/python-project-83/actions)
[![Maintainability](https://qlty.sh/badges/eabff0cc-8407-4563-8d9c-9d2c288735ed/maintainability.svg)](https://qlty.sh/gh/Andradit/projects/python-project-83)

# A site that analyses the specified pages for SEO suitability

Page Analyzer is a site that analyses specified pages for SEO suitability similar to PageSpeed Insights. Page Analyser is a full-fledged application based on the Flask framework.

## Installation

> ```diff
> + Please report issues if you try to install and run into problems!
> ```

Make sure you are running at least Python 3.12

Clone the repository and install manually:

```bash
$ git clone git@github.com:Andradit/python-project-83.git
$ cd python-project-83/
$ make install
$ make build
$ make package-install
```
## Starting program execution

To run the application in debug mode, enter this command
```bash
make dev
```
To run the application in production mode, enter this command
```bash
make start
```

## Possible Improvements

- Adding new columns with information on the results of site inspections
- Creating additional conditions for site inspections
- Adding new design themes
- *Your* creative idea.

If you encounter any problem or have any suggestions, please [open an issue](https://github.com/Andradit/python-project-83/issues/new) or [send a PR](https://github.com/Andradit/python-project-83/compare).