import uuid

def get_pc_id():
    return hex(uuid.getnode())