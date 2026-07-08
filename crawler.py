import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


def start_crawling(start_url):
    current_url = start_url
    all_posts = []
    seen_titles = set()  
    page_number = 1

    while current_url:
        print(f" Hum Page number {page_number} ko read kar rahe hain...")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(current_url, headers=headers)

        if response.status_code != 200:
            print(" Oh ho! Page nahi khul raha.")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # 2. Quotes/Posts dhoondo
        posts_on_page = soup.find_all("div", class_="quote")

        if not posts_on_page:
            print("Is page par koi post nahi mili. Stopping...")
            break
        for post in posts_on_page:
            text_element = post.find("span", class_="text")

            if text_element:
                post_text = text_element.text.strip()
            else:
                post_text = "Missing Text"

            if post_text in seen_titles:
                print("⚠️ Ye to pehle se hai! Skip kar do.")
                continue

            seen_titles.add(post_text)
            all_posts.append({"content": post_text})

        next_button = soup.find("li", class_="next")
        if next_button and next_button.find("a"):
            next_page_link = next_button.find("a")["href"]
            current_url = "https://quotes.toscrape.com" + next_page_link
            page_number += 1
            time.sleep(1)  
        else:
            print("🏁 Saare pages khatam!")
            current_url = None

    if all_posts:
        df = pd.DataFrame(all_posts)
       
        df.to_csv("forum_posts.csv", index=False)
        print(
            f"🎉 Mubarak ho! Total {len(df)} unique posts save ho gayin 'week 2/forum_posts.csv' me."
        )

if __name__ == "__main__":
    test_url = "https://quotes.toscrape.com/"
    start_crawling(test_url)