import unittest
import re
import os


# handle relative import from parent directory
try:
    from gbget import get_accession
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from gbget import get_accession
    

ACCESSION_NUMBER = 'DQ336160.2'

def load_data(ext):
    filename = os.path.join(os.path.dirname(__file__), 'testdata', 'sequences.%s' % ext)
    handle = open(filename, 'r')
    data = handle.readlines()
    handle.close()
    # an extra line is added by reader: remove it
    return "".join(data[:-1])

class Test(unittest.TestCase):
    """Unit tests for get_accession"""
    
    def test_xml(self):
        a = get_accession(ACCESSION_NUMBER, 'nucleotide', 'xml')
        assert load_data('xml') == a
        
    def test_fasta(self):
        a = get_accession(ACCESSION_NUMBER, 'nucleotide', 'fasta')
        assert load_data('fasta') == a
        
    def test_gb(self):
        a = get_accession(ACCESSION_NUMBER, 'nucleotide', 'gb')
        assert load_data('gb') in a
    
    def test_native(self):
        a = get_accession(ACCESSION_NUMBER, 'nucleotide', 'native')
        assert load_data('xml') == a


if __name__ == "__main__":
    unittest.main()



