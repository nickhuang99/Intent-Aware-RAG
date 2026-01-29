# demo/logic_gate_demo.py

def five_w_one_h_logic_gate(query_intent, document_data):
    """
    Simulates the Logic Gate that prevents hallucinations 
    by enforcing slot-based filtering.
    """
    print(f"DEBUG: Processing Intent -> {query_intent['target_slot']}")
    
    # Logic: If user is looking for 'When', the document MUST have a date
    if query_intent['target_slot'] == "When":
        if not document_data.get("when"):
            return "❌ REJECTED: Semantic match found, but logical 'When' slot is missing."
        return f"✅ ACCEPTED: Found date {document_data['when']}"

# Scenario: User asks "When did the deal happen?"
query = {"target_slot": "When"}
doc_semantic_match = {"text": "The CEO signed the deal in Paris.", "when": None}

print(five_w_one_h_logic_gate(query, doc_semantic_match))
