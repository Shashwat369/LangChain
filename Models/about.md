# LangChain Models

# Table of Contents

1. Introduction
2. What is a Model?
3. Why Do We Need Models?
4. How Models Work
5. Types of Models
6. LLM (Large Language Models)
7. Chat Models
8. Embedding Models
9. Model Providers
10. Model Parameters
11. Temperature
12. Max Tokens
13. Top P
14. Frequency Penalty
15. Presence Penalty
16. Streaming
17. Structured Output
18. Model Invocation
19. Error Handling
20. Best Practices
21. Interview Questions
22. Summary

---

# Introduction

Models are the brain of every AI application.

Whenever you ask ChatGPT a question, generate code, summarize text, translate languages, or create content, a model performs all of the reasoning.

LangChain provides a standard interface to interact with different AI models without changing your application code.

Instead of writing provider-specific code for OpenAI, Anthropic, Gemini, or Groq separately, LangChain allows developers to use one unified API.

---

# What is a Model?

A model is an AI system trained on massive datasets that can understand and generate human language.

It receives an input called a **Prompt** and returns an output called a **Response**.

Example

Input

```
What is Python?
```

Output

```
Python is a high-level programming language...
```

---

# Why Do We Need Models?

Without a model, an AI application cannot generate responses.

The model performs tasks such as

- Question Answering
- Summarization
- Translation
- Coding
- Text Generation
- Classification
- Reasoning
- Conversation
- Data Extraction

---

# How Models Work

```

User
│
▼
Prompt

```
│
▼
LangChain
│
▼
AI Model
│
▼
Response
│
▼
User

```

LangChain acts as a bridge between your application and the AI model.

---

# Types of Models

LangChain mainly supports three kinds of models.

```

Models
│
├── LLM
│
├── Chat Model
│
└── Embedding Model

```

---

# 1. LLM (Large Language Model)

An LLM receives plain text as input and generates plain text as output.

Input

```
Write a poem on nature.
```

Output

```
Nature is beautiful...
```

Characteristics

- Text Input
- Text Output
- No conversation history
- Simple completion tasks

Example

```python
from langchain_openai import OpenAI

llm = OpenAI()

response = llm.invoke("What is Machine Learning?")

print(response)
```

Use Cases

- Blog generation
- Article writing
- Code generation
- Summarization
- Translation

---

# 2. Chat Models

Chat Models are designed specifically for conversations.

Instead of plain text, they receive messages.

Example

```
System Message

You are a Python teacher.

Human Message

Explain loops.

AI Message

Loops repeat a block of code.
```

Example

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI()

response = model.invoke("Explain Python Functions")

print(response.content)
```

Chat Models maintain context much better than LLMs.

Use Cases

- Chatbots
- AI Assistants
- Customer Support
- Virtual Tutors

---

# LLM vs Chat Model

| Feature | LLM | Chat Model |
|----------|------|------------|
| Input | Text | Messages |
| Output | Text | AI Message |
| Conversation | No | Yes |
| Context | Limited | Better |
| Used For | Completion | Chatbots |

---

# 3. Embedding Models

Embedding models convert text into vectors (numbers).

Example

```
"I love AI"

↓

[0.24, 0.51, 0.92, ...]
```

These vectors capture the semantic meaning of text.

Similar meanings produce similar vectors.

Example

```
Dog

↓

[0.91, 0.11, ...]

Puppy

↓

[0.90, 0.13, ...]

Similarity

98%
```

Example

```python
from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings()

vector = embedding.embed_query("Machine Learning")

print(len(vector))
```

Use Cases

- Semantic Search
- Recommendation Systems
- RAG
- Similarity Search
- Vector Databases

---

# Model Providers

LangChain supports many providers.

Examples

- OpenAI
- Anthropic
- Google Gemini
- Groq
- Ollama
- Hugging Face
- Cohere
- DeepSeek
- Mistral AI

Example

```
LangChain

↓

OpenAI

or

Gemini

or

Groq

or

Anthropic

```

Changing the provider usually requires only changing the model initialization.

---

# Model Parameters

Every model accepts configuration parameters.

Common parameters

- temperature
- max_tokens
- top_p
- frequency_penalty
- presence_penalty
- timeout
- streaming

---

# Temperature

Controls randomness.

Range

```
0 → Deterministic

2 → Very Creative
```

Examples

Temperature = 0

```
2 + 2 = 4
```

Always same answer.

Temperature = 1

```
Write a fantasy story.
```

Different output every time.

Example

```python
ChatOpenAI(
    temperature=0
)
```

---

# Max Tokens

Limits the maximum output length.

Example

```python
ChatOpenAI(
    max_tokens=100
)
```

If response exceeds 100 tokens, generation stops.

---

# Top P

Controls diversity by selecting tokens from the top cumulative probability.

Lower value

```
More Focused
```

Higher value

```
More Diverse
```

---

# Frequency Penalty

Reduces repeated words.

Example

Without penalty

```
AI AI AI AI AI
```

With penalty

```
AI is transforming technology.
```

---

# Presence Penalty

Encourages the model to introduce new topics.

Higher value

```
More diverse content
```

---

# Streaming

Instead of waiting for the full response, tokens are generated one by one.

Without Streaming

```
Wait...

↓

Complete Answer
```

With Streaming

```
H

He

Hel

Hell

Hello...
```

Useful for chat applications.

---

# Structured Output

Instead of plain text, models can return structured data.

Example

```json
{
    "name":"John",
    "age":25
}
```

Useful for

- APIs
- Automation
- Data Extraction

---

# Model Invocation

LangChain uses a common method called invoke().

Example

```python
response = model.invoke("Explain AI")
```

Regardless of provider, the interface remains consistent.

---

# Error Handling

Example

```python
try:
    response = model.invoke("Hello")
    print(response)
except Exception as e:
    print(e)
```

Always handle

- Network Errors
- API Errors
- Rate Limits
- Authentication Errors

---

# Best Practices

✔ Choose the correct model.

✔ Keep prompts clear.

✔ Use low temperature for factual tasks.

✔ Use higher temperature for creative tasks.

✔ Use embeddings for semantic search.

✔ Cache responses whenever possible.

✔ Handle API failures.

✔ Protect API keys.

✔ Stream long responses.

✔ Monitor token usage.

---

# Interview Questions

## What is a Model in LangChain?

A model is an abstraction that allows developers to interact with different AI providers through a unified interface.

---

## Difference between LLM and Chat Model?

LLMs work with plain text while Chat Models work with structured messages and maintain conversation context.

---

## What are Embeddings?

Embeddings are vector representations of text used for semantic similarity and retrieval.

---

## What is Temperature?

Temperature controls randomness in model outputs.

Lower temperature produces deterministic answers.

Higher temperature produces creative answers.

---

## What is invoke()?

invoke() is the standard LangChain method used to send input to a model and receive its response.

---

## Why use LangChain instead of provider SDKs?

LangChain provides

- Standard Interface
- Easy Provider Switching
- Chains
- Agents
- Memory
- RAG Integration
- Tools
- Document Processing

---

# Summary

LangChain Models are the core component responsible for generating responses in AI applications.

The three primary model categories are:

- LLMs for text generation
- Chat Models for conversational AI
- Embedding Models for semantic understanding

LangChain abstracts provider-specific implementations into a unified interface, making AI application development faster, cleaner, and easier to maintain.