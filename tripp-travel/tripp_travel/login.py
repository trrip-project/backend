def sayWelcome(name=None):
    message = "Hello user" if name is None else f"Hello {name}"
    return message