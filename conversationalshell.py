import time
from typing import Dict, List

class ConversationalShell:
    """
    Interface layer for real-time natural language interaction with Builder Core.
    Routes incoming messages to relevant agents and logs context.
    """
    def __init__(self):
        self.history: List[Dict] = []
        self.agent_bindings = {
            "optimize": "OptimizePriorities",
            "status": "ModuleHealthDashboard",
            "backup": "ResilientBackupProtocol",
            "funds": "TreasuryEngine",
            "flow": "FlowEthic"
        }

    def receive_message(self, user_input: str) -> str:
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S')
        self.history.append({"time": timestamp, "user": user_input})
        response = self.route_to_agent(user_input)
        self.history.append({"time": timestamp, "system": response})
        return response

    def route_to_agent(self, message: str) -> str:
        for keyword, agent in self.agent_bindings.items():
            if keyword in message.lower():
                return f"Routing to {agent}: (Simulated response)"
        return "I'm listening. Please clarify your intent or ask anything."