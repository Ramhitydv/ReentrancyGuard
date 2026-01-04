# test_reentrancyguard.py
"""
Tests for ReentrancyGuard module.
"""

import unittest
from reentrancyguard import ReentrancyGuard

class TestReentrancyGuard(unittest.TestCase):
    """Test cases for ReentrancyGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReentrancyGuard()
        self.assertIsInstance(instance, ReentrancyGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReentrancyGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
