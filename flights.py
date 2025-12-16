from mcp.server.fastmcp import FastMCP
import os
import json
mcp = FastMCP(name="Flights")

FLIGHTS_PATH = os.path.join(os.path.dirname(__file__), "flights.json")

@mcp.resource(uri="flights://today")
def _load_flights(): 
    with open(FLIGHTS_PATH, "r", encoding="utf-8") as f: 
        return json.load(f).get("flights", []) 
    

@mcp.tool()
def findflight(x : str) -> str:
    """ 
    Trouve un vol par son numéro. 
    Exemple d'appel : findflight("AF123") 
    """ 
    import json 
    flights = _load_flights()
    for flight in flights: 
        if flight.get("flight_number").upper() == x.upper(): 
            return f"flight {flight['flight_number']} from {flight['airline']} to {flight['arrival_city']} departs at {flight['departure_time']} and arrives at {flight['arrival_time']}."
    return "Vol non trouvé."


@mcp.tool()
def filter_by_destination(city: str) -> list:
    """
    Retourne tous les vols dont la ville d’arrivée correspond à 'city'.
    """
    flights = _load_flights()
    return [
        f for f in flights
        if f.get("arrival_city", "").lower() == city.lower()
    ]
@mcp.tool()
def flights_by_status(status: str) -> list:
    """
    Filtre les vols selon leur statut.
    Exemples : "delayed", "on-time", "cancelled"
    """
    flights = _load_flights()
    return [
        f for f in flights
        if f.get("status", "").lower() == status.lower()
    ]

@mcp.tool()
def flights_by_airline(airline: str) -> list:
    """
    Retourne tous les vols opérés par une compagnie donnée.
    Exemple : flights_by_airline ("British Airways")
    """
    flights = _load_flights()
    return [
        f for f in flights
        if f.get("airline", "").lower() == airline.lower()
    ]


if __name__ == "_main_":
    mcp.run(transport="stdio")