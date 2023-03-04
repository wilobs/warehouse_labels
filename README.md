# Warehouse Label Printer

Simple implementation of [blabel](https://github.com/Edinburgh-Genome-Foundry/blabel) during the Warehouse creation. It also implements the massive generation of the Bin names.

## Description

This simple code is only intended to cover basic implementations for educational purposes. We can improve this approach by constructing a complex object into the QR Code, and your imagination rules.

### Features

- Build the Bin string names (AISLE_BAY_LEVEL_POSITION)
- Export to a text file with the Bin names.
- Export the Labels to a ready to print in a PDF file

## Getting started

### Prerequisites

Install 'blabel' package from

``` sh
pip install blabel

```

### Usage

In the code you can easily change the params for Bins to build

``` sh
python3 main.py

```

### Legal disclaimer

Usage of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

### Acknowledgements

Thanks to all who helped inspire this template.

### See also

- [Blabel](https://github.com/Edinburgh-Genome-Foundry/blabel)

### License

This project is licensed under the [MIT License](LICENSE.md).
