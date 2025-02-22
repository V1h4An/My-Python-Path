# a collection of {key:value} pairs.Basically Hashmap.

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "France":"Paris",
            "Spain":"Madrid"}

#print(capitals.get("Japan"))
#capitals.update({"Japan":"Tokyo"})
#capitals.pop("USA")
#capitals.clear()
#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
#print(items)

for key, value in capitals.items():
    print(f"{key} : {value}")