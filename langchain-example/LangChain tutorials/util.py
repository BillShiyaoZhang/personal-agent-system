import os
from langchain_community.llms.mlx_pipeline import MLXPipeline
from langchain_openai import ChatOpenAI


def setLangSmith():
    """
    Set the environment variables for LangSmith
    """

    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = "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"


def getChatMLX():
    """
    Get the ChatMLX model.
    Returns:
        model (ChatMLX): The initialized ChatMLX model with the specified LLM pipeline.
    """

    llm = MLXPipeline.from_model_id(
        "mlx-community/Qwen2.5-32B-Instruct-4bit",
        pipeline_kwargs={"max_tokens": 4000, "temp": 0.1},
    )

    from langchain_community.chat_models.mlx import ChatMLX
    model = ChatMLX(llm=llm)
    return model


def getOpenAIMLX():
    model = ChatOpenAI(model="mlx-community/Qwen2.5-32B-Instruct-4bit", max_tokens=4000,
                  base_url="http://localhost:10240/v1",
                  api_key="not-needed")