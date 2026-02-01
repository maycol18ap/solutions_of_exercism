def response(hey_bob):
    new=hey_bob.strip()
    if new.isspace() or new=="":
        return "Fine. Be that way!"
    elif new.isupper() and new.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif new[-1]=="?":
        return "Sure."
    elif new.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

        
