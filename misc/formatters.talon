#provide both anchored and unachored commands via 'over'
<user.format_text>$: insert(format_text)
<user.format_text> over: insert(format_text)
phrase <user.phrase>$: dictate.lower(phrase)
phrase <user.phrase> over: dictate.lower(phrase)
(say | speak) <user.phrase>$: dictate.lower(phrase)
(say | speak) <user.phrase> over: dictate.lower(phrase)
word <user.word>: dictate.lower(word)


