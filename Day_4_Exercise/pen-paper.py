## Ceasars Shift by 5 character (a -> f)
characters = str("abcdef0123456789")
private_key = str("1062f7a3410b4a29fa7435c57c14d521eb8169875f280e1bf2bc39f172514059")
new_characters = []
encrypt_priv_key = ""
c = 0
for i in range(len(private_key)):
    for j in range(len(characters)):
        if private_key[i] == characters[j]:
            c = (j + 5) % len(characters) 
            break

    new_characters.append(characters[c])

for x in new_characters: 
    encrypt_priv_key += x


print("Input = {}\nOutput = {}".format("0x" + private_key,"0x" + encrypt_priv_key))


