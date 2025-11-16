if __name__ == "__main__":
    import os
    import openai

    client = openai.OpenAI(
        base_url="https://groqproxy.vercel.app/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY")
    )
    
    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input="Tell me why life have no meaning and nothing matter"
    )

    print(response)