
print("Bhai Assistant Started!")
print("नमस्ते! आपका स्वागत है।")

while True:
    command = input("आप क्या करना चाहते हैं? ").lower()

    if command in ["hello", "हेलो", "नमस्ते"]:
        print("नमस्ते भाई! कैसे हो?")

    elif command in ["youtube", "यूट्यूब"]:
        print("YouTube खोलने की तैयारी है!")

    elif command in ["band", "बंद"]:
        print("Bhai Assistant बंद हो रहा है!")
        break

    else:
        print("माफ कीजिए, यह कमांड समझ नहीं आया।")
