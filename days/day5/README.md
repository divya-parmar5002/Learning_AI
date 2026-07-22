# 🚀 Day 05 – Prompt Engineering: Designing Reliable & Production-Ready Prompts

> 📅 Learning Day: 05  
> 🎯 Topic: Prompt Engineering, Good Prompts, Bad Prompts, Roles, Tasks, Constraints, Output Formats, Examples & Fallbacks

---

## 📚 Concepts Covered

- Prompt Engineering
- Production-Ready Prompts
- Stability and Consistency
- Role
- Task
- Constraints
- Boundaries
- Output Format
- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Examples
- Fallback Handling
- Out-of-Scope Queries
- Prompt Structure
- Good Prompt vs Bad Prompt

---

# 🎯 Learning Objective

On Day 05, I learned about **Prompt Engineering** and how to design better prompts for Large Language Models (LLMs).

Until now, I was mainly learning how to send prompts to an LLM and get responses.

Today, I learned that simply asking a question is not always enough.

In real-world and production AI applications, we want the AI to:

- Behave consistently.
- Follow specific instructions.
- Stay within a defined scope.
- Perform a specific task.
- Return the output in a specific format.
- Handle unexpected or unrelated questions properly.
- Follow examples when necessary.

For example, if I am building a chatbot for a food delivery company, I may want the chatbot to answer questions about:

- Food orders
- Delivery
- Payments
- Refunds

But I may not want the same chatbot to write Python code or explain Machine Learning.

Therefore, I need to clearly define the chatbot's:

- Role
- Responsibility
- Task
- Boundaries
- Output Format
- Examples
- Fallback behavior

This is where **Prompt Engineering** becomes important.

---

# 🧠 What is Prompt Engineering?

Prompt Engineering is the process of designing and structuring instructions given to an AI model so that it produces more useful, relevant, consistent, and controlled responses.

A prompt is not always just a question.

A well-designed prompt can contain:


Role
   ↓
Task
   ↓
Constraints
   ↓
Output Format
   ↓
Examples
   ↓
Fallback Behavior


A simple prompt may work for experimentation.

However, a production application usually needs a more carefully designed prompt.

---

# 🤔 Why Do We Need Better Prompts?

When we ask the same question to an LLM multiple times, we may sometimes receive different responses.

For example:


Prompt:
Suggest a name for my food company.


The AI might respond:


FreshBite


Another time:


FoodNova


Another time:


TasteHub


This variation can be useful for creative tasks.

However, in some production applications, we want the model to behave more consistently.

For example, suppose we create a customer support chatbot.

If a customer asks:


How can I cancel my order?


We do not want the chatbot to provide a completely different process every time.

We want the chatbot to follow the same rules and provide reliable answers.

Therefore, in production systems, we often try to improve **stability, consistency, and control**.

---

# 🔄 Stability and Consistency

Stability means that the AI should behave consistently when handling similar requests.

For example:


User:
I want to cancel my order.


The chatbot should consistently understand that this is an **Order Cancellation** request.

It should not answer:


Here is a Python program to cancel your order.


or:


You should contact a restaurant to order food.


The goal is to make the AI behavior predictable and aligned with the application's purpose.

---

# ⚠️ Important Note About Stability

Prompt Engineering can improve consistency, but it does not guarantee that an LLM will always produce exactly the same response.

LLMs are probabilistic systems.

Their output can be influenced by factors such as:

- Temperature
- Model behavior
- Prompt wording
- Context
- Sampling

Therefore, production systems often combine prompt engineering with other techniques such as:

- Lower temperature
- Structured output
- Validation
- Output parsing
- Guardrails
- Evaluation
- Application-level rules

Prompt Engineering is one part of building a reliable AI system.

---

# 🚧 Why Do We Need Limits and Boundaries?

A production AI system should have a clearly defined scope.

For example, imagine a chatbot designed for a food delivery company.

The chatbot may be responsible for:

- Order status
- Order cancellation
- Refunds
- Payment issues
- Delivery problems

Now imagine a user asks:


Write a Python program to sort a list.


The chatbot should not suddenly become a Python teacher.

This is an **out-of-scope query**.

Therefore, we should define boundaries.

For example:


The chatbot only handles food-order-related customer support queries.


Now the AI knows what it is responsible for and what it should not handle.

---

# ❌ Bad Prompt

A bad prompt is often vague and does not provide enough information about the task.

Example:


My laptop is not working.
Handle this.


This prompt has many problems.

The AI does not know:

- What role should it play?
- What exactly is the task?
- What type of issue is this?
- What are the allowed categories?
- What output should it return?
- What should it do if the issue is unrelated?
- How detailed should the answer be?

The instruction is too vague.

---

# 🧠 Problems with the Bad Prompt

Let's understand the problems one by one.

---

