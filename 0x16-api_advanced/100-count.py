import requests

def count_words(subreddit, word_list, instances=None, after=None, count=0):
    if instances is None:
        instances = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    try:
        response.raise_for_status()
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        for post in results.get("children"):
            title_words = post.get("data").get("title").lower().split()
            for word in word_list:
                if word.lower() in title_words:
                    times = title_words.count(word.lower())
                    instances[word] = instances.get(word, 0) + times
    except requests.exceptions.RequestException:
        print("An error occurred while fetching data from Reddit.")
        return

    if after is None:
        if instances:
            sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_instances:
                print(f"{word}: {count}")
        else:
            print("No matching words found in the subreddit.")
    else:
        count_words(subreddit, word_list, instances, after, count)

# Example usage
subreddit = "python"  # Replace with the desired subreddit
word_list = ["python", "programming", "javascript"]  # Replace with your desired keywords
count_words(subreddit, word_list)
