# Module 04 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Generative AI, LLMs, Prompts and Model Providers  
> **Purpose:** Prepare for beginner, intermediate, advanced, project-specific, follow-up, cross-question and pressure questions about how NovaMind uses AI models and providers.

---

## Practice Rule

For every answer, be able to explain:

```text
What is it?
Why is it used?
Where is it used in NovaMind?
What can fail?
What is the trade-off?
What would Production V2 improve?
```

Do not claim model training, fine-tuning, Bedrock inference, guaranteed hallucination prevention, or mature AI evaluation because those are not supported by the verified project implementation.

---

# Foundations

## Q1. What is Generative AI?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Generative AI is AI that creates new content such as text, code, images, summaries or explanations based on patterns learned during model training.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q2. What is an LLM?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> An LLM is a Large Language Model trained on large amounts of text-related data to generate and transform language.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q3. How is an LLM different from a normal database?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A database retrieves stored records. An LLM generates output from learned patterns and the context supplied in the request.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q4. What is inference?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Inference is using an already-trained model to generate an output from new input.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q5. Did NovaMind train its own LLM?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. The verified project integrates externally hosted pre-trained models and performs inference.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q6. Is fine-tuning implemented in NovaMind?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. The verified project does not include model fine-tuning.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q7. What is a token?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A token is a unit the model uses to represent input and output text.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q8. Why do tokens matter?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> They affect context usage, output length, latency and often cost.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q9. What is a context window?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The context window is the amount of tokenized information the model can consider in one request.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q10. What can fill the context window?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> System instructions, user prompt, conversation history, retrieved document chunks, web-search results and other supplied context.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q11. What is a prompt?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A prompt is the instruction and input sent to a model.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q12. What is a system prompt?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A system prompt gives higher-level behavior, role, rules or formatting instructions.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q13. What is a user prompt?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The user prompt is the user's actual question or task request.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q14. What is prompt engineering?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Prompt engineering is designing instructions and context so the model is more likely to produce useful, consistent and parseable output.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q15. What is temperature?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Temperature is a generation parameter that affects output variation or randomness.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q16. Does higher temperature mean higher intelligence?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. It changes generation variability, not intelligence.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q17. What are max output tokens?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A limit on how much the model can generate in one response.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q18. What is structured output?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A machine-readable response format, commonly JSON, that application code can parse.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q19. What is hallucination?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A hallucination is an output that sounds plausible but is unsupported or incorrect.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q20. Does RAG eliminate hallucinations?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. RAG can improve grounding, but retrieval and generation can still fail.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Model vs Provider

## Q21. What is the difference between a model and a provider?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A model is the AI system performing inference. A provider is the platform or API layer through which the application accesses models.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q22. Give a NovaMind example of provider vs model.

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> OpenRouter is the access layer, while `deepseek/deepseek-chat` is the model used by the Coding workflow.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q23. Is Groq a model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Groq is the inference/provider platform used by NovaMind. The configured model ID is `openai/gpt-oss-120b`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q24. Does `openai/gpt-oss-120b` mean NovaMind uses the OpenAI API?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. The verified implementation uses the Groq client/provider. The model identifier containing `openai/` does not mean the OpenAI API is being called.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q25. Is OpenRouter a model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. OpenRouter is the model-access layer used to access DeepSeek in the coding workflow.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q26. Is DeepSeek the provider?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> In NovaMind's coding path, DeepSeek is the model and OpenRouter is the access/provider layer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q27. Is Tavily an LLM?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Tavily is a web-search tool.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q28. Is Qdrant a model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Qdrant is the vector database used for PDF similarity retrieval.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q29. Is Stability AI used for chat?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. In the verified project it is used for image generation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q30. Is Gemini used for only one task?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Gemini is used for image analysis and separately for PDF embeddings.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Groq

