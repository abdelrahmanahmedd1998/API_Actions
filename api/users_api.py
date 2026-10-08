class UsersApi:
    def __init__(self,request_context):
        self.request_context=request_context

    def get_user(self,user_id:int):
        return self.request_context.get(f"/api/users/{user_id}")    

    def list_users(self,page:int):
        return self.request_context.get(f"/api/users",params={"page": page})

    def create_user(self):
        return self.request_context.post("/api/users")

    def update_user(self,user_id:int):
        return self.request_context.put(f"/api/users/{user_id}")

    def delete_user(self,user_id:int):
        return self.request_context.delete(f"/api/users/{user_id}")