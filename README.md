# Overview
This project involves creating a Streamlit web application to predict satellite coordinates based on various orbital parameters. The prediction model uses Random Forest Regressors to estimate the satellite's position (x, y, z) for three different time intervals: 3 months, 6 months, and 1 year. The dataset used for training the model contains predictions for all these time intervals.

## Installation

### Prerequisites

Ensure you have Python installed (preferably version 3.6 or higher). The required Python libraries are:
- Streamlit
- Pandas
- NumPy
- Scikit-Learn

### Input Parameters
-Semi-Major Axis (AU): Semi-major axis of the orbit.
-Eccentricity: Measure of the orbit's deviation from circularity.
-Inclination (deg): Angle between the orbital plane and the reference plane.
-Argument of Perihelion (deg): Angle from the ascending node to the perihelion.
-Longitude of Ascending Node (deg): Angle from the reference direction to the ascending node.
-Mean Anomaly (deg): Fraction of the orbital period that has elapsed since the last periapsis.
-Perihelion Distance (AU): Closest point of the orbit to the sun.
-Aphelion Distance (AU): Farthest point of the orbit from the sun.
-Orbital Period (yr): Time taken for one complete orbit.

### Output
The app will display the predicted satellite coordinates for three future time intervals:

-Coordinates for 3rd Month: X, Y, Z
-Coordinates for 6th Month: X, Y, Z
-Coordinates for 1 Year: X, Y, Z
