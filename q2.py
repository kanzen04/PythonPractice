#QUESTION 2

import sys

encryptedText = """pda lupdkj lnkcnwiiejc hwjcqwca swo ejrajpaz xu cqezk rwj nkooqi, w zqpyd ykilqpan lnkcnwiian, wxkqp 25 uawno wck. rwj nkooqi zabejaz deo ckwho bkn lupdkj wo bkhhkso: wj awou wjz ejpqepera hwjcqwca fqop wo lksanbqh wo iwfkn ykilapepkno; klaj okqnya, ok wjukja ywj ykjpnexqpa pk epo zarahkliajp; ykza pdwp eo wo qjzanopwjzwxha wo lhwej ajcheod; oqepwxehepu bkn aranuzwu pwogo, whhksejc bkn odknp zarahkliajp peiao"""

decryptMapp = {
'v':'z',
'u':'y',
'x':'b',
'w':'a'
}

# Making use of hint
for a, b in decryptMapp.iteritems():
	print "%s -> %s : distance(%s)" % (a, b, ord(b) - ord(a))

decryptedText = ""
for c in encryptedText:
	if c in decryptMapp:
		decryptedText += decryptMapp[c]
	else:
		if c.isalpha():
			distance = ord(c) + 4
			if distance > 122:
				distance = ord(c) - 22
			decryptedText += chr(distance)
		else:
			decryptedText += c

sys.stdout.write(decryptedText + '\n')



