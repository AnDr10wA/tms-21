
hours = 1
seconds = 30
minutes = 45


while True:

    if seconds>0:
        seconds -= 1
        print(hours, minutes,seconds)
    else:
        if minutes>0:
            minutes -= 1
            seconds +=60
        else:
            if hours > 0:
                hours -= 1
                minutes +=60
            else:
                break





# class Mytime:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def (self):








