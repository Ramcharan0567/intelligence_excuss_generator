from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

def generate_excuse(scenario, urgency, style, proof):
    # Build prompt
    prompt = f"Q: Provide an excuse for the scenario '{scenario}' with urgency '{urgency}', style '{style}', and need fake proof: {proof}.\nA:"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.9,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only the generated part after "A:"
    if "A:" in response:
        return response.split("A:")[-1].strip()
    return response.strip()
