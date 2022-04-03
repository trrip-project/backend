def sayWelcome(name=None):
    message = "Hello user1" if name is None else f"Hello {name}"
    return message
