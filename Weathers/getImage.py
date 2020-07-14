def getImage(code: int) -> str:
    if code >= 200 and code <= 232:
        return 'thunder.jpg'
    elif code >= 300 and code <= 321:
        return 'Drizzle.jpg'
    elif code >= 500 and code <= 531:
        return 'rain.jpg'
    elif code >= 600 and code <= 622:
        return 'snow.jpg'
    elif code >= 701 and code <= 781:
        return 'mist.jpg'
    elif code == 800:
        return 'sunny.jpg'
    else:
        return 'cloud.jpg'
