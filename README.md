# Movie Recommendation System

This repository contains a simple Movie Recommendation System implemented using Flask and Surprise. The system allows users to rate movies and receive personalized recommendations based on their ratings.

## Project Structure

- `app.py`: The main Python application that sets up the Flask server and handles movie recommendations.
- `EDA.ipynb`: A Jupyter notebook containing exploratory data analysis (EDA) that details the approach to the task.
- `taskdetails.txt`: A text file detailing the task at hand.
- `data/`: A folder containing the datasets.
  - `filtered_ratings.csv`: A small sample from the actual dataset available at the [Kaggle Movie Recommendation System dataset](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system). This sample data can be used to get the best out of the system and reduce the mean squared error (MSE).
  - `movies.csv`: A CSV file containing movie titles and their corresponding IDs.
- `static/`: A folder containing static files.
  - `styles.css`: CSS file for styling the HTML page.
  - `wallpaper/`: A subfolder containing the wallpaper image used in the HTML page.
  - `movies.json`: A JSON file containing sample movie information for the drop-down menu in the HTML page.
- `templates/`: A folder containing HTML templates.
  - `index.html`: The main HTML page for the web application.

## Running the Application

To run the application, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required Python packages:
    ```bash
    pip install numpy pandas flask surprise
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Open your web browser and go to `http://localhost:5000`.

## Usage

- On the main page, select a movie from the drop-down menu and rate it.
- Click the "Submit Rating" button to add the movie to the list of rated movies.
- Click the "Get Recommendations" button to receive personalized movie recommendations based on your ratings.

## Conclusion

This project demonstrates a simple implementation of a movie recommendation system using collaborative filtering with Flask and Surprise. By following the instructions, you can set up and run the application locally and explore how movie recommendations are generated based on user ratings.
