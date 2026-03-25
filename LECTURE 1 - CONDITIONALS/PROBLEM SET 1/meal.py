

#CHALLENGE: FORMAT AM/PM, CASE INSENSITIVE, NO EXTRA SPACES.

def main():
    #fare time = time.lower().strip() dentro def convert se si pensa di riutilizzare il codice convert
    time = input("What time is it? ").lower().strip()
    result = convert(time)
    
    if result >= 7 and result <= 8:
        print("breakfast time")
    elif result >= 12 and result <= 13:
        print("lunch time")
    elif result >= 18 and result < 19:
        print("dinner time")

def convert(time):
    # Se c'è uno spazio in time, separiamo l'orario dal suffisso AM/PM
    if " " in time:
        # Dividiamo in "8:30" e "p.m."
        time_part, format = time.split(" ")
    else:
        time_part = time
        format = None

    # Ora lavoriamo solo sulla parte "8:30"
    hours, minutes = time_part.split(":")
    h = float(hours)
    m = float(minutes)
    result = h + (m / 60)

    # Applichiamo i correttivi per il formato 12 ore
    if format == "p.m." and h != 12:
        return result + 12
    elif format == "a.m." and h == 12:
        return 0.0 #Eccezione di Mezzanotte
    
    return result
    

if __name__ == "__main__":
    main()