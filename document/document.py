"""@package asciidoc-dom
This module implements a way to generate asciidoc-documentation in your
python-code inspired by the XML Document Object Model (DOM)

"""

from enum import Enum


class Document:
    """The Document class is the top-level class having access to all objects
    within the document.

    """

    def __init__(self, title):
        """The constructor."""
        self.items = []
        self.document_header = ""
        self.title = title

    def addSection(self, title):
        """Add a Level 1 heading to the current document."""
        header = Header1(title)
        self.items.append(header)
        return header

    def getItems(self):
        """Returns a list of all level 1 headings in the current document."""
        return self.items

    # def __init__(self, text, paragraph_type=None, optional_title=None,
    def addParagraph(self, text, paragraph_type=None, optional_title=None):
        par = Paragraph("adsfasdf")
        par = Paragraph("adsfsa", optional_title="helo")

        par = Paragraph(text, optional_title=optional_title, paragraph_type=paragraph_type)
        self.items.append(par)

    def generateDocument(self, filename="out.adoc"):
        """Generate the asciidoc document and save it as filename."""
        output = "= " + self.title + "\n\n"
        for section in self.items:
            output += section.generateAsciidoc()

        with open(filename, "w") as f:
            f.write(output)
            f.close()


class Section:
    """ An abstract class inherited by all the headers."""
    section_id = 0

    def __init__(self, title):
        """The constructor."""
        self.items = []
        self.paragraphs = []
        self.title = title
        self.id = self.section_id
        self.section_id += 1

    def getSubsections(self):
        """Returns a list of header-objects all located within the current
        heading."""
        return self.sections

    def getParagraphs(self):
        """Returns a list of all paragraph-objects located within the current
        heading."""
        return self.elements

    def addParagraph(self, text, paragraph_type=None, optional_title=None,
                     code_language=None):
        """Adds a new paragraph to the current heading."""
        par = Paragraph(text, paragraph_type=paragraph_type,
                        optional_title=optional_title,
                        code_language=code_language)
        self.items.append(par)

    def getId():
        """Return the unique ID of the section."""
        return self.id

    def __recursiveGenerateAsciidoc(self):
        """Generate Asciidoc syntax for all subitems of a section."""
        output = ""
        for item in self.items:
            output += item.generateAsciidoc()

        return output


class Header1(Section):
    """Level 1 heading, corresponds to \"==\"."""

    def addSubsection(self, title):
        """Add a subsection to the current section."""
        header = Header2(title)
        self.items.append(header)
        return header

    def generateAsciidoc(self):
        """Generate Asciidoc syntax for current section and subsections"""
        output = "== " + self.title + "\n\n"
        output += self._Section__recursiveGenerateAsciidoc()
        return output


class Header2(Section):
    """Level 2 heading, corresponds to \"===\"."""

    def addSubsection(self, title):
        """Add a subsection to the current section."""
        header = Header3(title)
        self.items.append(header)
        return header

    def generateAsciidoc(self):
        """Generate Asciidoc syntax for current section and subsections"""
        output = "=== " + self.title + "\n\n"
        output += self._Section__recursiveGenerateAsciidoc()
        return output


class Header3(Section):
    """Level 3 heading, corresponds to \"====\"."""

    def addSubsection(self, title):
        """Add a subsection to the current section."""
        header = Header4(title)
        self.items.append(header)
        return header

    def generateAsciidoc(self):
        """Generate Asciidoc syntax for current section and subsections"""
        output = "==== " + self.title + "\n\n"
        output += self._Section__recursiveGenerateAsciidoc()
        return output


class Header4(Section):
    """Level 3 heading, corresponds to \"=====\"."""

    def generateAsciidoc(self):
        """Generate Asciidoc syntax for current section and subsections"""
        output = "===== " + self.title + "\n\n"
        output += self._Section__recursiveGenerateAsciidoc()
        return output


class Paragraph():
    """Paragraph object."""
    # Paragraph type enum
    NOTE = 1
    TIP = 2
    IMPORTANT = 3
    WARNING = 4
    CAUTION = 5
    CODE = 6

    def __init__(self, text, paragraph_type=None, optional_title=None, code_language=None):
        """The constructor."""
        self.optional_title = optional_title
        self.text = text
        self.paragraph_type = paragraph_type

    def generateAsciidoc(self):
        """Generate asciidoc syntax output for the class"""
        output = ""
        if self.optional_title:
            output += "." + self.optional_title + "\n\n"

        if self.paragraph_type == self.CODE and code_language:
            output += "[source," + code_language + "]\n"
        elif self.paragraph_type == self.NOTE:
            output += "NOTE: "
        elif self.paragraph_type == self.TIP:
            output += "TIP: "
        elif self.paragraph_type == self.IMPORTANT:
            output += "IMPORTANT: "
        elif self.paragraph_type == self.WARNING:
            output += "WARNING: "
        elif self.paragraph_type == self.CAUTION:
            output += "CAUTION: "

        output += self.text
        return output


class Block():
    pass


class List():
    pass


class Table():
    pass
