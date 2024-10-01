import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

frase_emoji = emoji.emojize(frase_codificada)

print("\nFrase emojizada:")
print(frase_emoji)