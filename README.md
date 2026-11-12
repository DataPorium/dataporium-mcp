# DataPorium MCP server: financial, economic and housing data for Claude, ChatGPT, Cursor and AI agents

DataPorium runs a remote [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server with 46 tools that read US investment data: stocks and company financials, ETFs, crypto, forex and commodities, Congress stock trades, layoffs, the US economy, banks, hospitals, elections, and housing down to the ZIP code. Connect it once, then ask your AI assistant in plain language. There is nothing to install.

```
https://mcp.dataporium.io/mcp
```

| | |
|---|---|
| Transport | Streamable HTTP |
| Authentication | Your DataPorium API key |
| Health check | <https://mcp.dataporium.io/health> |
| Tools | 46 |

The tools read the same data as the website and the [REST API](https://dataporium.tech/api-docs). This repository holds the setup for each app; the official setup page is <https://dataporium.tech/mcp>. If the two ever differ, the website is right.

## Your API key

Every call uses your own API key, so your plan limits apply exactly as they do for the REST API. MCP access is included with the Premium plan; see [pricing](https://dataporium.tech/pricing). Your API key is in your account settings once you subscribe.

The server accepts the key in three ways:

| Way | Example |
|---|---|
| `Authorization` header | `Authorization: Bearer YOUR_API_KEY` |
| `X-API-Key` header | `X-API-Key: YOUR_API_KEY` |
| In the address, for apps that only accept a URL | `https://mcp.dataporium.io/mcp?apikey=YOUR_API_KEY` |

## Setup

### Claude (web, desktop and mobile)

Custom connectors need a paid Claude plan; on Team and Enterprise plans an owner adds the connector for the organization.

1. Open **Settings**, then **Connectors**, then **Add custom connector**.
2. Name: `Dataporium`. Remote MCP server URL: `https://mcp.dataporium.io/mcp?apikey=YOUR_API_KEY`.
3. Click **Add**. In a chat, open the tools menu and turn Dataporium on.

### ChatGPT

ChatGPT Plus, Pro, Business and Enterprise support custom MCP connectors through Developer mode.

1. Open **Settings**, then **Apps & Connectors**, then **Advanced settings**, and turn on **Developer mode**.
2. Choose **Create**. Name: `Dataporium`. MCP server URL: `https://mcp.dataporium.io/mcp?apikey=YOUR_API_KEY`. Authentication: No authentication. Confirm that you trust the connector.
3. In a new chat, open the tools menu, choose Developer mode and enable the Dataporium connector.

### Claude Code

```bash
claude mcp add --transport http dataporium https://mcp.dataporium.io/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

Start Claude Code and type `/mcp` to check the connection. Also in [configs/claude-code.sh](configs/claude-code.sh).

### Cursor, VS Code and Windsurf

Open the MCP settings of the editor (Cursor: **Settings**, then **MCP**, then **Add new global MCP server**; VS Code: the `.vscode/mcp.json` file or the **MCP: Add Server** command) and paste [configs/mcp.json](configs/mcp.json):

```json
{
  "mcpServers": {
    "dataporium": {
      "url": "https://mcp.dataporium.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

### Gemini CLI

Add [configs/gemini-settings.json](configs/gemini-settings.json) to `~/.gemini/settings.json`, start Gemini CLI and type `/mcp`. The Gemini web and mobile apps do not accept custom MCP servers yet.

```json
{
  "mcpServers": {
    "dataporium": {
      "httpUrl": "https://mcp.dataporium.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" }
    }
  }
}
```

### Grok (xAI API)

Add a tool of type `mcp` to your xAI API request ([configs/xai-tools.py](configs/xai-tools.py)). The Grok consumer apps do not accept custom MCP servers yet.

```python
tools = [{
    "type": "mcp",
    "server_label": "dataporium",
    "server_url": "https://mcp.dataporium.io/mcp?apikey=YOUR_API_KEY",
}]
```

### Other MCP apps

Any client that supports remote servers over Streamable HTTP works with the server URL and one of the three key options above. Apps that can only start a local server can use the `mcp-remote` bridge as the server command ([configs/mcp-remote.sh](configs/mcp-remote.sh)):

```bash
npx mcp-remote https://mcp.dataporium.io/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

## The 46 tools

| Area | Tools |
|---|---|
| Find a company | `search_symbols` (tickers, names and CIK numbers) |
| Companies and stocks | `get_company_profile`, `get_company_logo`, `get_stock_prices` (stocks, ETFs, indexes and crypto), `get_financial_statements` (income statement, balance sheet, cash flow), `get_business_segments` (revenue by segment, product and region), `get_sec_filings`, `get_company_documents` (investor presentations and press releases), `get_earnings_transcripts`, `get_insider_activity`, `get_shareholders`, `get_short_interest`, `get_options_chain`, `get_ma_transactions`, `get_patents`, `get_industry_classification`, `get_social_media` (X, LinkedIn and Glassdoor data of a company), `get_stock_news` |
| Government and politics | `get_politician_trades` (stock trades reported by members of Congress), `get_government_activity` (federal contracts and lobbying), `get_election_results` |
| Markets | `get_market_news`, `get_market_movers`, `get_sector_industry_performance`, `get_calendar` (earnings, splits, IPOs and economic events), `get_exchange_schedule`, `get_commodity_prices`, `get_fx_rates`, `get_futures_positioning` |
| Economy and energy | `get_economic_metrics` (GDP, inflation, jobs, Treasury yields, Fed decisions, trade, layoffs), `get_energy_data`, `get_healthcare_market` |
| Real estate | `search_properties` (homes for sale, pending, for rent, sold or off the market), `get_property` (one home in full by address or ID), `search_housing_areas` (rank states, counties, metros, cities and ZIP codes), `get_housing_area_insights` (one area in full: market, property tax, crime, demographics, climate) |
| Industries | `get_bank_data` (banks and credit unions), `get_recalls` (vehicle and consumer product recalls), `get_airline_data`, `get_salaries` (pay offered in work-visa filings), `get_healthcare_provider`, `search_healthcare_providers` (hospitals, health systems and doctors) |
| Research screeners | `screen_stocks` (rank about 45,000 companies on dozens of metrics), `screen_ma_deals`, `describe_screen_fields` (fields and typical ranges for the screeners) |
| Help | `list_filters` (every filter a tool accepts) |

## Example questions

- Find profitable US stocks with a forward P/E below 15, revenue growth above 10% and insider buying, then compare the top five.
- What did Nvidia report last quarter, and how does its valuation compare with the sector?
- Which US cities have a gross rent yield above 7% with a growing population and low crime?
- Show homes in Austin, Texas under $600,000 that had a price cut in the last 7 days.
- How have mortgage rates and home values in Phoenix changed over the past year?
- What does the US Treasury yield curve look like today, compared with a year ago?
- Which companies filed layoff notices in California in the last 30 days, and how many workers were affected?
- Which hospitals in Texas have the most beds, and which health systems own them?

## Limits and safety

- 600 API requests per minute, and 150 tool calls per hour per key through MCP.
- Answers are capped at 100 rows per call.
- Treat a server address that contains your API key like a password. Do not share screenshots of it.
- If a key leaks, create a new key in your account settings. The old one stops working.

## Building your own app instead?

Use the same key with the REST API:

- Python: [dataporium-python](https://github.com/DataPorium/dataporium-python)
- JavaScript and TypeScript: [dataporium-js](https://github.com/DataPorium/dataporium-js)
- curl, R, Google Sheets and Excel: [financial-data-api](https://github.com/DataPorium/financial-data-api)
- API documentation: <https://dataporium.tech/api-docs>

## License and disclaimer

The configuration files in this repository are released under the [MIT License](LICENSE). Use of the server and its data is governed by the DataPorium [Terms of Use](https://dataporium.tech/terms-of-use). Data is for information only and is not investment advice.
