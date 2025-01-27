# Resume Generator

A customizable Python-based **Resume Generator** that allows users to create professional PDF resumes with dynamic font size, font color, and background color options. Built using the **ReportLab** library, this tool provides an elegant and simple way to showcase your skills, experience, and education in a visually appealing format.

## Features

- Generate PDF resumes with customizable:
    - Font size
    - Font color (using Hex codes)
    - Background color (using Hex codes)
- Dynamic content for:
    - **Work Experience**
    - **Education**
    - **Additional Information** (Languages, Technical Skills, Certifications, and Interests)
- Clean and professional layout with table-based formatting for organized sections.
- Easy-to-use command-line interface (CLI).

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/pranjal15195gaur/Customized_Resume_Generator.git
    cd resume-generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

## Usage

Run the script with customizable options for font size, font color, and background color:
```bash
python resume_generator.py --output <output_file_name> --font-size <font_size> --font-color <font_color> --background-color <background_color>
