a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# 1. wife는 a에 없음->wife 출력 x
# 2. python이 a에 있고, you 또한 a에 있음-> python 출력 x
# 3. shirt가 a에 없음-> shirt 출력
# 4. need가 a에 없음-> need 출력 x
# 5. 위 넷 중 하나가 해당하므로 none 출력 x
