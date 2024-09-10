# Docker Weather Dashboard
The Docker Weather Dashboard is a web application designed to provide real-time weather information and forecasts for your location. The application is built using Docker to containerize the web server and is managed through Docker Compose.

# Current Features
1. Current Weather Display:
    - Current Conditions: Shows the current temperature, weather description, cloudiness, and rain probability.
    - Weather Icon: Displays an icon representing the current weather condition.
      
2. 24-Hour Hourly Forecast:
    - Temperature and Rain Probability: Provides a detailed hourly forecast for the next 24 hours.
    - Graphical Representation: The forecast data is displayed using a line chart created with Chart.js, including a vivid graphical representation of temperature and rain probability.
    - Data Labels: Values are shown at each data point on the chart for better readability.
   
3. Live Rain Radar:
    - Embedded Radar: Integrates an interactive rain radar from Windy.com to show live precipitation data for your location. The radar provides an up-to-date view of rain patterns in the area.

4. Automatic Data Updates:
    - Refresh Interval: The weather data is refreshed every 10 minutes to ensure up-to-date information.

5. Dynamic Content:
    - Website Title and Header: Both the website title and the main header (<h1>) text are set dynamically using environment variables, allowing easy customization without altering the code.

6. User Interface:
    - Modern Design: The dashboard features a sleek, modern design inspired by high-quality websites, ensuring a visually appealing and user-friendly experience.
    - Responsiveness: The design adapts to different screen sizes for optimal viewing on both desktop and mobile devices.