## Q31. How is Groq used in NovaMind?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Groq is used as an inference provider for major language-generation workflows such as general chat, search synthesis and PDF-RAG answer generation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q32. What model ID is configured through Groq?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> `openai/gpt-oss-120b`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q33. What does Groq do in a normal Chat flow?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> NovaMind builds the prompt/context, sends it to the configured Groq-backed model and receives the generated text response.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q34. What does Groq do in Search?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Tavily retrieves current web information and the Groq-backed language-model path synthesizes those results into the final answer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q35. What does Groq do in PDF RAG?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> After Qdrant retrieves relevant PDF chunks, those chunks are supplied to the Groq-backed language-model path to generate the answer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q36. Why not say Groq is the RAG system?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Because RAG includes extraction, chunking, embeddings, vector retrieval, prompt augmentation and generation. Groq handles the final generation stage.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q37. What could cause a Groq request to fail?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Timeouts, rate limits, invalid credentials, provider outages, malformed requests or application-side parsing/error handling problems.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q38. Would adding more ECS tasks fix a Groq quota limit?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Provider quota is an external dependency limit and is not solved by scaling application containers.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q39. How would you monitor Groq usage in production?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Track request count, latency, error rate, timeout rate, input/output token usage where available and workflow-level cost.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q40. Should you blindly retry every failed Groq request?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Retrying must consider whether earlier application side effects already happened and whether the failure is safe to retry.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Gemini

## Q41. What are Gemini's two main verified roles?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Image analysis using `gemini-2.0-flash` and PDF embeddings using `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q42. What is an embedding model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A model that converts text or other content into a numeric vector representing semantic meaning.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q43. Does an embedding model generate the final answer?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. It produces vectors used for retrieval.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q44. How is `gemini-embedding-001` used in PDF RAG?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> PDF chunks and the user question are embedded so Qdrant can perform semantic similarity search.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q45. What does `gemini-2.0-flash` do?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It analyzes uploaded images with the user's prompt and returns a text response.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q46. Is image analysis the same as image generation?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Image analysis is image-to-text; image generation is text-to-image.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q47. Could Gemini analysis still be wrong?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes. Multimodal models can misread details, infer incorrectly or hallucinate.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q48. Why is the embedding model separate from the answer model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Embeddings optimize vector representation for retrieval, while a generative model produces natural-language answers.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q49. What happens if embedding generation fails?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The PDF RAG workflow cannot build or query the vector representation correctly, so retrieval cannot proceed normally.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q50. Could another embedding provider replace Gemini?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Potentially, but vector dimensions, quality, cost, latency and existing stored indexes would have to be considered.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# OpenRouter and DeepSeek

## Q51. How is the Coding workflow implemented at the model level?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> NovaMind sends coding requests through OpenRouter to `deepseek/deepseek-chat` and expects structured file output.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q52. Why is OpenRouter useful?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It provides a model-access layer that can expose multiple supported models through one integration pattern.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q53. What is the configured coding temperature?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The verified coding configuration uses temperature 0.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q54. Why is low temperature useful for structured code generation?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It can reduce output variation and improve consistency, although it does not guarantee valid structure.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q55. What is the approximate coding max-output setting?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Approximately 2500 output tokens in the verified configuration.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q56. Why does the coding workflow request structured JSON?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The frontend needs machine-readable file names and contents so it can build a code artifact and display files in Monaco.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q57. What can go wrong with model-generated JSON?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The model may add Markdown fences, extra explanation, malformed JSON, missing fields or broken escaping.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q58. How would you improve structured-output reliability?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Use explicit schemas, provider-supported structured output where available, server-side validation and safe repair/retry logic.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q59. Does DeepSeek execute the generated project?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. It generates structured source content; the current project does not provide a complete secure server-side execution and test loop.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q60. Is Monaco part of the model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Monaco is the frontend code editor used to display generated code.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Stability AI

