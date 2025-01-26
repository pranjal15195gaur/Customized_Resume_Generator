<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume Generator</title>
</head>
<body>
    <h1>Resume Generator</h1>
    <p>
        A customizable Python-based <strong>Resume Generator</strong> that allows users to create professional PDF resumes with dynamic font size, font color, and background color options. 
        Built using the <strong>ReportLab</strong> library, this tool provides an elegant and simple way to showcase your skills, experience, and education in a visually appealing format.
    </p>

    <h2>Features</h2>
    <ul>
        <li>Generate PDF resumes with customizable:
            <ul>
                <li>Font size</li>
                <li>Font color (using Hex codes)</li>
                <li>Background color (using Hex codes)</li>
            </ul>
        </li>
        <li>Dynamic content for:
            <ul>
                <li><strong>Work Experience</strong></li>
                <li><strong>Education</strong></li>
                <li><strong>Additional Information</strong> (Languages, Technical Skills, Certifications, and Interests)</li>
            </ul>
        </li>
        <li>Clean and professional layout with table-based formatting for organized sections.</li>
        <li>Easy-to-use command-line interface (CLI).</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/yourusername/resume-generator.git
cd resume-generator
            </code></pre>
        </li>
        <li>Create a virtual environment and activate it:
            <pre><code>python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
            </code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <p>Run the script with customizable options for font size, font color, and background color:</p>
    <pre><code>python resume_generator.py --output &lt;output_file_name&gt; --font-size &lt;font_size&gt; --font-color &lt;font_color&gt; --background-color &lt;background_color&gt;
    </code></pre>

    <h3>Arguments</h3>
    <ul>
        <li><code>--output</code>: Name of the output PDF file (default: <code>customized_resume.pdf</code>).</li>
        <li><code>--font-size</code>: Font size for the resume text (default: <code>12</code>).</li>
        <li><code>--font-color</code>: Hex code for the font color (default: <code>#000000</code>).</li>
        <li><code>--background-color</code>: Hex code for the background color (default: <code>#FFFFFF</code>).</li>
    </ul>

    <h3>Example Command</h3>
    <pre><code>python resume_generator.py --output my_resume.pdf --font-size 14 --font-color #333333 --background-color #f5f5f5</code></pre>

    <h2>Project Structure</h2>
    <pre><code>resume-generator/
│
├── resume_generator.py       # Main script to generate the resume
├── README.md                 # Documentation

    </code></pre>

    <h2>Contributing</h2>
    <p>Contributions are welcome! If you'd like to improve the project, please follow these steps:</p>
    <ol>
        <li>Fork the repository.</li>
        <li>Create a new feature branch (<code>git checkout -b feature-name</code>).</li>
        <li>Commit your changes (<code>git commit -m "Add some feature"</code>).</li>
        <li>Push to the branch (<code>git push origin feature-name</code>).</li>
        <li>Open a pull request.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>

    <h2>Contact</h2>
    <p>If you have any questions or suggestions, feel free to reach out:</p>
    <ul>
        <li><strong>Name:</strong> Pranjal Gaur</li>
        <li><strong>Email:</strong> <a href="mailto:pranjal.gaur@iitgn.ac.in">pranjal.gaur@iitgn.ac.in</a></li>
    </ul>
</body>
</html>
