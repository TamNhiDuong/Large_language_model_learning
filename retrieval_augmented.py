import os
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "Your secret HuggingFace API key"

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'microsoft/Phi-3-mini-4k-instruct',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}

app = App.from_config(config=config)
app.add("https://en.wikipedia.org/wiki/Jean_Sibelius")

response = app.query("When was Jean Sibelius born?")
print(response)