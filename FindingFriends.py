def friend(x):
    friends = []                        
    for name in x:
        if len(name) == 4:
            friends.append(name)
            
    return friends

assert friend(["Ryan", "Kieran", "Mark",]) == ["Ryan", "Mark"]
assert friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"]
assert friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"]