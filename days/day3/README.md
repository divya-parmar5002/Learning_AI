# 🚀 Day 03 – Understanding Tokens & Token Usage in Large Language Models (LLMs)

> 📅 **Learning Day:** 03
> 🎯 **Topic:** Tokens, Tokenization, Prompt Tokens, Completion Tokens, Total Tokens, Token Usage

---

# 🎯 Learning Objective

On Day 03, I learned one of the most important concepts used in every Large Language Model (LLM): **Tokens**.

Whenever we use AI tools like ChatGPT, Claude, Gemini, or Groq, we often hear people say:

* "My token limit is over."
* "This model supports 128K tokens."
* "The API charges per token."

Before today, I only saw the word **token**, but I did not know what it actually meant.

The goal of Day 03 was to understand:

* What is a token?
* Why do AI models use tokens instead of plain text?
* How does text become tokens?
* What are Prompt Tokens?
* What are Completion Tokens?
* What is Total Token Usage?
* Why do AI companies charge based on tokens?
* How to check token usage using the Groq API?

---

# 📖 Quick Revision of Previous Days

### Day 01

I learned how to:

* Set up the AI development environment.
* Create a Groq client.
* Load API keys from a `.env` file.
* Send prompts to an LLM.
* Receive responses from the API.

---

### Day 02

I learned how to control AI responses using:

* System Role
* User Role
* Temperature

The AI could now answer questions in different styles and with different levels of creativity.

---

### Day 03

Today I learned what happens **inside the AI model** after a prompt is sent.

Instead of learning how to ask better questions, I learned **how AI reads and processes text internally.**

---

# 🧠 What is a Token?

A **Token** is the smallest unit of text that an AI model processes.

The AI model does **not** read complete sentences like humans do.

Instead, it first breaks the text into smaller pieces called **tokens**.

A token can be:

* A complete word
* Part of a word
* A punctuation mark
* A number
* A special symbol

Different AI models may split the same text differently because each model uses its own tokenizer.

---

# Simple Example

Sentence:

```text
I love Artificial Intelligence.
```

Possible tokens:

```text
I

love

Artificial

Intelligence

.
```

Another example:

```text
Walking
```

Possible tokens:

```text
Walk

ing
```

Another example:

```text
ChatGPT
```

Possible tokens (illustrative only):

```text
Chat

G

PT
```

> **Note:** The exact token split depends on the tokenizer used by the model.

---

# Why Don't AI Models Read Plain Text?

Humans can easily read:

```text
Hello, how are you?
```

But computers do not understand human language directly.

They understand numbers.

Therefore, before an AI model can process text, it must convert that text into numerical representations.

This is where tokenization becomes important.

---

# A Short Journey of Text Representation

Understanding this history helped me understand why tokens are needed.

---

## Step 1 – Binary Language

Every computer understands only binary.

```text
0

1
```

Although computers work using binary, humans cannot communicate efficiently using only 0s and 1s.

Therefore, another representation was needed.

---

## Step 2 – ASCII

ASCII assigned numbers to characters.

Example:

```text
A → 65

B → 66

C → 67
```

This made communication between humans and computers much easier.

However, ASCII only represents characters.

It does not help an AI understand the meaning of text.

---

## Step 3 – Word-Based Vocabulary

Earlier Natural Language Processing (NLP) systems tried storing complete words inside a vocabulary.

Example:

```text
Apple

Computer

Student

Teacher
```

This worked for common words.

But there were many problems.

What if a completely new word appeared?

Example:

```text
Zomato
```

If the word was not present in the vocabulary, the system struggled to understand it.

Maintaining a vocabulary containing every possible word in every language also became extremely difficult.

---

## Step 4 – Tokenization

Modern AI models solve this problem using **Tokenization**.

Instead of storing only complete words, the tokenizer can split text into smaller meaningful pieces.

Example (illustrative only):

```text
Zomato

↓

Zo

mato
```

Another example:

```text
Playing

↓

Play

ing
```

This approach allows AI models to understand both common words and many new or uncommon words.

---

# What is Tokenization?

**Tokenization** is the process of breaking text into tokens before sending it to the AI model.

Every prompt follows this workflow:

```text
User Prompt

↓

Tokenizer

↓

Tokens

↓

Token IDs (Numbers)

↓

Large Language Model

↓

Generated Token IDs

↓

Tokens

↓

Readable Text

↓

User
```

The AI never directly understands plain English.

It processes numerical token IDs internally and then converts the generated tokens back into human-readable text.