## Q61. What is Stability AI used for?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Text-to-image generation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q62. What verified endpoint family is used?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> `stable-image/generate/core`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q63. What is the basic image-generation flow?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Prompt preparation → Stability AI → generated image bytes → S3 → presigned URL → frontend.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q64. Does Stability AI generate textual chat answers?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not in the verified NovaMind role.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q65. What failures can happen in image generation?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Provider errors, rate limits, invalid prompts, network timeouts, binary handling problems, S3 upload failures or URL-generation failures.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q66. Why store generated images in S3?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It separates generated files from container-local storage and provides durable object storage with controlled access.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q67. Does a successful Stability response mean the user can access the image?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not necessarily. S3 upload or presigned-URL generation can still fail afterward.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q68. Could image generation be moved to an async worker?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes, that can be useful for long-running jobs, but it is a Production V2 option rather than a current verified feature.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Tavily and Search

## Q69. What is Tavily's role?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Web retrieval/search.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q70. How does Search differ from Chat?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Chat sends prompt/context directly to the language model, while Search first retrieves current web information with Tavily and then synthesizes it with an LLM.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q71. How many Tavily results are configured?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Up to five results, with images also requested.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q72. Does Tavily generate the final answer?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. It returns search results; the Groq-backed language-model path synthesizes the answer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q73. Does the current Search workflow guarantee correct citations?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Mature citation alignment and fact checking are not verified.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q74. What is the prompt-injection risk with web search?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Retrieved web text is untrusted and may contain instructions that try to manipulate the model.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q75. What is a safe mental model for retrieved web content?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Treat it as untrusted data, not as trusted instructions.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q76. Why can Search cost more than Chat?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It uses additional retrieval and generation calls and therefore adds latency and provider usage.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q77. Could Search fail even if Groq is healthy?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes. Tavily can fail independently.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q78. Could Chat fail even if Tavily succeeded?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes. Retrieval can succeed while the later language-generation step fails.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# RAG and Model Interaction

## Q79. Which model creates PDF embeddings?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Gemini `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q80. Which component stores PDF vectors?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q81. Which component retrieves relevant chunks?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Qdrant similarity search.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q82. Which model generates the final PDF answer?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The Groq-backed language-model path.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q83. How many chunks are retrieved?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Top five in the verified implementation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q84. What is the approximate chunk size?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> About 1000 characters.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q85. What is the approximate overlap?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> About 200 characters.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q86. Why not send the entire PDF directly every time?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Retrieval can reduce irrelevant context and select the chunks most related to the question, though the current retrieval design has its own limitations.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q87. What if Qdrant returns irrelevant chunks?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The language model receives poor grounding and can generate a weak or incorrect answer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q88. Would a stronger LLM completely fix bad retrieval?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Retrieval quality and generation quality are separate parts of RAG.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q89. Is OCR implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Scanned/image-only PDFs are a current limitation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q90. Is reranking implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q91. Are mature page-level citations implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q92. Is persistent document reuse mature?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. The current design lacks a strong durable user-document-index mapping for long-term follow-up.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Prompts

## Q93. Where are prompts managed in NovaMind?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> They are embedded in specialist workflow source rather than managed by a mature centralized prompt registry.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q94. Why is a centralized prompt registry useful?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It allows versioning, review, testing, rollback and clearer ownership of prompt changes.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q95. What should a strong system prompt contain?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Clear role, task rules, safety/behavioral constraints and output-format requirements appropriate to the workflow.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q96. Why add retrieved context separately from instructions?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> To help the model distinguish source data from behavioral instructions.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q97. Can a system prompt fully prevent prompt injection?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q98. Why use explicit JSON-format instructions?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> To improve the chance that downstream parsing succeeds.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q99. What is few-shot prompting?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Providing examples of desired input-output behavior in the prompt.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q100. Is few-shot prompting verified as a systematic feature in NovaMind?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Do not claim a mature prompt-example framework unless supported by source.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q101. What is prompt regression testing?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Testing important prompts against a fixed evaluation set so changes do not silently reduce quality.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q102. Is a mature prompt regression suite implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Hallucination and Evaluation

