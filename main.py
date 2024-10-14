meme_dict = {
            "DECLARE": "Duyurmak",
            "INCLUDING": "İÇERMEK",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
   print("Böyle bir kelime bulunamadı!")
