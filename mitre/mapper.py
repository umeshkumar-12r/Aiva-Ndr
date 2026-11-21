from backend.app.models.hypothesis import Hypothesis
from correlation.correlated_activity import CorrelatedActivity
from mitre.technique import MitreTechnique


def map_mitre_techniques(
    hypothesis: Hypothesis,
    activity: CorrelatedActivity,
) -> list[MitreTechnique]:

    techniques = []

    event_types = set(activity.event_types)

    # ICMP/network discovery-style activity
    if "connection" in event_types:

        techniques.append(
            MitreTechnique(
                technique_id="T1016",
                name="System Network Configuration Discovery",
                tactic="Discovery",
                description=(
                    "Potential network-related discovery activity "
                    "observed through network telemetry."
                ),
                confidence=0.20,
            )
        )

    return techniques
