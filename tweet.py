import tweepy
# AUTENTICAR AO TWITTER
auth = tweepy.OAuthHandler("api_key", "api_secret_key")
auth.set_access_token("access_token", "access_token_secret")


api = tweepy.API(auth)


print (" ")
print ("PT-BR - Esse é um script para tweetar usando a biblioteca Tweepy")
print ("EN - This is a script to tweet using the library Tweepy")
print (" ")
print ("By: luisgbr1el")
print (" ")
print ("O que deseja tweetar? | What do you want tweet?")
print ("[1] Texto | Text")
print ("[2] Imagem | Image")
print ("[3] Texto e Imagem | Text with Image")
print (" ")
num = input("Escolha a opção: | Choose the option: ")

if num == "1":
	print("Enter para ignorar linhas. | Enter to ignore lines.")
	print(" ")
	line1 = input("Linha 1: | Line 1: ")
	line2 = input("Linha 2: | Line 2: ")
	line3 = input("Linha 3: | Line 3: ")
	line4 = input("Linha 4: | Line 4: ")
	line5 = input("Linha 5: | Line 5: ")
	print (" ")
	print ("Texto: | Text: ")
	texto = [line1, line2, line3, line4, line5]
	textof = ( '\n'.join(texto) )
	print(textof)
	print(" ")
	print("Confirma? | Confirm? (yes/no) ")
	confirmar = input("")
	if confirmar == "yes":
		print ("Tweetando... | Tweeting...")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		api.update_status(textof)
		print ("Tweetado! | Tweeted!")
	if confirmar == "no":
		print ("Operação cancelada.")

if num == "2":
	print ("Ponha a foto na minha pasta. | Put the image in my directory (this file directory)")
	print (" ")
	linkF = input("Digite o nome e a extensão da foto: (Ex: image.png) | Type the name and extension of the image: (Ex: image.png) ")
	print (" ")
	print ("Imagem: | Image: ")
	print (linkF)
	print(" ")
	print("Confirma? | Confirm? (yes/no) ")
	confirmar = input("")
	if confirmar == "yes":
		print ("Tweetando imagem... | Tweeting...")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		api.update_with_media(linkF)
		print ("Tweetado! | Tweeted!")
	if confirmar == "no":
		print ("Operação cancelada.")

if num == "3":
	print ("Ponha a foto na minha pasta. | Put the image in my directory (this file directory)")
	print (" ")
	linkF = input("Digite o nome e a extensão da foto: (Ex: image.png) | Type the name and extension of the image: (Ex: image.png) ")
	print("Texto | Text: ")
	line1 = input("Linha 1: | Line 1: ")
	line2 = input("Linha 2: | Line 2: ")
	line3 = input("Linha 3: | Line 3: ")
	line4 = input("Linha 4: | Line 4: ")
	line5 = input("Linha 5: | Line 5: ")
	print (" ")
	print ("Tweet:")
	texto = [line1, line2, line3, line4, line5]
	textof = ( '\n'.join(texto) )
	print (textof)
	print (linkF)
	print(" ")
	print("Confirma? | Confirm? (yes/no) ")
	confirmar = input("")
	if confirmar == "yes":
		print ("Tweetando... | Tweeting...")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		print (" ")
		api.update_with_media(linkF, textof)
		print ("Tweetado! | Tweeted!")
	if confirmar == "no":
		print ("Operação cancelada.")