"""
Weather Visualization Functions
===============================

Simple functions to display weather data in text format.
"""

def plot_temperature_trend(temperatures, title="Temperature Trend"):
    """
    Create a simple ASCII chart of temperature over time.
    
    Parameters
    ----------
    temperatures : list of float
        List of temperature values
    title : str, optional
        Title for the chart (default: "Temperature Trend")
        
    Returns
    -------
    str
        Formatted ASCII chart
        
    Examples
    --------
    >>> temps = [15, 17, 19, 21, 20, 18]
    >>> print(plot_temperature_trend(temps))
    """
    if not temperatures:
        return "No data to plot"
    
    # Find min and max for scaling
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    range_temp = max_temp - min_temp or 1  # Avoid division by zero
    
    # Create the chart
    chart = []
    chart.append(title)
    chart.append("-" * len(title))
    
    for i, temp in enumerate(temperatures):
        # Scale to 0-20 characters
        scaled = int((temp - min_temp) / range_temp * 20)
        bar = "█" * scaled + "░" * (20 - scaled)
        chart.append(f"{i:3d}: {bar} {temp:5.1f}°")
    
    return "\n".join(chart)


def print_weather_summary(location, temperature, conditions):
    """
    Print a nicely formatted weather summary.
    
    Parameters
    ----------
    location : str
        Name of the location
    temperature : float
        Current temperature in Celsius
    conditions : str
        Weather conditions description
        
    Returns
    -------
    str
        Formatted weather summary
        
    Examples
    --------
    >>> summary = print_weather_summary("London", 15.5, "Partly Cloudy")
    >>> print(summary)
    """
    # Determine weather emoji based on conditions
    conditions_lower = conditions.lower()
    if "sun" in conditions_lower or "clear" in conditions_lower:
        emoji = "☀️"
    elif "cloud" in conditions_lower:
        emoji = "☁️"
    elif "rain" in conditions_lower:
        emoji = "🌧️"
    elif "snow" in conditions_lower:
        emoji = "❄️"
    elif "storm" in conditions_lower or "thunder" in conditions_lower:
        emoji = "⛈️"
    else:
        emoji = "🌡️"
    
    # Create border
    border = "=" * (len(location) + 20)
    
    summary = []
    summary.append(border)
    summary.append(f"📍 {location} Weather")
    summary.append(border)
    summary.append(f"{emoji} {conditions}")
    summary.append(f"🌡️  {temperature}°C")
    summary.append(f"💧 Comfort: {'❄️ Cold' if temperature < 10 else '😊 Mild' if temperature < 25 else '🔥 Hot'}")
    summary.append(border)
    
    return "\n".join(summary)
