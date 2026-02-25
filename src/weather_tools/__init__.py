"""
Weather Tools
=============

A collection of simple weather-related utilities for learning documentation.
"""

from .calculations import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    calculate_dew_point,
    heat_index,
    wind_chill
)

from .visualization import (
    plot_temperature_trend,
    print_weather_summary
)

__version__ = "0.1.0"
