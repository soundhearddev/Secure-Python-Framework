# Secure Python Framework

## Overview

The Secure Python Framework provides a set of tools for encoding and decoding text using a custom mapping system. It is designed to enhance the security of sensitive information by obfuscating it before storage or transmission.

## Features

- Encode and decode text using a custom mapping.
- Save and load mappings for reuse.
- Unit tests to ensure functionality.

## Installation

To install the Secure Python Framework, you can use pip. Run the following command in your terminal:

```
pip install .
```

## Usage

After installation, you can import the framework in your Python projects:

```python
import secure_python

# Example of creating a random mapping
mapping = secure_python.crm()

# Encoding text
encoded_text = secure_python.et("Your sensitive data", mapping)

# Decoding text
decoded_text = secure_python.dt(encoded_text, mapping)
```

## Running Tests

You need to have a Python file in the directory, written for the encode_test_use and decode_test_use functions. First, run the encoder and then run the decoder. The decoder uses exec to run the file. You can use it as shown in the example, but you can also use functions, classes, etc. It is necessary to have the .venv folder in the same directory as the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
