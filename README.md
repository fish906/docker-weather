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
    - NOTE: I'm using OpenWeatherAPI to get weather data. Due to API limitations, the forecast currently provides just 3-hour intervals.
   
3. Live Rain Radar:
    - Embedded Radar: Integrates an interactive rain radar from Windy.com to show live precipitation data for your location. The radar provides an up-to-date view of rain patterns in the area.

4. Automatic Data Updates:
    - Refresh Interval: The weather data is refreshed every 10 minutes to ensure up-to-date information.
    - NOTE: The free version of the OpenWeatherAPI only allows for 1000 calls per day (that's still one call per 1.5 minutes).

5. Dynamic Content:
    - Website Title and Header: Both the website title and the main header text are set dynamically using environment variables, allowing easy customization without altering the code.

6. User Interface:
    - Design: The dashboard features a sleek design ensuring a visually appealing and user-friendly experience.
    - NOTE: The frontend is still under construcation and will be updatet in the future.
    - Responsiveness: The design adapts to different screen sizes for optimal viewing on both desktop and mobile devices.
  
# Technical Details
    - Backend: The application is built using Flask, a lightweight web framework in Python, to fetch and process weather data from the OpenWeatherMap API.
    - Frontend: The user interface is developed using HTML, CSS, and JavaScript, with Chart.js for data visualization.
    - Containerization: Docker is used to containerize the application, and Docker Compose manages the deployment and configuration of the Docker container.

# Deployment
The project is set up using Docker Compose, which simplifies the deployment process by managing environment variables and container configurations. The application runs in a Docker container, exposing     the weather dashboard on port 5000. (I recommend note exposing the container to the internet and instead run it behind a reverse proxy)
To custimze the website's title and header, simply edit the corresponding environment variable.

The Dashboard uses OpenWeatherAPI to collect it's data. Therefore you need an API KEY from OpenWeather (you need to create a free account).
To specify the location put in the CITY ID of the desired location.
