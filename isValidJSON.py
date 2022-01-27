import json

def is_json(jsonCheck):
  try:
      with open(jsonCheck, "r") as read_file:
          data = json.load(read_file)
  except ValueError as e:
    return False
  return True

print(is_json("C:\\Users\\nadezhda.patrusheva\\PycharmProjects\\pythonProject1\\jsonCheck1.json"))