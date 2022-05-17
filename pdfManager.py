def create_pdf_document(input_name: str, output_file: str):
    """
    Create the pdf document and save it to output_file
    """

    # Create an empty document
    pdf = Document()
    # Create an empty Page
    page = Page()
    # Add Page to document
    pdf.append_page(page)
    # Create a page layout
    layout: PageLayout = SingleColumnLayout(page)
    # Fill in the page layout
    create_page_layout(page, layout, name=input_name)

    with open(output_file, 'wb') as pdf_out:
        PDF.dumps(pdf_out, pdf)

    summary = {
        "Name": input_name, "Output File": output_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")


def create_page_layout(page, layout, name):
    """
    Create the page layout
    """
    path_to_images = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "static", "images")

    # Create a QR code for the course url
    course_qr_code: LayoutElement = Barcode(
        data=COURSE_URL, width=Decimal(64), height=Decimal(64), type=BarcodeType.QR,
    )

    company_logo = Image(
        PILImage.open(os.path.join(path_to_images, "company_logo.png")), width=Decimal(80), height=Decimal(32), horizontal_alignment=Alignment.RIGHT
    )

    course_title = Paragraph(
        "PDF Management in Python", font_color=HexColor("3342FF"), font_size=Decimal(18), font="Helvetica-Bold", padding_bottom=Decimal(5)
    )

    course_logo = Image(
        PILImage.open(os.path.join(path_to_images, "course_logo.png")), width=Decimal(150), height=Decimal(96), horizontal_alignment=Alignment.LEFT
    )
    # Add the header section
    layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=2, column_widths=[Decimal(0.15), Decimal(0.6), Decimal(0.25)],
                              ).no_borders()
        # Add First column
        .add(TableCell(course_title, col_span=2),).no_borders()
        .add(TableCell(company_logo, row_span=2),).no_borders()
        .add(TableCell(course_qr_code, padding_top=Decimal(15),),).no_borders()
        .add(course_logo, ).no_borders()
    )

    # Add the body section
    layout.add(
        Paragraph(
            f"Dear {name},", font_color=HexColor("000000"), font_size=Decimal(14), padding_top=Decimal(30)
        )
    )

    layout.add(
        Paragraph(
            """
            Provide user with hands-on experience on PDF 
            manipulation using Python programming language by integrating the most common 
            real-life scenarios into the course proceedings and providing you with 
            a framework of "how to do it".
            """, font_color=HexColor("000000"), font_size=Decimal(14), padding_top=Decimal(10)
        )
    )

    layout.add(
        Paragraph(
            """
            Broaden my knowledge 
            in the Python programming language and to gain in-depth experience in handling 
            and processing PDF files which constitue a large part of our day-to-day lives.
            """, font_color=HexColor("000000"), font_size=Decimal(14), padding_top=Decimal(10)
        )
    )

    # Add the trailer section
    author_logo = Image(
        PILImage.open(os.path.join(path_to_images, "author_logo.png")), width=Decimal(64), height=Decimal(64), horizontal_alignment=Alignment.LEFT
    )

    layout.add(
        FixedColumnWidthTable(number_of_columns=2, number_of_rows=1, column_widths=[Decimal(0.15), Decimal(0.85)], padding_top=Decimal(50)
                              ).no_borders()
        # Add First column
        .add(author_logo,).no_borders()
        .add(
            Paragraph(
                """
            Bassem Marji
            """, font="Helvetica-bold-oblique", font_color=HexColor("000000"), font_size=Decimal(12), padding_top=Decimal(15)
            ),
        ).no_borders()
    )

    # To simplify the navigation to destination link the QR code with the course URL
    page.append_remote_go_to_annotation(
        course_qr_code.get_bounding_box(), uri=COURSE_URL
    )
