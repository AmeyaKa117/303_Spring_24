import wikipedia
import time
from concurrent.futures import ThreadPoolExecutor

def sequential_download():
    start_time = time.perf_counter()

    topics = wikipedia.search("generative artificial intelligence")
    for topic in topics:
        try:
            page = wikipedia.page(topic, auto_suggest=False)
            title = page.title
            references = page.references

            with open(f"{title}.txt", "w", encoding='utf-8') as file:
                for reference in references:
                    file.write(reference + "\n")

        except Exception as e:
            print(f"Error processing topic {topic}: {e}")

    elapsed_time = time.perf_counter() - start_time
    print(f"Sequential download took {elapsed_time} seconds")

sequential_download()

def wiki_dl_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = page.references

        with open(f"{title}.txt", "w", encoding='utf-8') as file:
            for reference in references:
                file.write(reference + "\n")
    except Exception as e:
        print(f"Error processing topic {topic}: {e}")

def concurrent_download():
    start_time = time.perf_counter()

    topics = wikipedia.search("generative artificial intelligence")
    with ThreadPoolExecutor() as executor:
        executor.map(wiki_dl_and_save, topics)

    elapsed_time = time.perf_counter() - start_time
    print(f"Concurrent download took {elapsed_time} seconds")

concurrent_download()
