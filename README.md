# network_from_location

technical test: https://papernest.notion.site/Backend-developer-technical-test-fa0a5fab912e45d4813482d3bcb54224

# **Goal**

Build a small api project that we can request with a textual address request and retrieve 2G/3G/4G network coverage for each operator (if available) in the response.

**Example**

Request:
```
GET: 127.0.0.1:5000/?q=42+rue+papernest+75011+Paris
```
Response:

```json
{
	"orange": {"2G": true, "3G": true, "4G": false}, 
	"SFR": {"2G": true, "3G": true, "4G": true}
}
```

**Install**

```shell
pip install -r requirements.txt
```

**Run**

```shell
cd app/
flask --app network run
```

if you want to use another port

```shell
flask --app network run -p <PORT>
```
