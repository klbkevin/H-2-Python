"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    new = {}
    
    for key, value in result.items():
        if key == "foo":
            new["Foo"] = value.capitalize().replace("k","")
            
    return new
    