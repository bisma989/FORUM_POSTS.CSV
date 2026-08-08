import os

def load_posts(file_path="data/posts.txt"):
    """Read lines from the text file to form the corpus database."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            posts = [line.strip() for line in f if line.strip()]
        if posts:
            return posts
            
    # Fallback default posts if file is empty or missing
    return [
        "The latest patch caused major bugs and crashed my game.",
        "How to optimize backend database queries in Flask.",
        "Server update deployment failed this morning.",
        "Troubleshooting performance drops after the recent software patch."
    ]