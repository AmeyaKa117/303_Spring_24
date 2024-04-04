import wikipedia
import time

def get_wiki_references(topic):
    page = wikipedia.page(topic, auto_suggest=False)
    title = page.title
    references = page.references
    
    filename = title.replace("/", "-").replace("\\", "-")
    
    with open(f"{filename}.txt", "w", encoding='utf-8') as file:
        for ref in references:
            file.write(ref + "\n")

def sequential_download():
    start_time = time.perf_counter()
    
    topics = wikipedia.search("generative artificial intelligence")
    
    for topic in topics:
        try:
            get_wiki_references(topic)
        except Exception as e:
            print(f"Error processing topic {topic}: {e}")
    
    elapsed_time = time.perf_counter() - start_time
    print(f"Sequential download took {elapsed_time:.2f} seconds")

sequential_download()