---

# Prompt Tokens

Prompt Tokens are the tokens that come from the user's input.

Example:

User Prompt:

```text
Explain AI in short.
```

Every token inside this prompt contributes to the Prompt Token count.

The longer the prompt, the more Prompt Tokens are used.

---

# Completion Tokens

Completion Tokens are the tokens generated by the AI model as its response.

Example:

Prompt:

```text
Explain AI in short.
```

Response:

```text
Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.
```

Every token in this response contributes to the Completion Token count.

A longer answer uses more Completion Tokens.

---

# Total Tokens

Total Tokens represent the total amount of work done during one API request.

Formula:

```text
Total Tokens

=

Prompt Tokens

+

Completion Tokens
```

Example:

```text
Prompt Tokens      : 18

Completion Tokens  : 52

----------------------------

Total Tokens       : 70
```

---

# Why Do AI Companies Charge Per Token?

AI models perform computation on every token they process.

Whenever an API request is sent:

1. The user's text is converted into tokens.
2. Those tokens are processed by the model.
3. The model generates response tokens.
4. The response tokens are converted back into readable text.

Since computation happens on tokens, most AI providers calculate usage and pricing based on the total number of processed tokens rather than the number of prompts.

---

# Key Points Learned Today

* AI models do not read plain text directly.
* Every prompt is converted into tokens.
* Tokens are converted into numerical IDs before entering the model.
* A token can be a complete word or part of a word.
* Different models may tokenize the same text differently.
* Prompt Tokens come from the user's input.
* Completion Tokens come from the AI's response.
* Total Tokens = Prompt Tokens + Completion Tokens.
* AI companies usually measure usage and pricing using total tokens.

---
# 💻 Code Explanation

In this program, I wanted to understand **how different prompts consume different numbers of tokens**.

Instead of printing only the AI response, I also printed the token usage returned by the API.

---

## Step 1 – Importing Libraries

```python
import os
from dotenv import load_dotenv
from groq import Groq
```

### `os`

The `os` module is used to read environment variables.

It allows me to securely access my API Key stored in the `.env` file.

---

### `load_dotenv()`

```python
load_dotenv()
```

This function loads all environment variables from the `.env` file into the current Python environment.

---

### `Groq`

```python
from groq import Groq
```

The `Groq` class is used to create a client that communicates with the Groq API.

---

# Reading the API Key

```python
my_api_key = os.getenv("GROQ_API_KEY")
```

This line reads the value of `GROQ_API_KEY` from the environment variables.

Instead of writing the API Key directly in the code, it is stored safely inside the `.env` file.

This is considered a good security practice.

---

# Checking Whether the API Key Exists

```python
if not my_api_key:
    raise ValueError("No API Available")
```

Before creating the client, I check whether the API Key exists.

If the key is missing, the program immediately stops and displays an error.

This prevents invalid API requests.

---

# Creating the Groq Client

```python
client = Groq(api_key=my_api_key)
```

Using the API Key, a Groq client is created.

The client is responsible for sending requests to the Groq server and receiving responses.

---

# Selecting the AI Model

```python
model = "llama-3.3-70b-versatile"
```

This specifies which Large Language Model will generate the response.

---

# Creating Multiple Prompts

Instead of testing only one prompt, I created three different prompts.

```python
prompt1 = "Hii"
prompt2 = "Explain AI in short"
prompt3 = "Give me essay on LLM"
```

These prompts have different lengths.

Therefore, they also consume different numbers of tokens.

---

# Creating a Prompt List

```python
prompts = [prompt1, prompt2, prompt3]
```

Instead of repeating the same code three times, I stored all prompts inside a list.

This makes the code cleaner and easier to maintain.

---

# Using a Loop

```python
for prompt in prompts:
```

The loop processes one prompt at a time.

For every prompt:

* A message is created.
* The API request is sent.
* The response is received.
* Token usage is printed.

This avoids writing duplicate code.

---

# Creating the Message

```python
message = {
    "role": "user",
    "content": prompt
}
```

This creates a user message using the current prompt from the loop.

---

# Creating the Messages List

```python
messages = [message]
```

The API expects a list of messages.

Even when there is only one message, it must still be placed inside a list.

---

# Sending the API Request

```python
response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=600
)
```

This sends the request to the Groq server.

The request contains:

* Selected model
* User message
* Maximum number of response tokens

---

# Understanding `max_tokens`

One new concept I learned today is **`max_tokens`**.

```python
max_tokens = 600
```

