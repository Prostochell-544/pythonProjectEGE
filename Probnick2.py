for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (not (y) and (x == (not (w) or y))):
                    print(w, x, z, y)
