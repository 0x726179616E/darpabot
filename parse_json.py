import json
file_path = "proposals.json"

with open(file_path, "r") as f:
    data = json.load(f)

for proposal in data:
    print(proposal["notice_id"], "\n")




