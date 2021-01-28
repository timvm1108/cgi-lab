#!/usr/bin/env python3
import json
import os


# Print environment variable as plain text
# print("Content-Type: text/plain")
# print()
# print(os.environ)

# Print environment variables as JSON
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

# Print POST results
print("Content-Type: text/html")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")