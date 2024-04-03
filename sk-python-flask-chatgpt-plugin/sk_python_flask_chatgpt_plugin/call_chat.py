import requests

def call_chat_with_message(text):
    request_body = {
        "message": {
            "text": text
        },
        "source": "call_chat",
        "traceId": "12345",
        "messageProgress": "INTERMEDIATE",
        "optionsSets": ["codepusher","stream_writes","prompt_coloring","enable_stop_suggestion"]
    }
    headers = {
        "Authorization": "COPY BEARER TOKEN HERE"
    }
    response = requests.post("https://localhost:44344/Chat", json=request_body, headers=headers, verify=False)
    print(response)
    print(response.json())

def main():
    call_chat_with_message("Search for the oldest ever elephant and then write python code in a single-line string to print the prime factorization of the elephant's age. Push it to git with the filename 'elephant.py'")
    call_chat_with_message("What were the 3 biggest animals in history? Summarize it like you would explain to a five year old, and download the summary to a file using codepusher.")

if __name__ == "__main__":
    main()