# OpenAI-Tokenizer
Calculate token count and cost of a OpenAI query.

## Setup

Import tiktoken  
`pip3 install tiktoken`

## Usage  
Function: get_cost_from_api_model_data_price()  
Accepts:
- api: "text"|"Chat"
- model: "gpt-3.5-turbo"|"gpt-4"|"text-davinci-003"| etc...
- data: 
  -  If you are using the Text Completion API (api = "text") the data type should be a string of your message to send.
     -  Example:    
      ```python
      message = "Hello World!"
      ```
  -  If you are using the Text Completion API (api = "chat") the data type should be a list of the messages to send.
     - Example:   
      ```python
      message = [
          {
              "role": "system",
              "name": "example_assistant",
              "content": "Let's talk later when we're less busy about how to do better.",
          },
          {
              "role": "user",
              "content": "This late pivot means we don't have time to boil the ocean for the client deliverable.",
          }
      ]
      ```
  
Example:
```python
cost = get_cost_from_api_model_data_price("text","gpt-3.5-turbo",message,0.002)
```
