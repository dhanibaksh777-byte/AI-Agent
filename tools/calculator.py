import math
def calculate(expressions : str):
    result = eval(expressions,vars(math))
    return result


calculator_tool = {
    "type" : "function",
    "function" : {
        "name" : "calculate",
        "description" : "calculates the expressions",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "expressions" : {
                    "type" : "string",
                    "description" : "the mathematical expression to evaluate e.g 2+2, sqrt(16)"

                }
                
            },
            "required" : ["expressions"]
        }
    }
}

