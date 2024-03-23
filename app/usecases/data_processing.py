from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData


def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    try:
        z_value = agent_data.accelerometer.z
        road_state = classify_road_state(z_value)
        return ProcessedAgentData(road_state=road_state, agent_data=agent_data)
    except Exception as e:
        print(f"An error occurred while processing agent data: {e}")


def classify_road_state(z_coordinate: float) -> str:
    if 9562.259489 <= z_coordinate <= 18620.4738:
        road_state = "В межах норми"
    else:
        road_state = "Аномалія"
    return road_state
