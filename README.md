# APOD Viewer

## Overview

The APOD Viewer is a web application that allows users to explore NASA's Astronomy Picture of the Day (APOD). Each day, NASA posts a different image or photograph of our universe, along with a brief explanation written by a professional astronomer. This project fetches and displays the APOD, making it easily accessible to everyone.

## Features

- **Daily Image**: Automatically fetches and displays the APOD for the current day.
- **Previous Images**: Users can navigate to and view previous APODs by selecting a date.
- **Detailed Information**: Displays a brief description along with each image, providing context and additional details.
- **Responsive Design**: The application is fully responsive and can be accessed on various devices.

## Deployment

The APOD Viewer is deployed on Streamlit and can be accessed via the following link:

👉 [Explore the APOD Viewer](https://hdbufkc6wfavwenykgaybg.streamlit.app/)

## Installation

If you want to run the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/apod-viewer.git
    cd apod-viewer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

4. **Access the application**:
    Open your web browser and go to `http://localhost:8501/`.

## Technologies Used

- **Python**: The core logic is written in Python.
- **Streamlit**: The web application framework used for building the UI.
- **NASA API**: Used to fetch the Astronomy Picture of the Day data.

## Contributing

Contributions are welcome! If you'd like to improve the project, feel free to submit a pull request or open an issue.

## Acknowledgments

- NASA for providing the Astronomy Picture of the Day API.
- The developers and contributors of Streamlit.
