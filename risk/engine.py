from backend.app.models.hypothesis import Hypothesis
from backend.app.models.evidence import Evidence


def calculate_confidence(
    hypothesis: Hypothesis,
    evidence: list[Evidence],
) -> float:

    score = hypothesis.confidence

    for item in evidence:

        if item.type == "supporting":
            score += item.strength * 0.5

        elif item.type == "contradicting":
            score -= item.strength * 0.5

    return max(0.0, min(score, 1.0))


def calculate_risk(
    evidence: list[Evidence],
) -> str:

    supporting_score = 0.0

    for item in evidence:

        if item.type == "supporting":
            supporting_score += item.strength

    if supporting_score >= 0.8:
        return "HIGH"

    elif supporting_score >= 0.4:
        return "MEDIUM"

    return "LOW"


def calculate_assessment(
    hypothesis: Hypothesis,
    evidence: list[Evidence],
) -> dict:

    confidence = calculate_confidence(
        hypothesis,
        evidence
    )

    risk = calculate_risk(evidence)

    return {
        "hypothesis_id": hypothesis.hypothesis_id,
        "risk": risk,
        "confidence": round(confidence, 2),
    }
