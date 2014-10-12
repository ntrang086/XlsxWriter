###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2014, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):
        self.maxDiff = None

        filename = 'header_image04.xlsx'

        test_dir = 'xlsxwriter/test/comparison/'
        self.image_dir = test_dir + 'images/'
        self.got_filename = test_dir + '_test_' + filename
        self.exp_filename = test_dir + 'xlsx_files/' + filename

        self.ignore_files = []
        self.ignore_elements = {'xl/worksheets/sheet1.xml': ['<pageMargins', '<pageSetup']}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with image(s)."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.set_footer('&L&G&C&G&R&G', None,
                             {'image_left': self.image_dir + 'red.jpg',
                              'image_center': self.image_dir + 'blue.jpg',
                              'image_right': self.image_dir + 'yellow.jpg'})

        workbook.close()

        self.assertExcelEqual()

    def test_create_file_with_picture(self):
        """Test the creation of a simple XlsxWriter file with image(s)."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.set_footer('&L&[Picture]&C&G&R&[Picture]', None,
                             {'image_left': self.image_dir + 'red.jpg',
                              'image_center': self.image_dir + 'blue.jpg',
                              'image_right': self.image_dir + 'yellow.jpg'})

        workbook.close()

        self.assertExcelEqual()