## Q103. Why can LLMs hallucinate?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Because they generate probable sequences rather than querying a guaranteed truth source.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q104. How does RAG help?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It gives the model retrieved source context so the answer can be grounded in application-provided evidence.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q105. Why does RAG still fail?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Extraction, chunking, embeddings, retrieval and generation can each introduce errors.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q106. How would you evaluate RAG?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Measure retrieval relevance and answer quality/faithfulness using representative question-document test sets.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q107. Is a mature RAG evaluation suite implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q108. How would you evaluate routing?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Build labeled prompts/files and compare the expected specialist with the router's selected specialist.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q109. Is routing evaluation implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not as a mature automated suite.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q110. How would you evaluate coding output?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Validate schema first, then compile/test in a secure sandbox for applicable projects.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q111. Is that implemented?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q112. How would you evaluate image analysis?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Use labeled image-question examples and compare correctness, completeness and uncertainty handling.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q113. What is groundedness?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> How strongly the generated answer is supported by supplied source context.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Multi-Provider Design

## Q114. Why use multiple AI providers?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Different workflows need different capabilities such as language generation, coding, embeddings, vision, image generation and web retrieval.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q115. What is the biggest benefit?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Task-specific capability flexibility.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q116. What is the biggest cost?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Operational complexity across credentials, quotas, APIs, failures, latency and billing.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q117. Is more providers always better?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Each integration adds operational and security overhead.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q118. What criteria should you use to select a provider/model?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Capability, quality, latency, cost, context limits, output reliability, multimodal support, quotas, governance and reliability.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q119. What is provider lock-in?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> When application design becomes highly dependent on one provider's proprietary APIs or behavior.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q120. How can an abstraction layer help?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It can standardize some model invocation patterns, although provider-specific features still need explicit handling.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q121. Does NovaMind have a mature universal model abstraction?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The project uses LangChain/LangGraph integrations and direct provider APIs, but do not claim a complete provider-independent abstraction layer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q122. What is semantic fallback?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Switching to an alternate provider only when the alternate can preserve the meaning and guarantees of the original workflow.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q123. Why is fallback dangerous in RAG?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A fallback to ordinary chat could remove document grounding while still returning a fluent answer.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Reliability, Cost and Security

## Q124. What should you monitor for model APIs?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Latency, errors, timeouts, rate limits, token usage where available, provider availability and workflow-level success.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q125. Why do timeouts matter?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> External inference calls can become slow; without deadlines they can hold application requests open too long.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q126. What is a rate limit?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A provider or application limit on how many requests or tokens may be processed in a period.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q127. Can more ECS tasks solve a provider rate limit?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q128. What contributes to AI cost?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> LLM input/output tokens, embeddings, image generation, web search and repeated routing/classification calls.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q129. Are NovaMind credits a verified dollar-cost ledger?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Application credits are not the same as measured real provider cost.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q130. Why track per-workflow cost?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> To understand which features drive usage and to make pricing, limits and optimization evidence-based.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q131. Why are API keys sensitive?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Anyone with the key may be able to use the provider account and incur cost or access configured services.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q132. Where should provider secrets live?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Server-side secret management, not exposed in frontend code.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q133. What is prompt injection?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Untrusted input attempts to influence the model to ignore intended instructions or misuse tools/context.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q134. Can prompt injection come from PDFs?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q135. Can prompt injection come from search results?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q136. Can CORS prevent prompt injection?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. They are unrelated controls.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q137. Why validate model output?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Because model output is untrusted application input and can be malformed, unsafe or inconsistent.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q138. What is a circuit breaker?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> A reliability pattern that temporarily stops calls to a failing dependency to prevent cascading failures.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q139. Is a mature circuit-breaker system verified?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No; it is a possible Production V2 improvement.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Project Defense

