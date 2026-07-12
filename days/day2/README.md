# 🚀 Day 02 – Understanding System Role & Temperature

## 🎯 Learning Objective

On Day 02, I learned how to **control the behavior of an AI model** instead of simply asking questions.

On Day 01, I learned how to send a prompt to an LLM using the Groq API.

On Day 02, I learned:

* What is a **System Role**?
* Why do we use a System Role?
* What is **Temperature**?
* How does Temperature affect AI responses?
* How to use both in a real Python program.

---

# 📖 Quick Revision of Day 01

Before learning new concepts, let's quickly remember the LLM workflow.

```text
User
   │
   ▼
Python Program
   │
   ▼
Groq Client
   │
   ▼
Groq Server
   │
   ▼
Selected LLM
   │
   ▼
Generated Response
```

On Day 01, I learned how to send prompts to an LLM.

Today, I learned **how to control the way the LLM responds.**

---

# 🧠 Concept 1 – System Role

## What is a System Role?

A **System Role** is a special instruction given to the AI **before** the user's question.

It tells the AI:

* Who it should act as.
* How it should behave.
* What style it should use.
* What rules it should follow.
* How the final answer should look.

Think of the System Role as **setting the personality and behavior of the AI**.

---

## Simple Example

Without a System Role:

**User**

> Suggest a name for my food company.

The AI may return:

* FoodHub
* FreshBite
* TastyFoods

The AI is free to answer in any style.

---

With a System Role:

```text
You are a brand manager who suggests names for food companies.
The name should be in one word.
```

Now the AI understands:

* It is acting as a **Brand Manager**.
* It should suggest **brand names**, not descriptions.
* Every name should contain **only one word**.

Possible answers:

* Swadify
* Bitezo
* Cravio
* Zestly

The System Role changes **how** the AI answers, not **what** the user asks.

---

# Why Do We Use a System Role?

We use a System Role to control the AI.

Instead of giving only a question, we first tell the AI:

* What role to play.
* What writing style to use.
* What format to follow.
* What rules it must obey.

This helps us get more accurate and consistent responses.

---

# Real Life Examples

## Example 1

```text
You are an experienced Python teacher.
```

Now every answer will be explained like a teacher.

---

## Example 2

```text
Always answer in one sentence.
```

The AI will keep every answer short.

---

## Example 3

```text
Explain everything using simple English.
```

The AI will avoid difficult words.

---

## Example 4

```text
You are a software interviewer.
```

The AI behaves like an interviewer instead of a teacher.

---

# Message Structure

The System Role is written as another message.

```python
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests names for food companies. Name should be in one word."
}
```

The user's question is written separately.

```python
message = {
    "role": "user",
    "content": "Suggest me a name for my food company"
}
```

Both messages are sent together.

```python
messages = [
    message_system,
    message
]
```

The AI first reads the System Role and then reads the User's question.

---

# 🧠 Concept 2 – Temperature

## What is Temperature?

Temperature controls **how random or creative** the AI should be while generating a response.

It does **not** change the user's question.

It changes **how the answer is generated**.

---

## Temperature Range

Usually:

```text
0.0  →  2.0
```

Lower value = Less creativity

Higher value = More creativity

---

# Temperature = 0

Very low randomness.

The AI gives predictable and consistent answers.

Best for:

* Coding
* Mathematics
* SQL Queries
* Facts
* Technical explanations

Example:

Prompt:

> What is 2 + 2?

Answer:

> 4

Every time, the answer will be almost the same.

---

# Temperature = 0.5

Balanced creativity.

The answers are still reliable but may contain small variations.

---

# Temperature = 1

Creative.

The AI has more freedom while generating responses.

Useful for:

* Writing
* Brainstorming
* Storytelling
* Ideas

---

# Temperature = 2

Very high creativity.

The AI becomes much more random.

Useful for:

* Brand names
* Poems
* Stories
* Creative writing
* Marketing ideas

