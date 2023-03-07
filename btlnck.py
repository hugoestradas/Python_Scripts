from pregex.core.classes import AnyButWhitespace
from pregex.core.quantifiers import OneOrMore
from pregex.core.quantifiers import Optional
from pregex.core.operators import Either

text = "You can find me through GitHub https://github.com/hugoestradas"

pre = (
    "http"
    + Optional("s")
    + "://"
    + OneOrMore(AnyButWhitespace())
    + Either(".com", ".org")
    + OneOrMore(AnyButWhitespace())
)

print(pre.get_matches(text))