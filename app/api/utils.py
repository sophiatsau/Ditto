# history: record / memory of conversation.
# using an object so that it can be changed between files: logging out = clearing history
"""
[
  {
    "role": "user" or "model",
    "parts": ["text"]
  }
]
"""
history = {"history":[]}