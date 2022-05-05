from googletrans import Translator

translator = Translator()

sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요: ")
print("")

result_en = translator.translate(sentence, "en")
result_fr = translator.translate(sentence, "fr")
detected = translator.detect(sentence)

print("============= 번역 결과 =============\n")
print("입력어-", detected.lang, ":", sentence)
print("번역어1-", result_en.dest, ":", result_en.text)
print("번역어2-", result_fr.dest, ":", result_fr.text, "\n")
print("=====================================") 