import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

def save_references(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references
        
        filename = title.replace("/", "-").replace("\\", "-")
        
        with open(f"{filename}.txt", "w", encoding='utf-8') as file:
            file.write("\n".join(references))
    except Exception as e:
        print(f"Error processing topic {topic}: {e}")

def concurrent_download():
    start_time = time.perf_counter()
    
    topics = wikipedia.search("generative artificial intelligence")
    
    with ThreadPoolExecutor() as executor:
        executor.map(save_references, topics)
    
    elapsed_time = time.perf_counter() - start_time
    print(f"Concurrent download took {elapsed_time:.2f} seconds")

concurrent_download()