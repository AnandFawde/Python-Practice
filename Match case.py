def weekday(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "IT HELLL"
        case "Saturday" | "Sanday":
            return "HELL'S OVER"
        
print(weekday("Sanday")) 
print(weekday("Monday"))