# Better Research Paper Deduplication

This repository contains a Python script for deduplicating research papers. It focuses on identifying duplicates by considering titles (with case normalization) and the presence of unique identifiers like ISSN and DOI when available.

## Overview

Deduplicating entries in bibliographic datasets is crucial for maintaining the quality of research metadata and ensuring accurate citation analysis. This script enhances the deduplication process by:
- Normalizing title case to ensure case insensitivity does not affect duplication detection.
- Excluding records with NaN values in critical fields ('ISSN' and 'DOI') from duplicate checks based on these identifiers.
- Combining robust duplicate detection strategies to provide a cleaner, more accurate dataset.

## Features

- **Title Case Normalization**: Converts all titles to lowercase to prevent duplicates due to case differences.
- **ISSN and DOI Deduplication**: Further filters duplicates based on 'ISSN' and 'DOI' fields, considering only entries where these fields are not null.
- **Data Integrity**: Ensures that entries without 'ISSN' or 'DOI' are still retained after cleaning.

## Data Source

The dataset used in this script is derived from exporting search results for research papers from academic databases. These exports typically include detailed bibliographic metadata which is essential for managing and analyzing scholarly publications. Users can export their search results from sites like Scopus, Web of Science, or Google Scholar, which provide comprehensive metadata for each entry.


## Requirements

To run the script, you need Python and pandas installed. You can install pandas with pip:

```bash
pip install pandas
```

## Usage

To use the script:
1. Place your dataset in the root directory of this project and name it `your_dataset.csv`.
2. Run the script using the command `python index.py`.
3. The script will produce `cleaned_dataset.csv` in the root directory, which will be your deduplicated dataset.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements or have identified bugs.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements

- This project was inspired by challenges encountered in handling academic datasets with varying standards of metadata completeness and accuracy.