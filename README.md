# Things I learned

- FastAPI uses {} instead of <> for path parameters.
- The curl command works on Windows. Sample:

```bash
curl -X "GET" "http://127.0.0.1:8000/property/1" -H "accept: application/json"
```

And to request the headers, use -I:

```bash
curl -X "GET" -I "http://127.0.0.1:8000/property/1" -H "accept: application/json"
```

NOTE: On Windows, single quotes fail. Use always double quotes.

- How you sort your functions in your files, matters. 
- Path parameters are those specified with a slash (/), and query parameters those specified after the question mark (?) and separated with the @ symbol. In the second case, key and value are needed.

- Nice definition of metadata: metadata is data about data.
