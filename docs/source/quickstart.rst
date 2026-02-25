Quickstart Guide
================

Get started with Weather Tools in minutes!

Basic Usage
-----------

.. code-block:: python

   from weather_tools import calculations

   # Convert Celsius to Fahrenheit
   f = calculations.celsius_to_fahrenheit(25)
   print(f"25°C = {f}°F")

   # Calculate dew point
   dew = calculations.calculate_dew_point(25, 60)
   print(f"Dew point: {dew}°C")

Weather Summary
---------------

.. code-block:: python

   from weather_tools import visualization

   summary = visualization.print_weather_summary(
       "New York", 22.5, "Sunny"
   )
   print(summary)

Temperature Trend
-----------------

.. code-block:: python

   temps = [15, 17, 19, 21, 20, 18]
   chart = visualization.plot_temperature_trend(temps)
   print(chart)
