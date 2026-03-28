# tips.py
import random

tips = [
    "Stay hydrated throughout your cycle.",
    "Iron-rich foods can help with energy.",
    "Gentle exercise may reduce cramps.",
    "Tracking your mood can improve self-awareness.",
    "Adequate sleep supports hormonal balance.",
    "Warm compresses may ease discomfort.",
    "Include leafy greens for better nutrition."
]

def get_random_tip() -> str:
    """
    Returns a random tip from the list.
    """
    return random.choice(tips)