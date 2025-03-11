def success_response(data, message="Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(error_message, status_code=400):
    return {
        "status": "error",
        "message": error_message
    }, status_code