This tells the AI:

> "You are allowed to generate a maximum of 600 response tokens."

It **does not** limit the user's prompt.

It only limits the length of the AI's generated response.

---

## Example

Suppose the AI wants to generate an answer that needs **900 tokens**.

If:

```python
max_tokens = 600
```

The response will stop after approximately 600 generated tokens.

The answer may become incomplete.

---

Another example:

If the complete answer only needs **120 tokens**,

the AI will stop naturally after generating those 120 tokens.

It will **not** generate unnecessary extra text.

---

# Understanding `usage`

After receiving the response, I accessed:

```python
usage = response.usage
```

The `usage` object contains information about token consumption.

It helps me understand how many tokens were used during the API request.

---

# Prompt Tokens

```python
usage.prompt_tokens
```

These are the tokens used by my input prompt.

Longer prompts use more Prompt Tokens.

---

# Completion Tokens

```python
usage.completion_tokens
```

These are the tokens generated by the AI.

Longer responses consume more Completion Tokens.

---

# Total Tokens

```python
usage.total_tokens
```

Total Tokens are calculated as:

```text
Prompt Tokens

+

Completion Tokens

=

Total Tokens
```

This value is usually used for API usage and pricing.

---

# Understanding `finish_reason`

```python
response.choices[0].finish_reason
```

This tells us **why the AI stopped generating the response**.

The most common values are:

---

## `stop`

Example:

```text
Finish Reason: stop
```

This means the AI completed its answer normally.

The response ended naturally.

---

## `length`

Example:

```text
Finish Reason: length
```

This means the AI reached the `max_tokens` limit before finishing the answer.

The response may be incomplete.

---

# Program Output

The program prints something similar to:

```text
Prompt: Hii

Prompt Tokens: 8

Completion Tokens: 12

Total Tokens: 20

Finish Reason: stop
```

Another prompt:

```text
Prompt: Give me essay on LLM

Prompt Tokens: 10

Completion Tokens: 600

Total Tokens: 610

Finish Reason: length
```

This clearly shows how different prompts consume different numbers of tokens.

---

# Important Notes

* AI models process tokens instead of plain text.
* Different models may tokenize the same sentence differently.
* Prompt Tokens come from the user's input.
* Completion Tokens come from the AI's output.
* Total Tokens = Prompt Tokens + Completion Tokens.
* `max_tokens` limits only the generated response.
* `max_tokens` does **not** limit the user's prompt.
* `finish_reason = stop` means the answer finished normally.
* `finish_reason = length` means the response stopped because it reached the maximum token limit.

---

# Key Takeaways

After completing Day 03, I can:

* Explain what a token is.
* Understand why tokenization is required.
* Explain how AI converts text into tokens.
* Understand Prompt Tokens, Completion Tokens, and Total Tokens.
* Read token usage from the API response.
* Control the maximum response length using `max_tokens`.
* Understand the purpose of `finish_reason`.
* Compare token usage for different prompts.

---

# Interview Notes

### What is a token?

A token is the smallest unit of text processed by an AI model. It can be a word, part of a word, punctuation, or another text unit depending on the tokenizer.

---

### Why do AI models use tokens instead of plain text?

AI models perform computations on numerical representations. Text is first broken into tokens, and those tokens are converted into token IDs before being processed.

---

### What is tokenization?

Tokenization is the process of breaking text into smaller units called tokens before sending it to the AI model.

---

### What are Prompt Tokens?

Prompt Tokens are the tokens present in the user's input.

---

### What are Completion Tokens?

Completion Tokens are the tokens generated by the AI in its response.

---

### What are Total Tokens?

Total Tokens are the sum of Prompt Tokens and Completion Tokens.

---

### What is `max_tokens`?

`max_tokens` specifies the maximum number of tokens the AI is allowed to generate in its response.

---

### What is `finish_reason`?

`finish_reason` explains why the model stopped generating text. Common values include `stop` (normal completion) and `length` (stopped because the maximum token limit was reached).

---

# Summary

Day 03 helped me understand how Large Language Models process text internally.

I learned that AI models do not read plain English directly. Instead, they convert text into tokens, process those tokens internally, and then generate new tokens that are converted back into readable text.

I also learned how to measure token usage using the Groq API, how Prompt Tokens, Completion Tokens, and Total Tokens are calculated, and how `max_tokens` and `finish_reason` influence the generated response.

Understanding tokens is an important foundation because almost every modern AI API uses token-based processing, context windows, and usage-based pricing.
