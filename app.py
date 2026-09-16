
import os

import streamlit as st
from dotenv import load_dotenv
from litellm import completion


load_dotenv()

API_KEY = os.getenv("DUKE_AI_API_KEY")
DUKE_AI_BASE_URL = "https://litellm.oit.duke.edu/v1"

st.set_page_config(
    page_title="Explain My Code",
    page_icon="💡",
)

st.title("💡 Explain My Code")
st.write(
    "Paste Python code below and let an LLM explain what it does, "
    "identify potential problems, and suggest improvements."
)

code = st.text_area(
    "Paste your Python code:",
    height=300,
    placeholder="""def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
""",
)

if st.button("Explain Code", type="primary"):

    if not API_KEY:
        st.error("DUKE_AI_API_KEY is not configured.")
        st.stop()

    if not code.strip():
        st.warning("Please paste some code first.")
        st.stop()

    prompt = f"""
You are a helpful programming tutor.

Analyze the following Python code.

Provide your response using these sections:

## What it does
Explain the overall purpose in simple language.

## Step-by-step walkthrough
Explain the important parts of the code in order.

## Potential problems
Identify bugs, edge cases, security concerns, or performance issues.
If there are none, say so.

## Suggestions
Suggest concrete improvements.

## Example
Give a short example showing how the code behaves.

Keep the explanation appropriate for someone learning Python.

Here is the code:

```python
{code}
```
"""

    with st.spinner("Analyzing your code..."):

        try:
            response = completion(
                model="openai/gpt-5.4-nano",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                api_key=API_KEY,
                api_base=DUKE_AI_BASE_URL,
                temperature=0.2,
            )

            explanation = response.choices[0].message.content

            st.markdown("## Explanation")
            st.markdown(explanation)

        except Exception as e:
            st.error(f"An error occurred: {e}")