import os
from src.keyword_extractor import extract_keywords_spacy, extract_keywords_nltk

def save_keywords_to_file(posts, output_file="extracted_keywords.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== Extracted Keywords Output ===\n\n")
        for idx, post in enumerate(posts, 1):
            spacy_kw = extract_keywords_spacy(post)
            nltk_kw = extract_keywords_nltk(post)
            
            f.write(f"--- Post {idx} ---\n")
            f.write(f"Text: {post}\n")
            f.write(f"spaCy Keywords: {spacy_kw}\n")
            f.write(f"NLTK Keywords:  {nltk_kw}\n\n")
    print(f"Success! Keywords saved to {output_file}")

def main():
    # Direct root folder wali post.txt file
    post_file = "post.txt"
    
    if not os.path.exists(post_file):
        print(f"Error: {post_file} file nahi mili root folder mein!")
        return

    with open(post_file, "r", encoding="utf-8") as f:
        posts = [line.strip() for line in f.readlines() if line.strip()]
    
    # Run and save to file
    save_keywords_to_file(posts)

if __name__ == "__main__":
    main()