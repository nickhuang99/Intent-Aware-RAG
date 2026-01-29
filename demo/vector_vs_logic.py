import numpy as np

# Mock function for Semantic Similarity
def mock_vector_similarity(q, d):
    # In a real world, this is an Embedding Model. 
    # Here we simulate high similarity due to keyword overlap.
    return 0.92 

# Mock 5W1H Structured Data
documents = [
    {
        "id": "doc_001",
        "text": "The project was cancelled by the CEO in June due to budget cuts.",
        "5w1h": {"who": "CEO", "what": "cancelled project", "when": "June", "why": "budget cuts"}
    },
    {
        "id": "doc_002",
        "text": "The CEO is considering the project's future impact.",
        "5w1h": {"who": "CEO", "what": "considering impact", "when": None, "why": None}
    }
]

# Scenario: User asks "WHEN did the CEO cancel the project?"
query = "When did the CEO cancel the project?"

print(f"Query: {query}\n")

# --- TEST 1: TRADITIONAL VECTOR RAG ---
print("--- TEST 1: Traditional Vector RAG ---")
for doc in documents:
    score = mock_vector_similarity(query, doc["text"])
    print(f"Doc ID: {doc['id']} | Similarity Score: {score}")
print("Result: Both docs look identical to a vector engine. It might pick the wrong one.\n")

# --- TEST 2: 5W1H INTENT-AWARE RAG ---
print("--- TEST 2: 5W1H Intent-Aware RAG ---")
intent = "Supplement" # Extracted via QIC
target_slot = "when"  # Extracted via QIC

for doc in documents:
    # Logic: It must match the WHO/WHAT and MUST contain the WHEN
    has_who = "CEO" in doc["5w1h"]["who"]
    has_when = doc["5w1h"]["when"] is not None
    
    if has_who and has_when:
        print(f"✅ Doc ID: {doc['id']} MATCHED (Logic: Knowns found, Unknown slot filled)")
    else:
        print(f"❌ Doc ID: {doc['id']} REJECTED (Logic: Missing the target 'When' slot)")
