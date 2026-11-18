from langchain_openai import ChatOpenAI

MODEL_NAME = "gpt-4.1-mini"

llm = ChatOpenAI(
    # 1. Model
    model=MODEL_NAME,

    # 2. Generation / sampling
    temperature=1.0,
    top_p=1.0,

    # 3. Output length
    max_tokens=1000,

    # 4. Repetition penalties
    presence_penalty=0.0,
    frequency_penalty=0.0,

    # 5. Request configuration
    timeout=60,
    max_retries=2,

    # 6. Reproducibility
    seed=42,

    # 7. Debugging / probability information
    logprobs=False,

    # 8. Number of candidate responses
    n=1,
)