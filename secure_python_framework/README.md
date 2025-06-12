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
pip install secure_python_framework
```

## Usage
After installation, you can import the framework in your Python projects:

```python
from secure_python import secure_python

# Example of creating a random mapping
mapping = secure_python.crm()

# Encoding text
encoded_text = secure_python.et("Your sensitive data", mapping)

# Decoding text
decoded_text = secure_python.dt(encoded_text, mapping)
```

## Running Tests
To ensure everything is working correctly, you can run the unit tests provided in the `tests` directory:

```
python -m unittest discover -s tests
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.