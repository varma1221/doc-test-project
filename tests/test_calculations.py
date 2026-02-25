"""
Simple tests for calculation functions.
"""

import math
from src.weather_tools import calculations

def test_celsius_to_fahrenheit():
    """Test Celsius to Fahrenheit conversion."""
    assert calculations.celsius_to_fahrenheit(0) == 32.0
    assert calculations.celsius_to_fahrenheit(100) == 212.0
    assert calculations.celsius_to_fahrenheit(-40) == -40.0
    print("✓ Celsius to Fahrenheit tests passed")

def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    assert calculations.fahrenheit_to_celsius(32) == 0.0
    assert calculations.fahrenheit_to_celsius(212) == 100.0
    assert calculations.fahrenheit_to_celsius(-40) == -40.0
    print("✓ Fahrenheit to Celsius tests passed")

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
