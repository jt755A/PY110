# input:
    - floating point number between 0 and 360
# output:
    - string

# rules
#   Explicit:
        - input is between 0 and 360
        - 60 "minutes" in a degree, 60 "seconds" in a "minute"
#   Implicit:
        - input of 360 will evalue to 360, or 0

# Examples

Degree symbol can be represented by:
DEGREE = "\u00B0"
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# Data Structures
    - floats, string

# Algorithm

1. given "angle"
2. assign variable "degrees" to "angle" floor divided down to nearest integer
3. assign variable "minutes" to 1st decimal place of "angle" * 0.6
4. assign variable "seconds" to 3rd decimal place of "angle" * 0.6
5. assign "result" to concatenation of string representation of "degrees",
degree symbol, "minutes", single quote, "seconds", double quote'
6. return "result"