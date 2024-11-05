# GFF to Excel Converter

A simple web application built with Flask that converts Genomic Feature Format (GFF) files to Excel (XLSX) files. This tool makes it easier to analyze and work with GFF data by transforming it into a user-friendly spreadsheet format.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [File Structure](#file-structure)
7. [Example](#example)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

GFF (Genomic Feature Format) files are widely used in bioinformatics to store genome annotations. This application allows bioinformaticians, genetic researchers, and data analysts to easily convert GFF files to Excel format, enabling easier access, analysis, and visualization of genomic data.

## Features

- **Easy Upload**: Upload GFF files directly through the web interface.
- **Automated Conversion**: Convert GFF data to Excel format with just one click.
- **Simplified Data Analysis**: Excel output makes it easier to filter, sort, and analyze genomic data.
- **User-Friendly Interface**: Simple and intuitive UI built with Bootstrap.

## Prerequisites

- **Python 3.7+**
- **Flask**: `pip install Flask`
- **Pandas**: `pip install pandas`
- **Openpyxl**: `pip install openpyxl` (for exporting data to Excel)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mannie-stien/gff-xlsx.git
   cd gff-xlsx

