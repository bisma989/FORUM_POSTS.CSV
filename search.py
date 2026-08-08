import os
import torch
import torch.nn.functional as F
from src.embedder import TextEmbedder
from src.utils import load_posts

class SemanticSearch:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.posts = load_posts()
        
        print("Computing corpus embeddings...")
        self.post_embeddings = torch.stack([self.embedder.get_embedding(post) for post in self.posts])

    def search(self, query, top_k=2):
        """Find the top-k most relevant posts for a given search query."""
        query_embedding = self.embedder.get_embedding(query)
        
        # Compute cosine similarities
        cos_scores = F.cosine_similarity(query_embedding.unsqueeze(0), self.post_embeddings)
        
        # Get top-k scores and indices
        top_results = torch.topk(cos_scores, k=min(top_k, len(self.posts)))
        
        results = []
        for score, idx in zip(top_results.values, top_results.indices):
            results.append({
                "post": self.posts[idx.item()],
                "score": score.item()
            })
            
        return results

if __name__ == "__main__":
    search_engine = SemanticSearch()
    query = "update broke game"
    
    matches = search_engine.search(query, top_k=2)
    
    # Output ko console par dikhana
    output_text = f"Query: '{query}'\n" + "-" * 40 + "\n"
    for match in matches:
        line = f"Score: {match['score']:.4f} | Post: {match['post']}\n"
        output_text += line
        print(line.strip())
        
    # Output folder ke andar file mein save karna
    os.makedirs("output", exist_ok=True)
    output_file_path = "output/search_results.txt"
    
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(output_text)
        
    print(f"\n[Success] Output successfully saved in '{output_file_path}'!")