Sometimes the response may become unusual because randomness is very high.

---

# Food Company Example

Prompt:

> Suggest me a name for my food company.

### Temperature = 0

Possible answers:

* FoodHub
* FreshMeal
* TastyFoods

These are simple and predictable.

---

### Temperature = 2

Possible answers:

* Cravio
* Swadify
* BiteNova
* Zestora

These names are much more creative.

---

# Complete Flow

```text
System Role
        │
        ▼
Tell the AI how to behave
        │
        ▼
User Prompt
        │
        ▼
Selected Model
        │
        ▼
Temperature decides
how creative the answer should be
        │
        ▼
Final Response
```

---

# Code Explanation

## Importing Libraries

```python
import os
from dotenv import load_dotenv
from groq import Groq
```

* `os` is used to read environment variables.
* `load_dotenv()` loads values from the `.env` file.
* `Groq` is used to create a client that communicates with the Groq API.

---

## Loading Environment Variables

```python
load_dotenv()
```

Loads all variables stored inside the `.env` file.

---

## Reading API Key

```python
my_api_key = os.getenv("GROQ_API_KEY")
```

Reads the API Key from the environment variables.

---

## Checking API Key

```python
if not my_api_key:
    raise ValueError("No API Available")
```

Stops the program if the API Key is missing.

---

## Creating the Client

```python
client = Groq(api_key=my_api_key)
```

Creates a Groq client that communicates with the Groq server.

---

## Selecting the Model

```python
model = "llama-3.3-70b-versatile"
```

Selects the AI model that will generate the response.

---

## Creating the System Message

```python
message_system = {
    "role": "system",
    "content": "You are a brand manager who suggests names for my food company. Name should be in one word."
}
```

This tells the AI:

* Act as a Brand Manager.
* Suggest only one-word company names.

---

## Creating the User Message

```python
message = {
    "role": "user",
    "content": "Suggest me a name for my food company"
}
```

This is the actual question asked by the user.

---

## Creating the Messages List

```python
messages = [
    message_system,
    message
]
```

The API accepts a list because multiple messages can be sent together.

The System message is kept first so that the AI understands its behavior before reading the user's question.

---

## Sending the Request

```python
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)
```

The request contains:

* Selected Model
* Messages
* Temperature

The API sends everything to the Groq server and receives the generated response.

---

## Extracting the Final Answer

```python
answer = response.choices[0].message.content
```

The response object contains a lot of information.

This line extracts only the generated text.

---

# Important Notes

* A System Role controls the behavior of the AI.
* A User Role contains the actual question.
* The System Role is usually placed before the User message.
* Temperature controls creativity and randomness.
* Low Temperature gives predictable answers.
* High Temperature gives creative answers.
* Temperature does not change the question.
* Temperature only changes the style of the generated response.

---

# Key Takeaways

After Day 02, I can:

* Use a System Role to control AI behavior.
* Tell the AI to follow specific instructions.
* Make the AI respond in a particular format.
* Understand the purpose of Temperature.
* Choose different Temperature values based on the task.
* Send multiple messages in one API request.
* Understand why the System message comes before the User message.

---

# Interview Notes

### What is a System Role?

A System Role provides instructions that define the AI's behavior, personality, rules, and response style before the user's question.

---

### What is Temperature?

Temperature controls the randomness and creativity of the AI's response.

---

### Why is the System Role placed first?

Because the AI should understand its behavior before reading the user's prompt.

---

### Does Temperature change the user's question?

No.

It only changes how the answer is generated.

---

# Summary

Day 02 was about learning how to control AI responses.

I learned that the **System Role** allows me to define the AI's behavior, while **Temperature** controls the creativity of the generated response.

By combining these two concepts, I can make the AI behave in different ways and produce responses that are either more predictable or more creative, depending on the task.

This was my first step into **Prompt Engineering**, where the quality of instructions directly affects the quality of the AI's output.
