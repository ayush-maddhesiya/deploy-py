def you_name():
  incoming_data = request.json
  name = incoming_data["name"]
  return f'Hello {name}'

def you_name2():
  incoming_data = request.json
  name = incoming_data["name"]
  return f'Hello {name}! How are you?'

def you_name3():
  incoming_data = request.json
  name = incoming_data["name"]
  return f'Hello {name}! How are you doing today?'