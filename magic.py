import sys
sys.path.append('./magic')
import magic_parser_and_lexer

while True:
	text = input('magic > ')

	if ("run" in text and ".mgc" not in text):
		print("Not magic file, make sure the extension of the file is .mgc")
		continue

	if text.strip() == "": continue
	result, error = magic_parser_and_lexer.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))