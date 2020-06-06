"""@package asciidoc-dom
This module implements a way to generate asciidoc-documentation in your
python-code inspired by the XML Document Object Model (DOM)

"""

from enum import Enum


class Document:
    """The Document class is the top-level class having access to all objects
    within the document.

    """

    def __init__(self):
        """The constructor."""
        self.sections = []
        self.document_header = ""

    def addSection(self):
        """Add a Level 1 heading to the current document."""
        header = Header1()
        self.sections.append(header)
        return header

    def getSections(self):
        """Returns a list of all level 1 headings in the current document."""
        return self.sections

    def generateDocument(self, filename):
        """Generate the asciidoc document and save it as filename."""
        pass


class section:
    """ An abstract class inherited by all the headers"""
    id = 0

    def __init__(self):
        """The constructor."""
        self.items = []
        self.paragraphs = []
        self.id = id
        id += 1

    def getSubsections(self):
        """Returns a list of header-objects all located within the current
        heading"""
        return self.sections

    def getParagraphs(self):
        """Returns a list of all paragraph-objects located within the current
        heading"""
        return self.elements

    def addParagraph(self, paragraph_type, text):
        """Adds a new paragraph to the current heading"""
        return Paragraph(paragraph_type, text)

    def getId():
        """Return the unique ID of the section"""
        return self.id

    def generateAsciidoc():
        pass


class Header1(section):
    """Level 1 heading, corresponds to \"==\"."""

    def addSubsection():
        """Add a subsection to the current section."""
        header = Header2()
        self.sections.append(header)
        return header


class Header2(section):
    """Level 2 heading, corresponds to \"===\"."""

    def addSubsection():
        """Add a subsection to the current section."""
        header = Header3()
        self.sections.append(header)
        return header


class Header3(section):
    """Level 3 heading, corresponds to \"====\"."""

    def addSubsection():
        """Add a subsection to the current section."""
        header = Header4()
        self.sections.append(header)
        return header


class Header4(section):
    """Level 3 heading, corresponds to \"=====\"."""
    pass


class Paragraph(Enum):
    """Paragraph object."""

    # Paragraph type enum
    NOTE = 1
    TIP = 2
    IMPORTANT = 3
    WARNING = 4
    CAUTION = 5
    CODE = 6

    def __init__(self, text, paragraph_type=None, optional_title=None,
                 code_language=None):

        """The constructor."""
        self.optional_title = optional_title
        self.text = text
        self.type = type

    def generateAsciidoc(self):
        """Generate asciidoc syntax output for the class"""
        output = ""
        if optional_title:
            output += "." + optional_title + "\n\n"

        if paragraph_type == self.CODE and code_language:
            output += "[source," + code_language + "]\n"
        elif paragraph_type == self.NOTE:
            output += "NOTE: "
        elif paragraph_type == self.TIP:
            output += "TIP: "
        elif paragraph_type == self.IMPORTANT:
            output += "IMPORTANT: "
        elif paragraph_type == self.WARNING:
            output += "WARNING: "
        elif paragraph_type == self.CAUTION:
            output += "CAUTION: "

        output += text
