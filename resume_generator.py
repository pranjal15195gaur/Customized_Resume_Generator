import argparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_resume(output_file, font_size, font_color, background_color):
    # Set up the document
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Customize font size and color
    custom_style = ParagraphStyle(
        name="CustomStyle",
        fontSize=font_size,
        textColor=colors.HexColor(font_color),
        fontName="Helvetica",
    )
    header_style = ParagraphStyle(
        name="HeaderStyle",
        fontSize=font_size + 2,
        textColor=colors.HexColor(font_color),
        fontName="Helvetica",
    )


    header_style1 = ParagraphStyle(
        name="HeaderStyle1",
        fontSize=font_size + 6,
        textColor=colors.HexColor(font_color),
        fontName="Helvetica-Bold",
    )

    header_style2 = ParagraphStyle(
        name="HeaderStyle1",
        fontSize=font_size + 4,
        textColor=colors.HexColor(font_color),
        fontName="Helvetica-Bold",
    )

    # Background color setup
    def add_background(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(background_color))
        canvas.rect(0, 0, doc.pagesize[0], doc.pagesize[1], fill=True, stroke=False)
        canvas.restoreState()

    # Name and Contact Information
    name = Paragraph("<u>PRANJAL GAUR</u>", header_style1)
    elements.append(name)
    elements.append(Spacer(1, 10))

    contact_info1 = Paragraph(
        "Address - Parsa Shahalam, Siddharth Nagar, UP, India ",custom_style,
    )
    contact_info2 = Paragraph(
        "Mobile No - 8887853269 ",custom_style,
    )

    contact_info3 = Paragraph(
        "Email ID - pranjal.gaur@iitgn.ac.in ",custom_style,
    )

    elements.append(contact_info1)
    elements.append(contact_info2)
    elements.append(contact_info3)
    elements.append(Spacer(1, 15))


    # Education Section
    elements.append(Paragraph("<u>EDUCATION</u>", header_style2))
    elements.append(Spacer(1, 10))
    p1 = Paragraph("<b> Bachelors of Technology, Computer Science and Engineering</b> ", header_style)
    elements.append(p1)
    elements.append(Spacer(1, 2))
    dp1 = Paragraph("Oct 2022 - Present", custom_style)
    elements.append(dp1)
    elements.append(Spacer(1, 5))
    p2 = Paragraph(
                """• IIT Gandhinagar<br/>
                   • Relevant Courses: Artificial Intelligence, Machine Learning, Data Structures.""",
                custom_style,
            )
    elements.append(p2)
    elements.append(Spacer(1, 10))


    p4 = Paragraph("<b>Class 12th</b> ", header_style)
    elements.append(p4)
    elements.append(Spacer(1, 2))
    dp4 = Paragraph("Jul 2020 - Apr 2022", custom_style)
    elements.append(dp4)
    elements.append(Spacer(1, 5))
    p5 = Paragraph(
                """ • Siddharth Public School<br/>
                    • Achieved 98% in 12th board examination.<br/>
                    • Secured All India Rank 150 in competitive exams.""",
                custom_style,
            )
    elements.append(p5)
    elements.append(Spacer(1, 20))



    # Work Experience Section
    elements.append(Paragraph("<u>WORK EXPERIENCE</u>", header_style2))
    elements.append(Spacer(1, 10))


    h1 = Paragraph("<b>Engineering Executive, Borelle Technologies</b> ", header_style)
    elements.append(h1)
    elements.append(Spacer(1, 2))
    d1 = Paragraph("Jan 2023 - Feb 2024", custom_style)
    elements.append(d1)

    elements.append(Spacer(1, 4))
    s1 = Paragraph(
                """• Implemented cost-effective solutions, resulting in a 20% reduction in expenses.<br/>
                   • Streamlined project workflows, enhancing overall efficiency by 25%.<br/>
                   • Led a team in successfully delivering a complex engineering project on time and within allocated budget.""",
                custom_style,
            )
    
    elements.append(s1)
    
    elements.append(Spacer(1, 10))

    h2 = Paragraph("<b>Project Engineer, Salford & Co</b> ", header_style)
    elements.append(h2)
    elements.append(Spacer(1, 2))
    d2 = Paragraph("Mar 2021 - Dec 2022", custom_style)
    elements.append(d2)

    elements.append(Spacer(1, 4))
    s2 = Paragraph(
                """• Managed project timelines, reducing delivery times by 30%.<br/>
                   • Spearheaded the adoption of cutting-edge engineering software, improving project accuracy by 15%.<br/>
                   • Collaborated with cross-functional teams, enhancing project success rates by 10%.""",
                custom_style,
            )
    
    elements.append(s2)

    elements.append(Spacer(1, 10))


    # Additional Information Section
    elements.append(Paragraph("<u>ADDITIONAL INFORMATION</u>", header_style2))
    elements.append(Spacer(1, 10))

    g1 = Paragraph("<b>Languages Known : </b> ", header_style)
    elements.append(g1)
    elements.append(Spacer(1, 5))
    dg1 = Paragraph("English (Fluent), Hindi (Native), French (Basic)", custom_style)
    elements.append(dg1)
    elements.append(Spacer(1, 5))
    
    g2 = Paragraph("<b>Technical Skills : </b> ", header_style)
    elements.append(g2)
    elements.append(Spacer(1, 5))
    dg2 = Paragraph("Python, SQL, C++, React, Tableau, Power BI, Flask, Django", custom_style)
    elements.append(dg2)
    elements.append(Spacer(1, 5))

    g3 = Paragraph("<b>Certifications : </b> ", header_style)
    elements.append(g3)
    elements.append(Spacer(1, 5))
    dg3 = Paragraph("AWS Cloud Practitioner, Tableau Certified Associate", custom_style)
    elements.append(dg3)

    elements.append(Spacer(1, 5))

    g4 = Paragraph("<b>Interests : </b> ", header_style)
    elements.append(g4)
    elements.append(Spacer(1, 5))
    dg4 = Paragraph("Fintech Innovation, Machine Learning, Blockchain, Photography", custom_style)
    elements.append(dg4)
    elements.append(Spacer(1, 20))

    # Build the PDF with the background color
    doc.build(elements, onFirstPage=add_background, onLaterPages=add_background)
    print(f"Resume saved as {output_file}")


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a customizable resume.")
    parser.add_argument("--output", type=str, default="customized_resume4.pdf", help="Output file name (default: customized_resume.pdf)")
    parser.add_argument("--font-size", type=int, default=12, help="Font size (default: 12)")
    parser.add_argument("--font-color", type=str, default="#000000", help="Font color in hex code (default: #000000)")
    parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Background color in hex code (default: #FFFFFF)")

    # Parse arguments
    args = parser.parse_args()

    # Generate the resume with provided customization options
    generate_resume(args.output, args.font_size, args.font_color, args.background_color)
