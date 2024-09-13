# Docker Weather Dashboard
The Docker Weather Dashboard is a web application designed to provide real-time weather information and forecasts for your location. The application is built using Docker to containerize the web server and is managed through Docker Compose.

# Current Features
1. Current Weather Display:
    - Current Conditions: Shows the current temperature, weather description, cloudiness, and rain probability.
    - Weather Icon: Displays an icon representing the current weather condition.
      
2. 48-Hour Hourly Forecast:
    - Temperature and Rain Probability: Provides forecast for the next 24 hours in three hour intervals.
    - Graphical Representation: The forecast data is displayed using a line chart created with Chart.js, including a vivid graphical representation of temperature and rain probability.
    - NOTE: I'm using OpenWeatherAPI to get weather data. Due to API limitations, the forecast currently provides just 3-hour intervals. However there is a paid version which can provide an hourly forecast.
   
3. Live Rain Radar:
    - Embedded Radar: Integrates an interactive rain radar from Windy.com to show live precipitation data for your location. The radar provides an up-to-date view of rain patterns in the area.

4. Dynamic Content:
    - Website Title and Header: Both the website title and the main header text are set dynamically using environment variables, allowing easy customization without altering the code.

5. User Interface:
    - Design: The dashboard features a sleek design ensuring a visually appealing and user-friendly experience.
    - NOTE: The frontend is still under construcation and will be updatet in the future.
    - Responsiveness: The design adapts to different screen sizes for optimal viewing on both desktop and mobile devices.
  
# Technical Details
    - Backend: The application is built using Flask, a lightweight web framework in Python, to fetch and process weather data from the OpenWeatherMap API.
    - Frontend: The user interface is developed using HTML, CSS, and JavaScript, with Chart.js for data visualization.
    - Containerization: Docker is used to containerize the application, and Docker Compose manages the deployment and configuration of the Docker container.

# Deployment
The project is set up using Docker Compose, which simplifies the deployment process by managing environment variables and container configurations. The application runs in a Docker container, exposing     the weather dashboard on port 5000. (I don't recommend exposing the container to the internet and, if needed, run it behind a reverse proxy)
To custimize the website's title and header, simply edit the corresponding environment variable.
If you decide to host the service publicaly, make sure to account for your local data privacy law (e.g. cookie banners).

The Dashboard uses OpenWeatherAPI to collect its data. Therefore, you need an API KEY from OpenWeather (you need to create a free account).
To specify the location, put in the CITY ID of the desired location in the docker compose file.

Copy the required files into your local directory using wget.
After that, use docker compose up -d.
