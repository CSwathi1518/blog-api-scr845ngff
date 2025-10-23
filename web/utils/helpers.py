from flask import jsonify

def success_response(data, message='Success', status=200):
    """Standard success response format"""
    return jsonify({
        'success': True,
        'message': message,
        'data': data
    }), status

def error_response(message, errors=None, status=400):
    """Standard error response format"""
    response = {
        'success': False,
        'message': message
    }
    if errors:
        response['errors'] = errors
    return jsonify(response), status