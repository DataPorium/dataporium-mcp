# Grok through the xAI API: add DataPorium as a remote MCP tool in your request
# (Responses API or the xAI SDK), replacing YOUR_API_KEY.
tools = [{
    "type": "mcp",
    "server_label": "dataporium",
    "server_url": "https://mcp.dataporium.io/mcp?apikey=YOUR_API_KEY",
}]
