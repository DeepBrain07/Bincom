# get the colours worn on Monday and put them in a list
monday_colours = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
monday_colours = monday_colours.split(", ")

# get the colours worn on Tuesday and put them in a list
tuesday_colours = "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE"
tuesday_colours = tuesday_colours.split(", ")

# get the colours worn on Wednesday and put them in a list
wednesday_colours = "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE"
wednesday_colours = wednesday_colours.split(", ")

# get the colours worn on Thursday and put them in a list
thursday_colours = "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN"
thursday_colours = thursday_colours.split(", ")

# get the colours worn on Friday and put them in a list
friday_colours = "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
friday_colours = friday_colours.split(", ")

# create a dict with day of the week as the key and list of colours worn on that day as value
days = {"monday": monday_colours, "tuesday": tuesday_colours, "wednesday": wednesday_colours, "thursday": thursday_colours, "friday": friday_colours}

colours = {}

# get the number of times a colour was repeated in a day
for d in list(days.keys()):
    for colour in days[d]:
        if colour in list(colours.keys()):
            colours[colour] += 1
        else:
            colours[colour] = 1

# get the most work colour in the week
most_worn = max(colours, key=colours.get)
print(most_worn) 

