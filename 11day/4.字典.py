
id_card = {"name":"贾","age":20,"民族":"汉"}

#id_card.pop("name")
id_card["name"] = "贾"

id_card["height"] = 175


id_card.setdefault("qq",74215)

id_card.setdefault("phone",4102545)

id_card2 = {"朋友.":"宋","朋友,":"春","朋友'":"芳"}
id_card.update(id_card2)

id_card.pop("name")
id_card.pop("age")
id_card.pop("民族")
id_card.pop("qq")
id_card.pop("phone")
id_card.pop("height")





print(id_card)

for k in id_card:
    print("%s:%s"%(k,id_card[k]))


string = "'hello song"
for i in string:
    print(i,end="")

print("")


