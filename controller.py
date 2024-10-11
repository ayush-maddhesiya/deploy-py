def you_name():
  name = "Ayush"
  return f'Hello {name}'

def you_name2():
    incoming_data = request.json
    if "name" not in incoming_data:
        return jsonify({"error": "Missing field", "message": "The 'name' field is required."}), 400
    
    name = incoming_data["name"]
    return f'Hello {name}! How are you?'

def you_name3():
    incoming_data = request.json
    if "name" not in incoming_data:
        return jsonify({"error": "Missing field", "message": "The 'name' field is required."}), 400

    name = incoming_data["name"]
    return f'Hello {name}! How are you doing today?'
