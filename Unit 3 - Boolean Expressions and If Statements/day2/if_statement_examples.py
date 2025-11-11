# 1) Temperature classifier (°C):
#    Print one of: cold (<0), cool (0–15), warm (16–25), hot (>25) based on temp_c.
temp_c = 23
if temp_c < 0:
    print("cold")
elif temp_c < 15:
    print("cool")
elif temp_c < 25:
    print("warm")
else:
    print("hot")


# 2) Letter grades:
#    Print A (90+), B (80–89), C (70–79), D (60–69), or F (<60) based on percent.

# 3) Password strength by length:
#    Print weak (<8), ok (8–11), or strong (12+) using len(password).

# 4) Greeting by hour (0–23):
#    Print Good morning (5–11), Good afternoon (12–16), Good evening (17–21), or Good night (other).

# 5) Course code (strings):
#    If it begins with "ics" (case-insensitive) print "Computer Studies".
#    Elif it ends with "py" print "Python file".
#    Else print "Unknown".
#    (Use only lower(), len(), and slicing.)

# 6) Ticket price category by age:
#    Print child (0–12), student (13–17), adult (18–64), or senior (65+).

# 7) Shipping fee by weight (kg):
#    Print light (<=1.0), standard (<=5.0), or heavy (>5.0).

# 8) Honour roll:
#    If gpa >= 3.7 and attendance >= 95, print "Honour Roll".
#    Elif gpa >= 3.0, print "Good Standing".
#    Else print "Keep Going".

# 9) File type by extension (strings):
#    If filename ends with ".py" -> print "Python".
#    Elif it ends with ".txt" -> print "Text".
#    Else -> "Other".
#    (Use only lower() and slicing.)

# 10) Team placement (ints/floats):
#    If age < 13 -> "U13".
#    Elif 13–14 and height_m >= 1.65 -> "U15-Tall".
#    Elif 13–14 and height_m < 1.65 -> "U15".
#    Else -> "U17+".

# Challenge (optional):
#    Rewrite #8 using a nested if inside the gpa >= 3.7 branch (check attendance inside).
