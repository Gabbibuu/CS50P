from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("times", "", 50)
        self.cell(0, 55, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    shirt(name)


def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_text_color(255,255,255) #White
    pdf.set_font("times", size=30)
    pdf.cell(0, 200, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()