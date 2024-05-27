# Image Format Converter

This repository contains a Python script to convert images from one format to another. The script provides flexibility in specifying the input image format and the desired output format. It automatically detects the input image format based on file extensions and allows users to customize the conversion process.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Image Format Converter is a simple Python script designed to help users convert images from one format to another. It leverages the Pillow library to handle image processing tasks efficiently. With this tool, users can easily convert images to different formats without the need for complex image editing software.

## Features

- Convert images from one format to another.
- Automatically detect input image format based on file extensions.
- Customize conversion process by specifying input and output formats.
- Support for various image formats, including JPG, JPEG, AVIF, and more.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-format-converter.git
    cd image-format-converter
    ```

2. Install the required Python libraries:

    ```bash
    pip install pillow
    ```

## Usage

1. Set the `input_dir` and `output_dir` variables in the script to the paths of your input and output directories.

2. Update the `image_formats` dictionary to specify the input image formats and their corresponding slice lengths.

3. Run the script:

    ```bash
    python converter.py
    ```

4. The script will convert images from the specified input formats to the desired output format and save them in the output directory.

## Customization

- **Folder Variable**: Update the `folder` variable to match the name of the folder containing your images.

- **Input and Output Directories**: Set the `input_dir` and `output_dir` variables to the paths where your input images are located and where you want to save the converted images.

- **Image Formats and Slice Lengths**: Update the `image_formats` dictionary to specify the input image formats and their corresponding slice lengths.

- **Output Format**: Set the `output_format` variable to the desired output format.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a Pull Request.


---

Thank you for using the Image Format Converter! If you have any questions or suggestions, feel free to reach out.
