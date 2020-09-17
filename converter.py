# Application title and description
print("\n"
      " *******             **       ********       ********\n"
      "/**////**           /**      /**/////       /**/////\n"
      "/**    /**          /**      /**            /**\n"
      "/**    /**          /**      /*******       /*******\n"
      "/**    /**          /**      /**////        /**////\n"
      "/**    **       **  /**      /**            /**\n"
      "/*******       //*****       /**            /**\n"
      "///////         /////        //             //\n"
      "\n"
      "---------------- Unit Converter v.1 -----------------\n"
      "\n"
      "This program is an open source unit converter writen in Python 3. This "
      "program "
      "converts the following quantities:\n"
      "- Temperature\n"
      "\n"
      "Please see the README for the full list of units and their respective "
      "naming conventions.\n")

# List of units that can be converted
list_of_units = ("degC", "degF", "K")

# While loop for the unit_in variable input
while True:
    unit_in = input("Input the unit to be converted: ")
    if unit_in.strip() in list_of_units:
        # .strip() removes unnecessary white space from variable
        break
    print("Refer to README for list of valid inputs.")

# While loop for the unit_out variable input
while True:
    unit_out = input("Input the unit which you would like to convert "
                     + unit_in + " to: ")
    if unit_out.strip() not in list_of_units:
        # Tells user to refer to README if unit not available
        print("Refer to README for list of valid inputs.")
    elif unit_out.strip() == unit_in.strip():
        # Ensures the unit is not the same as the input unit
        print("You don't need to convert [" + unit_in + "] to itself!")
    elif unit_out.strip() in list_of_units:
        break

# num_in variable input
num_in = float(input("Input the value in " + unit_in + " to convert: "))

# Temperature conversions
# Convert to [degC]
if unit_in == "degF" and unit_out == "degC":
    num_out = (float(num_in) - 32) / 1.8

if unit_in == "K" and unit_out == "degC":
    num_out = float(num_in) - 273

# Convert to [degF]
if unit_in == "degC" and unit_out == "degF":
    num_out = float(num_in) * 1.8 + 32

if unit_in == "K" and unit_out == "degF":
    num_out = (float(num_in) + 273) * 1.8 + 32

# Convert to [k]
if unit_in == "degC" and unit_out == "K":
    num_out = float(num_in) + 273

if unit_in == "degF" and unit_out == "K":
    num_out = (float(num_in) / 1.8) - 32 - 273

# Print answer
print("\n"
      + str(num_in) + "[" + str(unit_in) + "]" + " = " + str(num_out) + "[" +
      str(unit_out) + "]")
