user = {
    "name": "Talha",
    "age": 20,
    "email": "Talha@gmail.com",
    "is_verified": True
}

print(user)
print(user["name"])
print(user.get("password"))

user["age"] = 21
print(user)

user["job"] = "Student"
print(user)
