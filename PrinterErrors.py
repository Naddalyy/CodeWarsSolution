def printer_error(s):
    errors = 0
    for colour in s:
        if colour > "m":
            errors += 1
    
    return "{}/{}".format(errors, len(s))

s ="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
assert printer_error(s) == "3/56"
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
assert printer_error(s) == "6/60"
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
assert printer_error(s) == "11/65"