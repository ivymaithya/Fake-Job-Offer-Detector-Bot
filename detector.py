import re

# Dictionary of suspicious phrases and their associated risk weights
SUSPICIOUS_PHRASES = {
    r"\bregistration fee\b": {
        "weight": 40,
        "reason": "Requests a payment or registration fee before hiring."
    },
    r"\bpay before interview\b": {
        "weight": 50,
        "reason": "Demands payment prior to an interview, a severe red flag."
    },
    r"\bguaranteed employment\b": {
        "weight": 30,
        "reason": "Promises guaranteed employment, which legitimate companies rarely do."
    },
    r"\bimmediate hiring\b": {
        "weight": 15,
        "reason": "Uses urgency ('immediate hiring') to pressure applicants."
    },
    r"\bno experience needed\b": {
        "weight": 10,
        "reason": "Claims 'no experience needed' for potentially high-paying roles."
    },
    r"\bwork from home and earn millions\b": {
        "weight": 45,
        "reason": "Makes unrealistic, exaggerated salary promises for work-from-home jobs."
    },
    r"\blimited slots\b": {
        "weight": 20,
        "reason": "Uses artificial scarcity ('limited slots') to force quick action."
    },
    r"\burgent recruitment\b": {
        "weight": 15,
        "reason": "Uses urgency tactics to prevent careful consideration."
    },
    r"\bsend money\b": {
        "weight": 50,
        "reason": "Explicitly asks the applicant to send money."
    },
    r"\bmpesa payment\b": {
        "weight": 45,
        "reason": "Requests money via mobile money (M-Pesa) for job processing."
    },
    r"\bprocessing fee\b": {
        "weight": 40,
        "reason": "Asks for a processing fee, which is a common scam tactic."
    },
    r"\btraining fee\b": {
        "weight": 40,
        "reason": "Charges the applicant for required training before starting."
    },
    r"\bselected automatically\b": {
        "weight": 35,
        "reason": "Claims you were 'selected automatically' without a proper application."
    },
    r"\bguaranteed salary\b": {
        "weight": 20,
        "reason": "Promises a 'guaranteed salary' without assessing qualifications."
    },
    r"\beasy money\b": {
        "weight": 25,
        "reason": "Promotes the job as 'easy money', appealing to desperation."
    }
}

def analyze_job_text(text):
    """
    Analyzes the provided job description text against known red flags.
    Returns a dictionary containing the score, classification, and list of reasons.
    """
    if not text or not text.strip():
        return {
            "score": 0,
            "classification": "Safe",
            "reasons": ["No text provided for analysis."]
        }
        
    score = 0
    reasons_set = set()
    text_lower = text.lower()

    # Check for matches
    for pattern, info in SUSPICIOUS_PHRASES.items():
        if re.search(pattern, text_lower):
            score += info["weight"]
            reasons_set.add(info["reason"])
            
    # Additional simple heuristics
    if "!!!" in text:
        score += 5
        reasons_set.add("Uses excessive exclamation marks (poor professionalism).")
        
    if text.isupper():
        score += 15
        reasons_set.add("Text is entirely in ALL CAPS, often used in spam/scams.")

    # Cap the score at 100
    score = min(score, 100)

    # Classification logic
    if score <= 30:
        classification = "Safe"
    elif score <= 60:
        classification = "Suspicious"
    else:
        classification = "Likely Scam"

    # If score is > 0 but no specific text phrase matched (e.g. only capitalization)
    if score > 0 and len(reasons_set) == 0:
         reasons_set.add("Contains general suspicious formatting or urgency indicators.")
         
    # Ensure there's a reason if safe
    if score == 0:
        reasons_set.add("No obvious red flags detected in the text.")

    return {
        "score": score,
        "classification": classification,
        "reasons": list(reasons_set)
    }
