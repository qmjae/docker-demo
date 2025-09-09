from api.ai.llms import get_openai_llm
from api.ai.schemas import EmailMessageSchema


def generate_email_msg(query:str) -> EmailMessageSchema:
    llm_base = get_openai_llm()
    llm = llm_base.with_structured_output(EmailMessageSchema)

    messages = [
        (
            "system",
            "You are a helpful assistant for research and content generation that helps people write better emails. Do not use markdown in your responses, use only plaintext.",
        ),
        ("human", f"{query}, Do not use markdown in your responses, use only plaintext."),
    ]

    response = llm.invoke(messages)

    return response