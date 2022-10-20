
monthConversions = {
    "jan": "january",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Set": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Set"])

print(monthConversions.get("lhfdggh"))

print(monthConversions.get("lhfdggh", "Nor a valid key"))