## Q140. Give me the one-sentence model/provider architecture of NovaMind.

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> NovaMind uses LangGraph to route each request to a specialist workflow, and each workflow prepares task-specific context and calls the external model provider or tool best suited to that capability.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q141. Which provider handles general language generation?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Groq, using the configured model ID `openai/gpt-oss-120b`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q142. Which provider/model handles coding?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> DeepSeek `deepseek/deepseek-chat` accessed through OpenRouter.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q143. Which model handles image analysis?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Gemini `gemini-2.0-flash`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q144. Which model handles embeddings?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Gemini `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q145. Which provider handles image generation?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q146. Which tool handles current web retrieval?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Tavily.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q147. Does NovaMind use Bedrock for active inference?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No, not in the verified implementation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q148. Does NovaMind train or fine-tune models?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No, not in the verified implementation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q149. What is the strongest current AI-engineering feature?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> The project integrates several real specialist workflows, including a genuine PDF RAG pipeline with separate embeddings, vector retrieval and answer generation.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q150. What are the main AI maturity gaps?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Prompt versioning, schema enforcement, systematic AI evaluation, detailed cost telemetry, robust provider fallbacks and stronger prompt-injection defenses.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q151. What would you improve first?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> I would add structured validation and evaluation around the existing workflows before adding more models, then improve provider observability, cost tracking and security controls.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Pressure Questions

## Q152. You use several providers. Isn't that over-engineered?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It can be if the capability differences do not justify the operational cost. In NovaMind, different providers serve distinct tasks, but I would still measure quality, cost and reliability and consolidate where there is no clear benefit.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q153. Why not use one model for everything?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> One model could simplify operations, but it may not provide the best support for embeddings, vision, coding and image generation. The decision should be based on measured capability and cost.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q154. Why is `openai/gpt-oss-120b` not OpenAI API usage?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Because the application is invoking that configured model identifier through the Groq client/provider.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q155. If Groq goes down, can you just switch to DeepSeek?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not automatically. A fallback must preserve the workflow's expected behavior, prompt format, output schema, latency and quality, and it must be tested before production use.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q156. If Tavily fails, can the LLM answer anyway?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> It could generate from its existing model knowledge, but that would no longer satisfy the same current-web-search guarantee. I would make the degradation explicit rather than silently pretending search succeeded.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q157. If Qdrant fails, can you ask Groq directly?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> That would remove document retrieval and therefore the answer would no longer be grounded in the uploaded PDF. I would surface a retrieval failure or use a verified alternate retriever.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q158. Why not send every conversation message to the LLM forever?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Context windows are finite, long inputs increase cost and latency, and irrelevant history can reduce answer quality. A token-aware memory strategy is better.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q159. Can temperature 0 guarantee identical responses?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. It reduces randomness, but provider/model behavior can still vary.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q160. Can JSON prompting guarantee valid JSON?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Application-side schema validation is still required.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q161. Can a bigger model fix bad prompts?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not reliably. Poor instructions or context can still produce poor output.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q162. Can a bigger model fix bad RAG retrieval?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> Not reliably. Retrieval quality must be solved separately.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q163. Does using an LLM make the application intelligent enough to be autonomous?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Autonomy depends on orchestration, tool permissions, planning loops, state and control logic, not simply the presence of an LLM.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q164. Is LangGraph the model provider?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. LangGraph orchestrates workflow execution; model providers perform inference.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

## Q165. Is the project production-ready because it uses strong models?

**What the interviewer is testing:** Whether you understand the concept and can connect it accurately to NovaMind rather than repeating model/provider names.

**Word-for-word answer:**

> No. Model quality is only one part. Production readiness also requires security, reliability, evaluation, observability, cost controls and safe deployment.

**Likely follow-up:** Be ready to explain the request flow, failure case, cost/latency impact, provider/model distinction, or Production V2 improvement.

**What not to say:** Do not turn a provider into a model, a search/vector tool into an LLM, or an inference integration into model training.

---

# Rapid-Fire Revision

**Q166. Generative AI?**  
AI that creates new content.

**Q167. LLM?**  
Large Language Model.

**Q168. Training?**  
Updating model parameters from data.

**Q169. Inference?**  
Using a trained model to produce output.

**Q170. Token?**  
A model input/output unit.

**Q171. Context window?**  
The amount of tokenized content the model can consider in one request.

**Q172. System prompt?**  
Higher-level instructions, role and rules.

**Q173. User prompt?**  
The user's actual request.

**Q174. Temperature?**  
Controls output variation/randomness.

**Q175. Structured output?**  
Machine-readable response such as JSON.

**Q176. Hallucination?**  
Plausible but unsupported or incorrect model output.

**Q177. Groq role?**  
Inference provider for language generation.

**Q178. Configured Groq model?**  
`openai/gpt-oss-120b`.

**Q179. OpenAI API used?**  
Not in the verified Groq path.

**Q180. OpenRouter role?**  
Model-access layer.

**Q181. DeepSeek role?**  
Coding model.

**Q182. DeepSeek model ID?**  
`deepseek/deepseek-chat`.

**Q183. Coding temperature?**  
0.

**Q184. Coding max output?**  
Approximately 2500 tokens.

**Q185. Gemini image model?**  
`gemini-2.0-flash`.

**Q186. Gemini embedding model?**  
`gemini-embedding-001`.

**Q187. Stability role?**  
Image generation.

**Q188. Stability endpoint family?**  
`stable-image/generate/core`.

**Q189. Tavily role?**  
Web search.

**Q190. Tavily an LLM?**  
No.

**Q191. Qdrant role?**  
Vector storage and similarity retrieval.

**Q192. Qdrant an LLM?**  
No.

**Q193. RAG guaranteed factual?**  
No.

**Q194. OCR in PDF RAG?**  
No.

**Q195. Reranking?**  
No.

**Q196. Mature prompt registry?**  
No.

**Q197. Mature AI evaluation suite?**  
No.

**Q198. Foundation-model training?**  
No.

**Q199. Fine-tuning?**  
No.

**Q200. Bedrock inference active?**  
No.

**Q201. Main multi-provider benefit?**  
Task-specific capability.

**Q202. Main multi-provider cost?**  
Operational complexity.

**Q203. Can provider quotas be fixed by scaling ECS?**  
No.

**Q204. Should model output be trusted blindly?**  
No.

**Q205. Can temperature 0 guarantee identical output?**  
No.

**Q206. Can prompt instructions guarantee valid JSON?**  
No.

**Q207. What must validate JSON?**  
Application-side schema/parsing logic.

**Q208. What should retrieved PDF/web content be treated as?**  
Untrusted data.

**Q209. Best maturity wording?**  
Production-oriented, not production-ready.

# Provider Map to Memorize

```text
Groq
  → provider / inference platform
  → model: openai/gpt-oss-120b
  → general language generation

