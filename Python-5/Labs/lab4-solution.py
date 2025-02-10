# Lab 4:
# def <function name> (arguments):
#     <code>
def format_message(msg, /, *, uppercase=False):
    # if uppercase:
    #     return msg.upper()
    # else:
    #     return msg
    return msg.upper() if uppercase else msg


print(format_message("hello"))  # Output: "hello"
print(format_message("hello", uppercase=True))  # Output: "HELLO"