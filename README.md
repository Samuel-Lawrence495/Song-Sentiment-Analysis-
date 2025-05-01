# Good Kid Song Lyric Analysis: Clustering and Sentiment

## Overview

This project explores the lyrical themes present in the songs of the artist Good Kid. It uses Natural Language Processing (NLP) techniques to:

1.  **Extract Lyrics:** Automatically gather song lyrics using web scraping.
2.  **Analyze Sentiment:** Calculate sentiment polarity scores for each song using TextBlob.
3.  **Understand Meaning:** Generate semantic vector embeddings for lyrics using Sentence-BERT, capturing deeper meaning beyond keywords.
4.  **Identify Themes:** Apply clustering algorithms (like K-Means) to group songs based on their semantic similarity.
5.  **Visualize & Interpret:** Visualize the song clusters and analyze how the identified lyrical themes correlate with the calculated sentiment scores.

The goal is to uncover patterns in Good Kid's songwriting and investigate the relationship between lyrical content and emotional tone as determined by standard sentiment analysis tools.

## Features

*   **Data Acquisition:** Reads lyrics from local `.txt` files created from web scraping.
*   **Sentiment Analysis:** Calculates polarity scores using `TextBlob` and classifies songs as positive, negative, or neutral.
*   **Semantic Embedding:** Uses the Sentence-BERT model to convert lyrics into meaningful vector representations.
*   **Clustering:** Implements K-Means clustering to group songs based on lyrical similarity. Includes:
    *   Elbow method visualization to help determine the optimal number of clusters (`k`).
    *   Uses the elbow method to determine the optimal value of `K`.
*   **Visualization:** Generates 2D visualizations of song embeddings using PCA, colored by cluster assignment and by sentiment classification.
*   **Analysis:** Provides summaries of sentiment distribution within each identified cluster.

## Technologies Used

*   Python 3.x
*   Pandas: Data manipulation and analysis.
*   TextBlob: Sentiment analysis.
*   Sentence-Transformers: Generating sentence/text embeddings.
*   Scikit-learn: K-Means clustering, PCA, Silhouette score calculation.
*   Matplotlib: Data visualization (plots).
*   NumPy: Numerical operations.
*   (Optional: Add `requests`, `beautifulsoup4` if web scraping is implemented)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Samuel-Lawrence495/Song-Sentiment-Analysis-.git
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Prepare Data:**
    *   Place the `.txt` files containing the lyrics for each Good Kid song into a designated folder (e.g., `data/lyrics/`).
    *   Update the `folder_path` variable in the main script (`SongSA.ipynb`) to point to this folder.

## Usage

1.  **Configure:** Ensure the `folder_path` in the script points to your lyrics directory.
2.  **Run the main analysis notebook:**
3.  **Interpret Output:**
    *   The script will print progress updates, sentiment analysis results, and cluster analysis summaries.
    *   Plots will be displayed interactively.
    *   You will be prompted to enter the desired number of clusters (`k`) after viewing the Elbow plot.
