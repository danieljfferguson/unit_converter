
# Application title
print("""
 *******             **       ********       ********                         
/**////**           /**      /**/////       /**/////                          
/**    /**          /**      /**            /**                               
/**    /**          /**      /*******       /*******                          
/**    /**          /**      /**////        /**////                           
/**    **       **  /**      /**            /**                               
/*******       //*****       /**            /**                               
///////         /////        //             // 

--- Unit Converter v.1 ---""")

print("""
This program is an open source unit converter writte in Python 3. At the
present time, only the conversion of S.I. units is possible. This program
converts the following quantities:
- Temperature

Please see the README for the full list of units and their respective naming
conventions.
""")

list_of_units = ("degC", "degF", "K")

while True:
    unit_in = input("Input the unit to be converted: ")
    if unit_in.strip() in list_of_units:
        break
    print("Refer to README for list of valid inputs.")

while True:
    unit_out = input("Input the unit which you would like to convert "
                     + unit_in + " to: ")
    if unit_out.strip() not in list_of_units:
        print("Refer to README for list of valid inputs.")
    elif unit_out.strip() in list_of_units:
        break

num_in = int(input("Input the value in " + unit_in + " to convert: "))

if unit_in == unit_out:
    num_out = num_in

# Temperature conversions
# Convert to [degC]
if unit_in == "degF" and unit_out == "degC":
    num_out = (float(num_in)-32)/1.8

if unit_in == "K" and unit_out == "degC":
    num_out = float(num_in)-273

# Convert to [degF]
if unit_in == "degC" and unit_out == "degF":
    num_out = float(num_in)*1.8 + 32

if unit_in == "K" and unit_out == "degF":
    num_out = (float(num_in)+273)*1.8 + 32

# Convert to [k]
if unit_in == "degC" and unit_out == "K":
    num_out = float(num_in)+273

if unit_in == "degF" and unit_out == "K":
    num_out = (float(num_in)/1.8)-32-273

# Print answer
print('''
''' + str(num_in) + "[" + str(unit_in) + "]" + " = " + str(num_out) + "[" 
+ str(unit_out) + "]")