Google Gemini
  → gemini-2.0-flash
  → uploaded-image analysis

Google Gemini
  → gemini-embedding-001
  → PDF embeddings

OpenRouter
  → model access layer

DeepSeek
  → deepseek/deepseek-chat
  → coding workflow

Stability AI
  → stable-image/generate/core
  → image generation

Tavily
  → web search tool
  → not an LLM

Qdrant
  → vector DB
  → not a model
```

---

# 30-Second Interview Answer

> NovaMind uses multiple external AI providers for inference rather than training its own models. LangGraph routes each request to a specialist workflow. General language generation uses a Groq-backed model path, Coding accesses DeepSeek through OpenRouter, PDF RAG uses Gemini embeddings with Qdrant retrieval followed by Groq generation, uploaded-image analysis uses Gemini, image generation uses Stability AI, and current web retrieval uses Tavily before LLM synthesis.

---

# 60–90 Second Interview Answer

> NovaMind separates application workflow logic from the AI providers themselves. The Agent service uses LangGraph to route a request to a predefined specialist. That workflow then constructs the required prompt and context and calls the appropriate provider. General language generation is handled through Groq with the configured model ID `openai/gpt-oss-120b`. Coding uses `deepseek/deepseek-chat` through OpenRouter. PDF RAG uses `gemini-embedding-001` to create vectors, Qdrant for similarity retrieval and the Groq-backed language-model path for answer generation. Uploaded-image analysis uses `gemini-2.0-flash`, image generation uses Stability AI, and web search uses Tavily followed by language-model synthesis.
>
> The main benefit is task-specific flexibility. The trade-off is more operational complexity across API keys, latency, quotas, cost and failure modes. The current project also needs stronger prompt versioning, schema validation, AI evaluation, provider observability and prompt-injection defenses before I would call the AI layer production-ready.

---

# Architecture Defense Script

If the interviewer asks, **“How does an LLM request actually move through your project?”**

> A user request first reaches the application layer. The Agent service and LangGraph determine the specialist workflow. The workflow constructs instructions, the user prompt and any required context such as conversation history, retrieved PDF chunks or web-search results. It then calls the configured external provider API. The provider runs inference on the selected pre-trained model and returns output. NovaMind parses that output, applies any workflow-specific post-processing, persists relevant messages or artifacts and returns the final result to the frontend.

---

# Cross-Question Chains

## Chain 1 — Coding

**Q:** What model handles coding?  
**A:** DeepSeek through OpenRouter.

**Q:** Is OpenRouter the model?  
**A:** No. It is the access layer.

**Q:** Why structured output?  
**A:** The frontend needs a machine-readable files array.

**Q:** Can JSON prompting fail?  
**A:** Yes.

**Q:** How do you improve it?  
**A:** Schema validation, provider-supported structured output where available, and safe repair/retry.

**Q:** Does NovaMind execute the code?  
**A:** Not through a complete secure server-side compile/test/repair loop.

---

## Chain 2 — PDF RAG

**Q:** Which model creates embeddings?  
**A:** `gemini-embedding-001`.

**Q:** Where are they stored?  
**A:** Qdrant.

**Q:** Who generates the answer?  
**A:** The Groq-backed model path.

**Q:** Can RAG hallucinate?  
**A:** Yes.

**Q:** Why?  
**A:** Retrieval or generation can be wrong.

**Q:** How would you improve confidence?  
**A:** Evaluate retrieval relevance and answer groundedness, add better metadata/citations, and improve retrieval/reranking where evidence supports it.

---

## Chain 3 — Search

**Q:** Is Tavily an LLM?  
**A:** No.

**Q:** Then what does it do?  
**A:** Retrieves current web results.

**Q:** Who writes the final answer?  
**A:** The language-model generation path.

**Q:** What if Tavily fails?  
**A:** The current-search guarantee is lost; I would surface or explicitly degrade the workflow rather than silently pretending search succeeded.

---

# What You Must Never Overclaim

Do not say:

- “We trained GPT.”
- “We fine-tuned the NovaMind LLM.”
- “Bedrock powers the inference.”
- “OpenRouter is our coding model.”
- “Tavily is the LLM.”
- “Qdrant generates the RAG answer.”
- “RAG removes hallucination.”
- “Temperature zero guarantees deterministic output.”
- “The model always returns valid JSON.”
- “We have complete prompt-injection protection.”
- “We have a mature AI evaluation platform.”
- “The credits system exactly represents provider cost.”

Use:

> **external pre-trained models for inference**

> **Groq as inference provider**

> **DeepSeek through OpenRouter**

> **Gemini embeddings + Qdrant retrieval + Groq generation**

> **Tavily retrieval + LLM synthesis**

> **bounded LangGraph orchestration**

---

# Final Self-Test

Before moving to Module 05, you should be able to explain without notes:

- Generative AI
- LLM
- training vs inference
- tokens
- context windows
- system vs user prompts
- prompt engineering
- temperature
- max output tokens
- structured output
- hallucination
- model vs provider
- exact role of Groq
- why `openai/gpt-oss-120b` does not mean OpenAI API
- exact roles of Gemini
- OpenRouter vs DeepSeek
- Stability AI
- Tavily
- Qdrant's role
- AI API lifecycle
- why NovaMind uses multiple providers
- provider/model selection trade-offs
- prompt injection
- AI evaluation gaps
- Production V2 improvements

**Module 04 interview preparation complete.**