## 1. No Clear Role

The prompt does not tell the AI who it is supposed to be.

Should it behave as:

- A Customer Support Agent?
- A Technical Support Engineer?
- A Laptop Repair Technician?
- A Salesperson?

The role is unclear.

---

## 2. No Clear Task

The prompt says:


Handle this.


But "handle" can mean many things.

Should the AI:

- Diagnose the problem?
- Ask questions?
- Classify the issue?
- Give troubleshooting steps?
- Create a support ticket?

The task is unclear.

---

## 3. No Constraints

There are no boundaries.

The AI does not know what topics it is allowed to handle.

---

## 4. No Output Format

The prompt does not specify how the response should look.

Should the AI return:


Technical


or:


This seems to be a technical issue with your laptop.


or:


{
    "category": "technical"
}


The expected output format is not defined.

---

## 5. No Examples

The AI has not been given examples of expected behavior.

Therefore, it has to interpret the task on its own.

---

## 6. No Fallback Behavior

What should happen if the user asks something unrelated?

For example:


Write me a Python program.


The prompt does not explain how to handle this situation.

---

# ✅ Good Prompt

A better prompt provides clear instructions.

A structured prompt may contain:


1. Role
2. Task
3. Constraints
4. Output Format
5. Examples
6. Fallback


This gives the AI a clear framework for solving the problem.

---

# 1️⃣ Role – Who Are You?

The role defines who the AI should act as.

The role should be related to the actual responsibility of the AI.

### ❌ Weak Role


You are a genius engineer.


This is vague.

"Genius" does not define the actual responsibility.

---

### ✅ Better Role


You are a Senior Technical Support Engineer responsible for classifying customer support issues.


Now the AI knows:

- Its domain is technical support.
- It is acting as a technical support engineer.
- Its responsibility is issue classification.

The role should be connected to the actual task.

---

# 2️⃣ Task – What Is Your Work?

The task tells the AI exactly what it needs to do.

For example:


Classify the customer's issue into one of the following categories:
billing, technical, or return.


Now the AI knows its exact responsibility.

It is not asked to solve the issue.

It is asked to **classify the issue**.

This distinction is important.

---

# 3️⃣ Constraints – What Are the Boundaries?

Constraints define what the AI is allowed to do.

For example:


Allowed categories are only:
- billing
- technical
- return


This prevents the model from inventing additional categories.

For example, it should not return:


shipping


if shipping is not an allowed category.

Constraints help control the model's behavior.

---

# 4️⃣ Output Format – What Should the Answer Look Like?

We should clearly define the expected output.

For example:


Return only one word.


Now the model should return something like:


technical


instead of:


The customer's issue is related to a technical problem.


This is useful when the output will be processed by another program.

---

# 5️⃣ Examples – Show the AI What You Expect

Sometimes instructions are not enough.

Examples can make the expected behavior much clearer.

For example:


Example 1:

Input:
My payment was deducted but my order was not placed.

Output:
billing


Another example:


Example 2:

Input:
I received a damaged product and want to send it back.

Output:
return


Now the AI can understand the expected pattern.

---

# 6️⃣ Fallback – What If the Query Is Unrelated?

A production system should also define what to do when the user's query does not fit into any allowed category.

For example:


If the user's query does not belong to any of the allowed categories, return:
other


Now if the user asks:


Write a Python program for me.


The AI can return:


other


This is called **Fallback Handling**.

---

# 🔄 Complete Prompt Structure

A production-oriented prompt can look like this:


ROLE:
You are a Senior Customer Support Engineer responsible for classifying customer issues.

TASK:
Classify the user's issue into one of the allowed categories.

CONSTRAINTS:
Allowed categories are:
- billing
- technical
- return

OUTPUT FORMAT:
Return only one word.

EXAMPLES:

Input:
My payment was deducted but my order was not placed.
Output:
billing

Input:
My laptop is not turning on.
Output:
technical

Input:
I want to return the product.
Output:
return

FALLBACK:
If the issue does not belong to any allowed category, return:
other


This prompt is much more controlled than:


My laptop is not working.
Handle this.


---

# 📌 Production Prompt Checklist

Before using a prompt in a production application, I should ask:

### Role


Who is the AI?


### Task


What exactly should the AI do?


### Constraints


What is the AI allowed or not allowed to do?


### Output Format


What should the final answer look like?


### Examples


Can examples help the AI understand the expected behavior?


### Fallback


What should happen if the user's request is outside the defined scope?


---

# 🎯 Key Learning

A good prompt is not just a question.

A good prompt is a **complete set of instructions** that defines:


Who you are
      +
What you need to do
      +
What you are allowed to do
      +
How the answer should look
      +
Examples of expected behavior
      +
What to do when the request is outside your scope


This makes the AI's behavior more controlled, predictable, and useful for production applications.