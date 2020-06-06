import unittest
import sys

from context import document
from document import *


class TestSection1(unittest.TestCase):
    """Test level 1 heading (==)"""

    def setUp(self):
        self.document = document.Document()
        self.section1 = self.document.addSection("section 1")

    def testSectionHeader(self):
        self.assertEqual(self.section1.generateAsciidoc(), "== section 1\n\n")


class TestSubsection1(unittest.TestCase):
    """Test level 2 heading (===)"""

    def setUp(self):
        self.document = document.Document()
        self.section1 = self.document.addSection("section 1")
        self.subsection1 = self.section1.addSubsection("subsection 1")

    def testGenerateAsciidoc(self):
        assert_equal = (
"""== section 1

=== subsection 1

""")
        self.assertEqual(self.section1.generateAsciidoc(), assert_equal)

class TestSubSubsection1(unittest.TestCase):
    """Test level 3 heading (====)"""

    def setUp(self):
        self.document = document.Document()
        self.section1 = self.document.addSection("section 1")
        self.subsection1 = self.section1.addSubsection("subsection 1")
        self.subsubsection1 = self.subsection1.addSubsection("subsubsection 1")

    def testGenerateAsciidoc(self):
        assert_equal = (
"""== section 1

=== subsection 1

==== subsubsection 1

""")
        self.assertEqual(self.section1.generateAsciidoc(), assert_equal)


class TestSubSubSubsection1(unittest.TestCase):
    """Test level 4 heading (=====)"""

    def setUp(self):
        self.document = document.Document()
        self.section1 = self.document.addSection("section 1")
        self.subsection1 = self.section1.addSubsection("subsection 1")
        self.subsubsection1 = self.subsection1.addSubsection("subsubsection 1")
        self.subsubsubsection1 = self.subsubsection1.addSubsection("subsubsubsection 1")

    def testGenerateAsciidoc(self):
        assert_equal = (
"""== section 1

=== subsection 1

==== subsubsection 1

===== subsubsubsection 1

""")
        self.assertEqual(self.section1.generateAsciidoc(), assert_equal)

if __name__ == '__main__':
    unittest.main()
