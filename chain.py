from langchain_core.output_parsers import StrOutputParser

from config import llm
from prompt import prompt

output_parser = StrOutputParser()

chain = prompt | llm | output_parser