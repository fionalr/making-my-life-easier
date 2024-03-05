# NEF to JPEG Converter

This program is designed to convert Nikon Electronic Format (NEF) files to JPEG format. It was created out of the need for a reliable and free online converter for personal use. The script processes each NEF file found in a specified source directory and saves the converted JPEG images to a designated target directory.

## Features

- **Batch Conversion:** Converts all NEF files found in the specified source folder.
- **Automatic Directory Creation:** Creates the target directory for JPEG images if it does not already exist.
- **Verbose Output:** Provides detailed output for each converted file, including the source NEF and destination JPEG paths.

## Requirements

Before running this script, ensure you have installed the following Python packages:

- `rawpy`: Used for reading NEF files and processing images.
- `imageio`: Used for saving the processed images in JPEG format.

You can install these packages using pip:

```bash
pip install rawpy imageio
```

## Usage

1. **Modify the Script:** Before running the script, modify the `nef_folder` and `jpeg_folder` variables at the top of the script to specify the source and target directories, respectively.

    ```python
    nef_folder = 'path/to/your/nef/files'
    jpeg_folder = 'path/to/save/jpeg/images'
    ```

2. **Run the Script:** With Python installed on your system, navigate to the directory containing the script and run it using:

    ```bash
    python script_name.py
    ```

Replace `script_name.py` with the actual name of the script file.

## Example Output

After successfully converting a NEF file to JPEG, the script will print a message similar to:

```
Successfully converted example.nef to JPEG and saved to path/to/save/jpeg/images/example.jpg
```

## Note

This script is intended for personal use and was created as a free alternative to online converters. It handles basic conversion needs and might not cover all aspects of NEF processing available in professional software.
