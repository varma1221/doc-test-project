"""
Weather Calculation Functions
=============================

This module contains mathematical functions for weather conversions and calculations.
All functions include detailed docstrings for documentation practice.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    This is a basic temperature conversion function.
    
    Parameters
    ----------
    celsius : float
        Temperature in degrees Celsius
        
    Returns
    -------
    float
        Temperature in degrees Fahrenheit
        
    Examples
    --------
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters
    ----------
    fahrenheit : float
        Temperature in degrees Fahrenheit
        
    Returns
    -------
    float
        Temperature in degrees Celsius
        
    Examples
    --------
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(212)
    100.0
    """
    return (fahrenheit - 32) * 5/9


def calculate_dew_point(temperature, relative_humidity):
    """
    Calculate dew point temperature using the Magnus formula.
    
    The dew point is the temperature at which air becomes saturated
    with water vapor.
    
    Parameters
    ----------
    temperature : float
        Air temperature in degrees Celsius
    relative_humidity : float
        Relative humidity as a percentage (0-100)
        
    Returns
    -------
    float
        Dew point temperature in degrees Celsius
        
    Notes
    -----
    This uses the Magnus formula approximation:
    
    
    a = 17.27, b = 237.7°C for water
    """
    a = 17.27
    b = 237.7
    
    alpha = (a * temperature) / (b + temperature) + math.log(relative_humidity / 100.0)
    dew_point = (b * alpha) / (a - alpha)
    
    return round(dew_point, 2)


def heat_index(temperature, relative_humidity):
    """
    Calculate heat index (apparent temperature).
    
    The heat index combines air temperature and relative humidity
    to determine the human-perceived equivalent temperature.
    
    Parameters
    ----------
    temperature : float
        Air temperature in degrees Fahrenheit (must be above 70°F)
    relative_humidity : float
        Relative humidity as a percentage
        
    Returns
    -------
    float
        Heat index in degrees Fahrenheit
        
    Warnings
    --------
    This formula is valid only for temperatures above 70°F (21°C).
    For lower temperatures, the heat index is not defined.
    """
    # Simple approximation formula
    hi = -42.379 + 2.04901523 * temperature + 10.14333127 * relative_humidity
    hi = hi - 0.22475541 * temperature * relative_humidity
    hi = hi - 6.83783e-3 * temperature**2
    hi = hi - 5.481717e-2 * relative_humidity**2
    hi = hi + 1.22874e-3 * temperature**2 * relative_humidity
    hi = hi + 8.5282e-4 * temperature * relative_humidity**2
    hi = hi - 1.99e-6 * temperature**2 * relative_humidity**2
    
    return round(hi, 1)


def wind_chill(temperature, wind_speed):
    """
    Calculate wind chill temperature.
    
    Wind chill accounts for the cooling effect of wind on exposed skin.
    
    Parameters
    ----------
    temperature : float
        Air temperature in degrees Fahrenheit
    wind_speed : float
        Wind speed in miles per hour
        
    Returns
    -------
    float
        Wind chill temperature in degrees Fahrenheit
        
    Notes
    -----
    Wind chill is only defined for temperatures below 50°F (10°C)
    and wind speeds above 3 mph.
    """
    # Wind chill formula used by US weather service
    wc = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16
    wc = wc + 0.4275 * temperature * wind_speed**0.16
    
    return round(wc, 1)
