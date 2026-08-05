import unittest
from generate_stats import get_canonical_name

class TestMCECEngineLogic(unittest.TestCase):
    
    def test_version_and_date_stripping(self):
        # Test standard version numbers (e.g., Hobbes 3.0 -> Hobbes)
        self.assertEqual(get_canonical_name("Hobbes 3.0"), "Hobbes")
        
        # Test build/date numbers (e.g., Hobbes 260714 -> Hobbes)
        self.assertEqual(get_canonical_name("Hobbes 260714"), "Hobbes")
        
    def test_alias_dictionary(self):
        # Test custom typos or complete name shifts mapped in the dictionary
        self.assertEqual(get_canonical_name("Hobbes dev"), "Hobbes")
        self.assertEqual(get_canonical_name("hobess"), "Hobbes")
        
    def test_unaffected_engines(self):
        # Ensure clean names without versions stay intact
        self.assertEqual(get_canonical_name("Stockfish"), "Stockfish")

if __name__ == "__main__":
    unittest.main()
