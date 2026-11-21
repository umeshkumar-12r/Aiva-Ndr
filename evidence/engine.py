from backend.app.models.evidence import Evidence
from backend.app.models.hypothesis import Hypothesis
from correlation.correlated_activity import CorrelatedActivity


def evaluate_hypothesis(
    hypothesis: Hypothesis,
    activity: CorrelatedActivity,
) -> list[Evidence]:

    evidence = []

    # -------------------------
    # Supporting evidence
    # -------------------------

    if "suricata" in activity.source_tools:

        evidence.append(
            Evidence(
                evidence_id=f"{hypothesis.hypothesis_id}-support-001",

                hypothesis_id=hypothesis.hypothesis_id,

                type="supporting",

                description=(
                    "Suricata generated a security alert "
                    "within the correlated activity."
                ),

                source_events=activity.event_ids,

                strength=0.6,
            )
        )

    if activity.event_count >= 3:

        evidence.append(
            Evidence(
                evidence_id=f"{hypothesis.hypothesis_id}-support-002",

                hypothesis_id=hypothesis.hypothesis_id,

                type="supporting",

                description=(
                    "Multiple related network events were "
                    "observed within the correlation window."
                ),

                source_events=activity.event_ids,

                strength=0.3,
            )
        )

    # -------------------------
    # Missing evidence
    # -------------------------

    evidence.append(
        Evidence(
            evidence_id=f"{hypothesis.hypothesis_id}-missing-001",

            hypothesis_id=hypothesis.hypothesis_id,

            type="missing",

            description=(
                "No evidence of successful compromise "
                "or post-compromise activity has been "
                "observed yet."
            ),

            source_events=[],

            strength=0.0,
        )
    )

    return evidence
