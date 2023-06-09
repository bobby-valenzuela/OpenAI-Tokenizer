import tiktoken

# Text-Completion API
def num_tokens_from_string(string: str, model_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# Chat API
def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
    """Returns the number of tokens used by a list of messages."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        print("Warning: gpt-3.5-turbo may change over time. Returning num tokens assuming gpt-3.5-turbo-0301.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
        return num_tokens_from_messages(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")
    
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>

    return num_tokens

def get_cost_from_api_model_data_price(api: str = "chat", model: str="gpt-3.5-turbo", data = "", tokenprice: float = 0.0):

    api = api.lower()

    valid_api = {"chat","text"}

    if api not in valid_api:
        raise ValueError("results: api must be one of %r." % valid_api)

    if api == "chat"and type(data) != list:
        raise ValueError("results: message must be one of type [list] when using the Chat Completion API.")

    if api == "text"and type(data) != str:
        raise ValueError("results: message must be one of type [string] when using the Text Completion API.")


    # Chat API vs Text-Completion API
    if api == "chat":
        num_tokens = num_tokens_from_messages(data, model)

    if api == "text":
        num_tokens = num_tokens_from_string(data, model)


    print(f"\nNum Tokens: {num_tokens}")


    price_per_tokencost = int(num_tokens) * float(tokenprice)

    print(f"Total Cost: {price_per_tokencost}")

cost = get_cost_from_api_model_data_price("text","gpt-3.5-turbo","Hello world!",0.002)
