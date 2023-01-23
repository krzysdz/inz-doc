from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class DNSLexer(RegexLexer):
	name = "DNS"
	aliases = ["dns", "zone"]
	filenames = ["*.dns", "*.zone"]

	tokens = {
		"root": [
			(r"^\s+", Text),
			(r"((?:\*\.)?[\w\-\.]+)(\s+)(\d+)(\s+)(IN\s+[A-Z]+)(\s+)([\w\-\.]+)$",
			 bygroups(Name.Key, Text, Number, Text, Keyword, Text, String))
		]
	}
